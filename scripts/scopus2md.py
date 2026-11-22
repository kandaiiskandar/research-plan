#!/usr/bin/env python3
"""Convert Scopus AI browser-printed PDF reports to Markdown.

Written for `papers/scopus/*.pdf`: Scopus AI search reports printed to PDF from a
browser. Read-only with respect to the source PDFs.

Usage
-----
    pip install pdfplumber
    python3 scripts/scopus2md.py papers/scopus papers/scopus/markdown
    python3 scripts/scopus2md.py path/to/one.pdf out_dir

The first argument may be a directory (every *.pdf in it is converted) or a single
PDF. Each output file takes its source's name with a .md extension and opens with
YAML front matter recording the source filename, its SHA-256, page count, the
Scopus AI query and report title, and the number of tables recovered. A JSON
summary of the run is printed to stdout.

Strategy
--------
Words are read with their font size and font name (pdfplumber), then:

  * Size thresholds are ratios of each document's own modal body size, because the
    prints in this corpus come from three different paths — Safari renders body
    text at 12.8pt, Chrome at 12pt, and the ratios absorb both.
  * Text below FURNITURE_RATIO x body size is the browser page header and URL
    footer and is dropped. Some prints render that furniture *at* body size, so
    STAMP_RE and FOOTER_RE strip it by content as well, including the case where a
    page header is glued to the first words of real text.
  * Text above TITLE_RATIO x body size is the report's query line (emitted as the
    H1). The all-bold lines immediately following it are the report title, which
    goes to front matter rather than the body.
  * Headings cannot be found by size — "Quick Reference" is the same size as body
    text — so an all-bold line no longer than HEADING_MAX_CHARS becomes an H2.
    The length cap matters because Scopus AI also bolds long phrases mid-paragraph.
  * Numerals below SUP_RATIO x body size are superscript citation markers and are
    rendered inline as [n].
  * Blocks are split into tables vs prose by detecting vertical gutters: maximal
    x-ranges that no word occupies across every line of the block. Table rows are
    then separated by vertical gaps larger than the in-cell line pitch. Borderless
    tables of up to nine columns recover this way; prose has no persistent gutter.
  * tidy() repairs the artefacts of PDF line wrapping — URLs broken after ? & or =,
    hyphenated words split across lines, and combining diacritics rendered as their
    own glyph (e.g. "Cali s kan" -> "Caliskan").

Verification used when this corpus was converted: word retention against
`pdftotext -layout` with the furniture removed, which ran 97.9%-99.8% per file.
"""
import hashlib, json, re, sys
from pathlib import Path
import pdfplumber

# Size thresholds are expressed as ratios of each document's modal body size,
# because the two print batches differ (Safari 7/12.8/16pt, Chrome 8/12/15pt).
FURNITURE_RATIO    = 0.72     # below this x body size: browser header/footer
SUP_RATIO          = 0.92     # below this x body size: superscript citation marker
TITLE_RATIO        = 1.15     # above this x body size: the report's query title
MIN_GUTTER_PT      = 7.0      # narrowest whitespace that counts as a column separator
ROW_GAP_FACTOR     = 1.55     # row break when vertical gap exceeds this x median pitch
HEADING_MAX_CHARS  = 60       # longer all-bold lines are emphasised prose, not headings
WRAP_MIN_CHARS     = 60       # a line this long filled the column and wrapped
LINE_TOL           = 3.0      # words within this many points share a line


def is_bold(fontname: str) -> bool:
    f = (fontname or "").lower()
    return "bold" in f or "-bd" in f


def render_rich(ws, sup_max):
    """Line text with inline bold preserved and citation superscripts as [n]."""
    parts, buf, buf_bold = [], [], None
    for w in ws:
        if w["size"] < sup_max and re.fullmatch(r"\d{1,3}", w["text"]):
            if buf:
                parts.append(("**%s**" % " ".join(buf)) if buf_bold else " ".join(buf))
                buf, buf_bold = [], None
            parts.append("[%s]" % w["text"])
            continue
        b = is_bold(w["fontname"])
        if buf and b != buf_bold:
            parts.append(("**%s**" % " ".join(buf)) if buf_bold else " ".join(buf))
            buf = []
        buf_bold = b
        buf.append(w["text"])
    if buf:
        parts.append(("**%s**" % " ".join(buf)) if buf_bold else " ".join(buf))
    out = ""
    for p in parts:
        if out and not p.startswith("[") and not out.endswith(" "):
            out += " "
        out += p
    return re.sub(r"\s+([.,;:)])", r"\1", out).strip()


# Some prints render the browser header/footer at body size, so size alone is not
# enough: these patterns identify the furniture by content.
STAMP_RE  = re.compile(r"^\s*\d{1,2}\s*/\s*\d{1,2}\s*/\s*\d{4}\s*,?\s*\d{1,2}\s*:?\s*\d{2}"
                       r"(\s*[APap]\.?[Mm]\.?)?\s*(Scopus\s*-\s*Scopus\s*AI)?\s*")
FOOTER_RE = re.compile(r"scopus\.com/pages/ai\?|^\s*Page\s+\d+\s+of\s+\d+\s*$|^\s*\d+\s*/\s*\d+\s*$")


def strip_furniture(ln, sup_max):
    """Drop a print header/footer line, or trim a header glued to real text."""
    if FOOTER_RE.search(ln["text"]):
        return None
    m = STAMP_RE.match(ln["text"])
    if not m or not m.group(0).strip():
        return ln
    cut, pos, ws = m.end(), 0, list(ln["words"])
    keep = []
    for i, w in enumerate(ws):
        pos_end = pos + len(w["text"])
        if pos_end > cut:
            keep = ws[i:]
            break
        pos = pos_end + 1
    if not keep:
        return None
    ln = dict(ln)
    ln["words"] = keep
    ln["text"] = " ".join(w["text"] for w in keep)
    ln["rich"] = render_rich(keep, sup_max)
    ln["bold"] = all(is_bold(w["fontname"]) for w in keep)
    ln["size"] = max(w["size"] for w in keep)
    return ln


def body_size(pdf):
    """Modal character size across the document: the body text size."""
    hist = {}
    for page in pdf.pages[:4]:
        for ch in page.chars:
            k = round(ch["size"], 1)
            hist[k] = hist.get(k, 0) + 1
    return max(hist, key=hist.get) if hist else 12.0


def page_lines(page, body):
    """Return [{top, bottom, words, size, bold}] with furniture removed."""
    words = page.extract_words(extra_attrs=["size", "fontname"], keep_blank_chars=False)
    words = [w for w in words
             if w["size"] >= body * FURNITURE_RATIO and w["text"].strip()]
    lines, cur = [], []
    for w in sorted(words, key=lambda w: (round(w["top"], 1), w["x0"])):
        if cur and abs(w["top"] - cur[0]["top"]) > LINE_TOL:
            lines.append(cur); cur = []
        cur.append(w)
    if cur:
        lines.append(cur)
    out = []
    for ws in lines:
        ws = sorted(ws, key=lambda w: w["x0"])
        rec = {
            "top": min(w["top"] for w in ws),
            "bottom": max(w["bottom"] for w in ws),
            "words": ws,
            "size": max(w["size"] for w in ws),
            "bold": all(is_bold(w["fontname"]) for w in ws),
            "any_bold": any(is_bold(w["fontname"]) for w in ws),
            "text": " ".join(w["text"] for w in ws),
            "rich": render_rich(ws, body * SUP_RATIO),
        }
        rec = strip_furniture(rec, body * SUP_RATIO)
        if rec:
            out.append(rec)
    return out


def find_gutters(lines, page_width):
    """x-ranges occupied by no word across these lines -> column separators."""
    occupied = [False] * (int(page_width) + 2)
    for ln in lines:
        for w in ln["words"]:
            for x in range(int(w["x0"]), min(int(w["x1"]) + 1, len(occupied))):
                occupied[x] = True
    left = next((i for i, o in enumerate(occupied) if o), None)
    right = next((i for i in range(len(occupied) - 1, -1, -1) if occupied[i]), None)
    if left is None:
        return []
    gutters, run = [], None
    for x in range(left, right + 1):
        if not occupied[x]:
            run = x if run is None else run
        else:
            if run is not None and x - run >= MIN_GUTTER_PT:
                gutters.append((run, x))
            run = None
    return gutters


def split_rows(lines):
    """Group lines into table rows using the vertical-gap distribution."""
    if len(lines) < 2:
        return [lines]
    gaps = [lines[i + 1]["top"] - lines[i]["top"] for i in range(len(lines) - 1)]
    pitch = sorted(gaps)[len(gaps) // 2] or 1
    rows, cur = [], [lines[0]]
    for i, g in enumerate(gaps):
        if g > pitch * ROW_GAP_FACTOR:
            rows.append(cur); cur = []
        cur.append(lines[i + 1])
    rows.append(cur)
    return rows


def row_cells(row_lines, bounds):
    """Assign each word to a column by its midpoint, preserving line order."""
    cells = [[] for _ in bounds]
    for ln in row_lines:
        per = [[] for _ in bounds]
        for w in ln["words"]:
            mid = (w["x0"] + w["x1"]) / 2
            idx = 0
            for i, (lo, hi) in enumerate(bounds):
                if lo <= mid < hi:
                    idx = i; break
            else:
                idx = len(bounds) - 1 if mid >= bounds[-1][0] else 0
            per[idx].append(w["text"])
        for i, chunk in enumerate(per):
            if chunk:
                cells[i].append(" ".join(chunk))
    return [" ".join(c).strip() for c in cells]


DIACRITIC = "\u015f\u015e\u011f\u011e\u0131\u0130\u00e7\u00c7\u00f6\u00d6\u00fc\u00dc\u00e9\u00c9\u00e8\u00c8\u00e1\u00c1\u00e0\u00c0\u00f1\u00d1\u00e5\u00c5\u00f8\u00d8"


def tidy(t: str) -> str:
    """Repair artefacts introduced by PDF line wrapping."""
    # a URL broken across lines after ? & or =
    for _ in range(2):
        t = re.sub(r"(https?://\S*[?&=])\s+(\S+)", r"\1\2", t)
    # a hyphenated word broken across lines
    t = re.sub(r"(?<=[a-z])-\s+(?=[a-z])", "-", t)
    # a combining diacritic rendered as its own glyph, e.g. "Cal\u0131 \u015f kan"
    t = re.sub(r"(?<=\w) ([" + DIACRITIC + r"])(?=[ ,.;:)])", r"\1", t)
    t = re.sub(r"(?<=[" + DIACRITIC + r"]) (?=\w)", "", t)
    return re.sub(r"\s+([.,;:)])", r"\1", t).strip()


def esc(s):
    return tidy(s).replace("|", "\\|").replace("\n", " ").strip()


def emit_table(rows, bounds, out):
    table = [row_cells(r, bounds) for r in rows]
    table = [r for r in table if any(c for c in r)]
    if len(table) < 2:
        for r in table:
            if any(r):
                out.append(" ".join(c for c in r if c)); out.append("")
        return 0
    ncol = len(bounds)
    header = [esc(c) or f"Col {i+1}" for i, c in enumerate(table[0])]
    out.append("| " + " | ".join(header) + " |")
    out.append("|" + "|".join([" --- "] * ncol) + "|")
    for r in table[1:]:
        out.append("| " + " | ".join(esc(c) for c in r) + " |")
    out.append("")
    return 1


def flush_block(lines, page_width, out, stats):
    """A run of body lines: table if it has gutters and several rows, else prose."""
    if not lines:
        return
    gutters = find_gutters(lines, page_width)
    rows = split_rows(lines)
    if len(gutters) >= 1 and len(rows) >= 2:
        left = min(w["x0"] for ln in lines for w in ln["words"])
        right = max(w["x1"] for ln in lines for w in ln["words"])
        edges = [left - 1] + [(a + b) / 2 for a, b in gutters] + [right + 1]
        bounds = list(zip(edges[:-1], edges[1:]))
        if len(bounds) >= 2:
            stats["tables"] += emit_table(rows, bounds, out)
            return
    # prose: rejoin wrapped lines, break paragraphs on larger vertical gaps
    for row in rows:
        text = " ".join(ln["rich"] for ln in row)
        text = tidy(re.sub(r"\s+", " ", text))
        if text:
            out.append(text); out.append("")


def convert(pdf_path: Path):
    stats = {"pages": 0, "tables": 0, "headings": 0}
    out, meta = [], {}
    pending, subtitle, subtitle_open = [], [], False
    with pdfplumber.open(str(pdf_path)) as pdf:
        stats["pages"] = len(pdf.pages)
        body = body_size(pdf)
        for pageno, page in enumerate(pdf.pages, 1):
            for ln in page_lines(page, body):
                if ln["size"] >= body * TITLE_RATIO:
                    subtitle_open = True
                    flush_block(pending, page.width, out, stats); pending = []
                    meta.setdefault("query", ln["text"])
                    out.append(f"# {ln['text']}"); out.append("")
                    stats["headings"] += 1
                elif subtitle_open and ln["bold"] and (
                        not subtitle or len(subtitle[-1]) >= WRAP_MIN_CHARS):
                    # the report title: one or more wrapped all-bold lines
                    subtitle.append(ln["text"])
                elif ln["bold"] and len(ln["text"]) <= HEADING_MAX_CHARS:
                    subtitle_open = False
                    flush_block(pending, page.width, out, stats); pending = []
                    htxt = re.sub(r"\s+([.,;:])", r"\1", ln["text"]).strip()
                    out.append(f"## {htxt}"); out.append("")
                    stats["headings"] += 1
                else:
                    subtitle_open = False
                    m = re.match(r"^Generated by Scopus AI,\s*(.+)$", ln["text"])
                    if m and "generated" not in meta:
                        meta["generated"] = m.group(1).strip()
                        continue
                    pending.append(ln)
            flush_block(pending, page.width, out, stats); pending = []
    if subtitle:
        meta["title"] = re.sub(r"\s+", " ", " ".join(subtitle)).strip()
    body = "\n".join(out)
    body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"
    sha = hashlib.sha256(pdf_path.read_bytes()).hexdigest()
    front = [
        "---",
        f'source_pdf: "{pdf_path.name}"',
        f'source_sha256: "{sha}"',
        f'source_pages: {stats["pages"]}',
        f'scopus_ai_generated: "{meta.get("generated", "")}"',
        f'query: "{meta.get("query", "").replace(chr(34), chr(39))}"',
        f'report_title: "{meta.get("title", "").replace(chr(34), chr(39))}"',
        f'converted_tables: {stats["tables"]}',
        'converter: "scopus2md.py (pdfplumber)"',
        "---",
        "",
    ]
    return "\n".join(front) + body, stats


if __name__ == "__main__":
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    dst.mkdir(parents=True, exist_ok=True)
    report = []
    targets = sorted(src.glob("*.pdf")) if src.is_dir() else [src]
    for pdf in targets:
        md, st = convert(pdf)
        outfile = dst / (pdf.stem + ".md")
        outfile.write_text(md, encoding="utf8")
        report.append({"pdf": pdf.name, "md": outfile.name, "chars": len(md), **st})
    print(json.dumps(report, indent=1))
