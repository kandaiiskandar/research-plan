# Scopus Metrix — paper corpus

21 research papers, converted from PDF to Markdown. Batch 1 (15 papers) on 19 November 2026; batch 2 (6 papers) on 20 November 2026.

Source: `~/Downloads/Scopus Metrix`. Converter: [`scripts/paper2md.py`](../../scripts/paper2md.py).

Two further papers were converted with the same tool but filed under [`papers/sources/`](../sources/) with the other individually-supplied papers, their Markdown in `papers/sources/markdown/`:

| Paper | Pages | Headings | Tables | Equations | Fig. caps\* | Refs\*\* |
|---|---:|---:|---:|---:|---:|---:|
| Functional Safety Architectural Patterns for AI-Based Critical Systems | 25 | 42 | 4 | 2 | 9 | 24 |
| Safety Shielding under Delayed Observation | 6 | 13 | 0 | 1 | 7 | 0 |
| Safe Reinforcement Learning Using Probabilistic Shields | 16 | 19 | 0 | 9 | 5 | 0 |
| Safe Reinforcement Learning via Shielding under Partial Observability | 9 | 15 | 2 | 0 | 7 | 0 |
| PIGDreamer — Privileged Information Guided World Models for Safe Partially Observable RL | 17 | 37 | 1 | 24 | 9 | 0 |
| Safe RL via Recovery-based Shielding with Gaussian Process Dynamics Models | 10 | 20 | 0 | 33 | 2 | 59 |
| ProSh — Probabilistic Shielding for Model-free Reinforcement Learning | 3 | 14 | 0 | 5 | 0 | 19 |

## Layout

| Path | Contents |
|---|---|
| `pdf/` | The 21 original PDFs, byte-identical to the source (verified with `cmp`) |
| `markdown/` | One `.md` per paper, slug-named |

**Figure images are deliberately not stored.** Batch 1's 262 extracted images (49 MB) were deleted on 20 November 2026 and batch 2's were discarded at conversion time: the PDF is the reference for any figure. Figure *captions* are preserved in full in the Markdown, at the position where the figure appears, with the page marker above them — so the caption tells you what the figure is and the page marker tells you where to find it. If the images are ever needed, re-render them from the PDFs with `python3 scripts/paper2md.py papers/scopus-metrix/pdf <markdown-out> <figures-out>` — the converter always writes both, so point it at a scratch directory to avoid overwriting the Markdown in place.

## What the conversion preserves

- **Section headings** — detected from font size, boldness and numbered/roman heading patterns
- **Tables** — detected geometrically and emitted as Markdown tables
- **Equations** — display equations kept verbatim in fenced ` ```math ` blocks with their equation numbers
- **Figure captions** — kept in full, in position, below the page marker for the page the figure is on
- **References** — full reference text retained; entries split one per line where the entry markers are recognised
- **Page numbers** — `<!-- page N -->` marker at every page break
- **Running headers and footers removed** — repeated page headers (journal name, author list, page number) detected across pages and dropped, so they do not pollute the heading outline. 429 such blocks removed across this corpus

## Conversion yield

### Batch 1 — 19 November 2026

| Paper | Pages | Headings | Tables | Equations | Fig. caps\* | Refs\*\* |
|---|---:|---:|---:|---:|---:|---:|
| A Finely Integrated Risk Evaluation Methodology for Life-Critical Embedded Systems | 26 | 27 | 0 | 20 | 13 | 3 |
| A Hybrid Framework for Nuclear-Grade AI Assurance … | 4 | 4 | 1 | 0 | 1 | 9 |
| A human-centered hybrid AI framework … emergency triage | 15 | 24 | 0 | 15 | 27 | 27 |
| Can we Defend Against the Unknown? … Threshold Selection | 13 | 21 | 0 | 0 | 5 | 1 |
| Causal Structure Learning Assumptions Shape Counterfactual Safety | 27 | 27 | 1 | 30 | 6 | 3 |
| Cost-sensitive security controls for continuous integration pipelines | 16 | 46 | 0 | 8 | 12 | 1 |
| Dynamic Model Predictive Shielding for Provably Safe RL | 29 | 22 | 2 | 5 | 8 | 102 |
| Empirically derived evaluation requirements … safety-critical settings | 11 | 0 | 0 | 0 | 0 | 0 |
| Expert Evaluation and the Limits of Human Feedback in Mental Health AI Safety Testing | 27 | 18 | 0 | 0 | 1 | 74 |
| Learning to Make Adherence-Aware Advice | 12 | 25 | 0 | 25 | 2 | 0 |
| Merging Deep Learning with Rule-Based and Explainable Techniques … | 6 | 2 | 2 | 5 | 6 | 14 |
| Multi-Objective Evaluation of Lightweight AI Models on Low-Cost Edge Devices | 21 | 29 | 0 | 9 | 0 | 3 |
| Optimal Runtime Assurance via Reinforcement Learning | 10 | 6 | 3 | 9 | 9 | 47 |
| Oral health reception and risk classification protocol | 9 | 0 | 2 | 0 | 1 | 29 |
| Safety of human-AI cooperative decision-making within intensive care | 17 | 9 | 0 | 0 | 5 | 64 |
| **Subtotal** | **243** | **260** | **11** | **126** | **96** | **377** |

### Batch 2 — 20 November 2026

| Paper | Pages | Headings | Tables | Equations | Fig. caps\* | Refs\*\* |
|---|---:|---:|---:|---:|---:|---:|
| A Rule-Based Shield — Accumulating Safety Rules from Catastrophic Action Effects | 12 | 16 | 0 | 4 | 6 | 0 |
| A two-layer safe RL framework for multi-constraint reservoir operation — action masking and Lagrangian dual | 19 | 20 | 0 | 35 | 10 | 1 |
| Adaptive Shielding via Parametric Safety Proofs | 28 | 26 | 0 | 39 | 5 | 47 |
| Feasibility-First Risk Management for Clinical AI — Release, Monitoring, Rollback and Withholding | 9 | 1 | 3 | 0 | 0 | 1 |
| Pure-Past Action Masking | 10 | 6 | 0 | 12 | 3 | 0 |
| Situation-aware recommender systems — a systematic review and framework for trustworthy recommendations | 38 | 54 | 0 | 10 | 2 | 0 |
| **Subtotal** | **116** | **123** | **3** | **100** | **26** | **49** |
| **Corpus total** | **359** | **383** | **14** | **226** | **122** | **426** |

\* Figure captions detected **and** located against artwork in the PDF. A paper showing 0 has figures the detector did not bound, not necessarily no figures — consult the PDF. Batch 2 detected 59 captions in total but located artwork for only 26, so the Markdown carries more captions than this column counts.

\*\* **Entry counts, not bibliography sizes** — see limit 4. A low number means the splitter did not recognise the entry markers, **not** that references are missing.

## Known conversion limits — read before quoting

1. **Equations are extracted glyph by glyph and are frequently mangled.** PDF text extraction has no notion of mathematical structure: subscripts, superscripts, fractions and accents are flattened into a character stream. Every `math` block is a *locator*, not a transcription. **Check the PDF before quoting any formula.**
2. **Five papers yielded no or few headings** — *Empirically derived evaluation requirements* (0), *Oral health reception* (0), *Feasibility-First Risk Management* (1), *Merging Deep Learning* (2) and *Pure-Past Action Masking* (6). Their body text extracted in full; only the heading **styling** was unconventional enough to defeat font-based detection. Navigate those by page marker.
3. **Figures must be read in the PDF.** This is by design (see Layout). Where the detector failed to locate a figure's artwork, its caption may also be missing from the Markdown — *Empirically derived evaluation requirements*, *Multi-Objective Evaluation* and *Feasibility-First Risk Management* yielded none at all, so their figures are not indexed here in any form.
4. **Reference counts are entry counts, not bibliography sizes.** A paper whose reference list is set without `[n]` markers reports a low count even though **the full reference text is present** — verified by inspection for *Pure-Past Action Masking* (0), *A Rule-Based Shield* (0), *Situation-aware recommender systems* (0) and *Feasibility-First Risk Management* (1), each of which carries its complete bibliography as running text under a `## References` heading. Search the text rather than trusting the count.
5. **Table detection is geometric** and keyed to ruled cells. Papers using whitespace-aligned tables with no rules report 0 tables while the content survives as text. Two filters guard against figure panels being misread as tables: cells longer than 200 characters, and mathematical-glyph density above 2%. Conversely, an undetected table's header cells can still surface as spurious `###` headings.
6. **Multi-column reading order is reconstructed**, not native. Left column is emitted before right. Where a figure or table spans both columns the surrounding prose may be ordered slightly differently from the printed page.
