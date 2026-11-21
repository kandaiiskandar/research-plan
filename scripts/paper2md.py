#!/usr/bin/env python3
"""
paper2md.py — convert academic-paper PDFs to structured Markdown.

Unlike scripts/scopus2md.py (built for Scopus AI browser-printed reports), this
targets typeset research papers: two-column layouts, numbered sections, ruled
tables, numbered equations, figure captions and reference lists.

Preserved:
  * section headings        — font-size + boldness + numbered-heading patterns
  * tables                  — detected geometrically, emitted as Markdown
  * equations               — display equations kept verbatim in fenced blocks,
                              with their equation number, and flagged because
                              PDF glyph extraction mangles math
  * figure captions         — kept inline, linked to the rendered figure
  * references              — one entry per line
  * page numbers            — `<!-- page N -->` markers at every page break
  * figures                 — each figure caption's region is RENDERED at 200 dpi
                              so vector diagrams are captured, not just rasters

Usage:
    python3 paper2md.py <pdf-dir> <md-out-dir> <fig-out-dir>
"""
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

import pymupdf  # noqa

# ── tuning ────────────────────────────────────────────────────────────────
HEAD_RATIO      = 1.06   # span size > body * this, with bold, is a heading
H1_RATIO        = 1.30   # and above this, a top-level heading
HEAD_MAX_CHARS  = 140
FIG_DPI         = 200
FIG_MIN_H       = 40     # pt; ignore a figure region shorter than this
FIG_MAX_H       = 520    # pt; cap how far above a caption we render
RASTER_MIN_PX   = 120    # embedded images smaller than this on a side are furniture
GUTTER_MIN      = 18     # pt of empty width to call a page two-column

# A caption starts with Figure/Table + number. Prose often starts the same way
# ("Figure 1 gives an overview..."), so require either punctuation straight after
# the number or a short block. CAPTION_MAX_PROSE keeps long sentences out.
CAPTION_RE = re.compile(
    r"^\s*(?:(Fig(?:ure)?\.?)\s*(\d+)|(TABLE|Table)\s+([IVXLCDM]+|\d+))"
    r"\s*(?P<punct>[:.–—-])?", re.I)
CAPTION_MAX_PROSE = 200
EQNUM_RE   = re.compile(r"\(\s*\d+[a-z]?\s*\)\s*$")
NUMHEAD_RE = re.compile(r"^\s*(\d+(?:\.\d+)*)\.?\s+(\S.{0,120})$")
ROMHEAD_RE = re.compile(r"^\s*([IVXLC]+)\.\s+(\S.{0,120})$")
REFHEAD_RE = re.compile(r"^\s*(?:\d+\.?\s*|[IVXLC]+\.\s*)?(REFERENCES?|Bibliography|References)\s*$", re.I)
REFENTRY_RE = re.compile(r"^\s*(?:\[\s*\d+\s*\]|\(\s*\d+\s*\)|\d+\.)\s+")
MATH_CHARS = set("∑∫∂∇√≤≥≠≈±×÷⊂⊆∈∀∃→←↔⇒⇔αβγδεθλμσφψωΩΔΣΠ")


def is_caption(text: str, m) -> bool:
    """True for a real caption, false for prose that opens with "Figure N".

    Punctuation straight after the number settles it ("Fig. 1. Overview").
    Without punctuation, the next word must not be lower-case: "Fig. 4 shows
    the reference architecture..." is a sentence, "Figure 4 Overview" is not.
    """
    if m.group("punct"):
        return True
    if len(text) > CAPTION_MAX_PROSE:
        return False
    rest = text[m.end():].lstrip()
    return bool(rest) and not rest[0].islower()


def furn_key(text: str) -> str:
    """Normalise a header/footer: drop the page number so the same running
    header collapses to one key across pages."""
    t = " ".join(text.split())
    return re.sub(r"^\d{1,4}\s+|\s+\d{1,4}$", "", t).strip().lower()


def edge_ys(page) -> set:
    """y0 of the topmost and bottommost text block on the page.

    Keying on page position rather than a fixed margin band: measured headers
    in one paper sat at y=71 on a 792pt page, just outside an 8.5% band, so a
    band threshold is a guess while "first or last block" is not.
    """
    bs = [b for b in page.get_text("blocks") if b[6] == 0 and b[4].strip()]
    if not bs:
        return set()
    return {round(min(bs, key=lambda b: b[1])[1], 1),
            round(max(bs, key=lambda b: b[3])[1], 1)}


def furniture(doc) -> set:
    """Normalised text of running headers and footers.

    A page header such as "4  Irune Agirre, Irune Yarza, ..." matches the
    numbered-heading pattern and otherwise becomes an `## ` heading on every
    other page, wrecking the document outline.
    """
    seen = Counter()
    for page in doc:
        edges = edge_ys(page)
        for b in page.get_text("blocks"):
            if b[6] != 0 or round(b[1], 1) not in edges:
                continue
            t = " ".join(b[4].split())
            if not t or len(t) > 160:
                continue
            k = furn_key(t)
            if k:
                seen[k] += 1
    return {k for k, n in seen.items() if n >= 3}


def is_furniture(text: str, bbox, edges: set, marks: set) -> bool:
    if round(bbox[1], 1) not in edges:
        return False
    t = " ".join(text.split())
    if re.fullmatch(r"\d{1,4}", t):           # a bare page number
        return True
    k = furn_key(t)
    return bool(k) and k in marks


def slug(name: str) -> str:
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    return re.sub(r"[\s_]+", "-", s)[:80]


def body_size(doc) -> float:
    c = Counter()
    for page in doc[: min(8, doc.page_count)]:
        for blk in page.get_text("dict")["blocks"]:
            for line in blk.get("lines", []):
                for sp in line["spans"]:
                    if sp["text"].strip():
                        c[round(sp["size"], 1)] += len(sp["text"])
    return c.most_common(1)[0][0] if c else 10.0


def columns(page):
    """Return x-midpoint if the page is two-column, else None."""
    blocks = [b for b in page.get_text("blocks") if b[6] == 0]
    if len(blocks) < 6:
        return None
    w = page.rect.width
    mid = w / 2
    left = [b for b in blocks if b[2] < mid + 10]
    right = [b for b in blocks if b[0] > mid - 10]
    if len(left) < 3 or len(right) < 3:
        return None
    gutter = min(b[0] for b in right) - max(b[2] for b in left)
    return mid if gutter >= GUTTER_MIN else None


def ordered_blocks(page):
    """Blocks in reading order, two-column aware."""
    blocks = [b for b in page.get_text("blocks") if b[6] == 0 and b[4].strip()]
    mid = columns(page)
    if mid is None:
        return sorted(blocks, key=lambda b: (round(b[1], 1), b[0]))
    left = sorted([b for b in blocks if (b[0] + b[2]) / 2 < mid],
                  key=lambda b: (round(b[1], 1), b[0]))
    right = sorted([b for b in blocks if (b[0] + b[2]) / 2 >= mid],
                   key=lambda b: (round(b[1], 1), b[0]))
    return left + right


def span_meta(page):
    """Map block index -> (max size, all-bold) for heading detection."""
    meta = {}
    for i, blk in enumerate(page.get_text("dict")["blocks"]):
        if "lines" not in blk:
            continue
        sizes, bolds, txt = [], [], []
        for line in blk["lines"]:
            for sp in line["spans"]:
                if sp["text"].strip():
                    sizes.append(sp["size"])
                    bolds.append(bool(sp["flags"] & 2 ** 4))
                    txt.append(sp["text"])
        if sizes:
            meta[("".join(txt)).strip()[:60]] = (max(sizes), all(bolds))
    return meta


CTRL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")


def tidy(t: str) -> str:
    # PDF glyph streams carry stray control bytes; left in, they make the
    # output a "binary file" to grep and other line tools.
    t = CTRL_RE.sub("", t)
    t = t.replace("ﬀ", "ff").replace("ﬁ", "fi").replace("ﬂ", "fl")
    t = re.sub(r"(\w)-\n(\w)", r"\1\2", t)          # de-hyphenate across lines
    t = re.sub(r"[ \t]*\n[ \t]*", " ", t)            # unwrap within a block
    t = re.sub(r"\s{2,}", " ", t)
    return t.strip()


def table_md(tbl) -> str:
    try:
        rows = tbl.extract()
    except Exception:
        return ""
    rows = [[(c or "").replace("\n", " ").replace("|", "\\|").strip() for c in r]
            for r in rows if any((c or "").strip() for c in r)]
    if len(rows) < 2:
        return ""
    # Figure panels are drawn from boxes and get picked up as tables. Reject a
    # candidate whose cells are mostly empty or mostly non-word glyphs.
    cells = [c for r in rows for c in r]
    if not cells:
        return ""
    filled = [c for c in cells if c]
    if len(filled) / len(cells) < 0.45:
        return ""
    joined = " ".join(filled)
    # No letter-density test: a genuine results table is mostly numbers, so
    # letter density rejects exactly the tables worth keeping (measured at
    # 0.23-0.26 for real results tables vs 0.39 for a figure's pseudocode).
    if max(len(c) for c in cells) > 200:   # a whole figure crammed into one cell
        return ""
    # Pseudocode panels inside figures are dense in arrows and hats.
    mathy = sum(joined.count(ch) for ch in "←→⊥ˆ′≜∧∨¬")
    if mathy / max(len(joined), 1) > 0.02:
        return ""
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    head, *rest = rows
    if not any(head):
        head = [f"col{i+1}" for i in range(ncol)]
    out = ["| " + " | ".join(head) + " |",
           "|" + "|".join(["---"] * ncol) + "|"]
    out += ["| " + " | ".join(r) + " |" for r in rest]
    return "\n".join(out)


def block_above(page, caption_rect, mid):
    """Bottom edge of the nearest text block above the caption, same column.

    Two-column reading order emits the whole left column before the right, so
    the previously emitted block is often BELOW a right-column caption. Using
    it as the clip top silently produced empty figures on the first run.
    """
    best = page.rect.y0
    for b in page.get_text("blocks"):
        if b[6] != 0 or not b[4].strip():
            continue
        cx = (b[0] + b[2]) / 2
        if mid is not None:
            same = (cx < mid) == ((caption_rect.x0 + caption_rect.x1) / 2 < mid)
            if not same:
                continue
        if b[3] <= caption_rect.y0 - 2:
            best = max(best, b[3])
    return best


def artwork_above(page, caption_rect):
    """Union bbox of vector drawings and images sitting above a caption.

    Targeting the actual artwork geometry, rather than inferring the figure
    from gaps between text blocks, is what makes full-width figures work: a
    two-column page puts a spanning figure's caption near the gutter, so a
    column-based guess clips it to half and often to nothing.
    """
    lo = caption_rect.y0 - FIG_MAX_H
    box = None
    items = []
    try:
        items += [pymupdf.Rect(d["rect"]) for d in page.get_drawings()]
    except Exception:
        pass
    try:
        items += [pymupdf.Rect(i["bbox"]) for i in page.get_image_info()]
    except Exception:
        pass
    for r in items:
        # A box diagram is built from strokes that are ~0pt on one axis, so
        # requiring BOTH dimensions to be non-trivial discards exactly the
        # lines that make up an architecture figure. Size on either axis.
        if r.is_empty or max(r.width, r.height) < 8:
            continue
        if r.y1 <= caption_rect.y0 - 1 and r.y1 >= lo:
            box = r if box is None else (box | r)
    return box


def render_figure(page, caption_rect, mid, out_png, prev_bottom):
    """Render a figure region: artwork geometry first, text gap as fallback."""
    art = artwork_above(page, caption_rect)
    if art is not None and art.height >= FIG_MIN_H:
        clip = pymupdf.Rect(max(art.x0 - 6, page.rect.x0),
                            max(art.y0 - 6, page.rect.y0),
                            min(art.x1 + 6, page.rect.x1),
                            min(art.y1 + 6, caption_rect.y0 - 1))
    else:
        top = max(prev_bottom + 2, caption_rect.y0 - FIG_MAX_H, page.rect.y0)
        if caption_rect.y0 - top < FIG_MIN_H:
            return False
        if mid is None:
            x0, x1 = page.rect.x0 + 20, page.rect.x1 - 20
        elif (caption_rect.x0 + caption_rect.x1) / 2 < mid:
            x0, x1 = page.rect.x0 + 20, mid
        else:
            x0, x1 = mid, page.rect.x1 - 20
        clip = pymupdf.Rect(x0, top, x1, caption_rect.y0 - 1)
    if clip.is_empty or clip.height < FIG_MIN_H or clip.width < 40:
        return False
    pix = page.get_pixmap(clip=clip, dpi=FIG_DPI)
    if pix.width < 60 or pix.height < 40:
        return False
    # A connected folder may forbid deletion, and saving over an existing file
    # unlinks it first. Never overwrite: the same caption can be matched twice.
    if Path(out_png).exists():
        return True
    pix.save(out_png)
    return True


def convert(pdf_path: Path, md_dir: Path, fig_dir: Path) -> dict:
    doc = pymupdf.open(pdf_path)
    base = slug(pdf_path.stem)
    figs = fig_dir / base
    figs.mkdir(parents=True, exist_ok=True)

    bsize = body_size(doc)
    marks = furniture(doc)
    lines = [f"# {pdf_path.stem}", "",
             f"> **Source PDF:** `{pdf_path.name}` · **Pages:** {doc.page_count} · "
             f"Converted by `scripts/paper2md.py` from the original PDF.", ""]
    stats = Counter()
    in_refs = False

    for pno, page in enumerate(doc, start=1):
        lines += ["", f"<!-- page {pno} -->", ""]
        mid = columns(page)
        meta = span_meta(page)
        page_edges = edge_ys(page)

        # Figure regions first: a figure's internal boxes are often detected as
        # a table, so the figure's extent is needed before tables are accepted.
        # Tables on this page, keyed by vertical position. Figure-panel false
        # positives are filtered by table_md's content tests, not by geometry:
        # a figure sits right next to its results table often enough that any
        # proximity or artwork-overlap rule also discards the real one.
        tables, table_bands = [], []
        try:
            for t in page.find_tables().tables:
                md = table_md(t)
                if md:
                    tables.append((t.bbox[1], md))
                    table_bands.append((t.bbox[1], t.bbox[3]))
                    stats["tables"] += 1
        except Exception:
            pass

        emitted_tbl = set()
        prev_bottom = page.rect.y0

        for blk in ordered_blocks(page):
            x0, y0, x1, y1, raw, *_ = blk
            text = tidy(raw)
            if not text:
                continue
            if is_furniture(text, blk[:4], page_edges, marks):
                stats["furniture"] += 1
                continue

            # flush any table that sits above this block
            for ti, (ty, md) in enumerate(tables):
                if ti not in emitted_tbl and ty <= y0:
                    lines += ["", md, ""]
                    emitted_tbl.add(ti)

            # skip text that lies inside a detected table's band
            if any(ty0 - 2 <= y0 <= ty1 + 2 for ty0, ty1 in table_bands):
                prev_bottom = y1
                continue

            size, bold = meta.get(text[:60], (bsize, False))

            # figure / table caption
            m = CAPTION_RE.match(text)
            if m and is_caption(text, m):
                if m.group(1):  # a figure, not a table caption
                    png = figs / f"p{pno:03d}-fig{m.group(2)}.png"
                    rect = pymupdf.Rect(x0, y0, x1, y1)
                    above = block_above(page, rect, mid)
                    if render_figure(page, rect, mid, str(png), above):
                        rel = f"../figures/{base}/{png.name}"
                        lines += ["", f"![{text[:90]}]({rel})", ""]
                        stats["figures"] += 1
                lines += [f"**{text}**", ""]
                prev_bottom = y1
                stats["captions"] += 1
                continue

            # references section
            if REFHEAD_RE.match(text):
                in_refs = True
                lines += ["", "## References", ""]
                prev_bottom = y1
                continue
            if in_refs:
                # Entries wrap across blocks; start a new one only at [n],
                # otherwise append to the entry already open.
                parts = [p.strip() for p in
                         re.split(r"(?=\[\s*\d+\s*\]\s)", text) if p.strip()]
                for p in parts:
                    if REFENTRY_RE.match(p):
                        lines += ["", p]
                        stats["refs"] += 1
                    elif lines and lines[-1] and not lines[-1].startswith("#"):
                        lines[-1] = (lines[-1] + " " + p).strip()
                    else:
                        lines += ["", p]
                prev_bottom = y1
                continue

            # display equation: short, numbered or math-heavy, not prose
            is_eq = (len(text) < 300 and
                     (EQNUM_RE.search(text) or
                      (sum(ch in MATH_CHARS for ch in text) >= 2 and len(text) < 160)) and
                     not text.endswith(".") and text.count(" ") < 40)
            if is_eq:
                lines += ["", "```math", raw.strip(), "```", ""]
                stats["equations"] += 1
                prev_bottom = y1
                continue

            # headings
            nm, rm = NUMHEAD_RE.match(text), ROMHEAD_RE.match(text)
            is_head = (
                len(text) <= HEAD_MAX_CHARS and not text.endswith(".") and (
                    (size >= bsize * HEAD_RATIO and bold) or
                    (nm and (bold or size >= bsize)) or
                    (rm and (bold or text.isupper())) or
                    (text.isupper() and 3 <= len(text) <= 60 and size >= bsize)))
            if is_head:
                lvl = 2 if (size >= bsize * H1_RATIO or rm or
                            (nm and "." not in nm.group(1))) else 3
                lines += ["", "#" * lvl + " " + text, ""]
                stats["headings"] += 1
                prev_bottom = y1
                continue

            lines += [text, ""]
            prev_bottom = y1

        for ti, (_, md) in enumerate(tables):
            if ti not in emitted_tbl:
                lines += ["", md, ""]

    # large embedded rasters, as a fallback for figures the caption pass missed
    for pno, page in enumerate(doc, start=1):
        for i, img in enumerate(page.get_images(full=True)):
            try:
                info = doc.extract_image(img[0])
            except Exception:
                continue
            if info["width"] < RASTER_MIN_PX or info["height"] < RASTER_MIN_PX:
                continue
            p = figs / f"p{pno:03d}-img{i}.{info['ext']}"
            if not p.exists():
                p.write_bytes(info["image"])
                stats["rasters"] += 1

    md = CTRL_RE.sub("", "\n".join(lines))   # also covers verbatim math blocks
    md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
    if stats["equations"]:
        md = md.replace(
            "Converted by `scripts/paper2md.py` from the original PDF.",
            "Converted by `scripts/paper2md.py` from the original PDF. "
            "**Equations are extracted glyph-by-glyph and may be mangled — "
            "check the PDF before quoting any formula.**")
    (md_dir / f"{base}.md").write_text(md, encoding="utf-8")
    doc.close()
    try:
        if not any(figs.iterdir()):
            figs.rmdir()        # best effort; deletion may be forbidden here
    except OSError:
        pass
    stats["pages"] = len(md.split("<!-- page")) - 1
    return stats


def main():
    src, md_dir, fig_dir = (Path(a) for a in sys.argv[1:4])
    md_dir.mkdir(parents=True, exist_ok=True)
    fig_dir.mkdir(parents=True, exist_ok=True)
    total = Counter()
    for pdf in sorted(src.glob("*.pdf")):
        try:
            s = convert(pdf, md_dir, fig_dir)
            total.update(s)
            print(f"OK   {pdf.name[:62]:62s} "
                  f"p{s['pages']:>3} h{s['headings']:>3} t{s['tables']:>2} "
                  f"e{s['equations']:>3} f{s['figures']:>2} r{s['refs']:>3}")
        except Exception as e:
            print(f"FAIL {pdf.name[:62]:62s} {type(e).__name__}: {e}")
    print("\nTOTAL", dict(total))


if __name__ == "__main__":
    main()
