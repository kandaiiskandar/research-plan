# AAI 2026 — Primary Threat Papers Source Package

## Purpose

This package contains **source-only Markdown extractions** of the five uploaded primary papers selected for the AAI 2026 literature-threat verification stage.

**Important:** These files are for source ingestion/storage first. They contain no research-gap verdict, comparison, summary, reinterpretation, or manuscript drafting.

## Source files

1. `01_legitimacy_layer.md` — *The Legitimacy Layer: A Runtime Governance Architecture for Human Oversight in AI-Assisted Critical Decision Systems*
2. `02_a4_gov.md` — *A⁴-Gov: A Governance Architecture for AI Service Systems*
3. `03_controlled_agentic_ai_systems.md` — *Controlled Agentic AI Systems: A Governance-Driven Architecture for Auditable and Reproducible Decision Pipelines*
4. `04_dsa_safetybench.md` — *DSA-SafetyBench: A Safety-Aware Benchmark for Artificial-Intelligence-Based Dynamic Security Assessment in Energy Systems*
5. `05_clinical_operational_safety.md` — *Defining Operational Safety in Clinical Artificial Intelligence Systems*

## Extraction convention

- Each Markdown file is extracted from the corresponding uploaded PDF.
- `## PDF Page N` markers preserve PDF page boundaries.
- Extracted page text is placed in fenced text blocks to minimize accidental reformatting.
- Extraction uses Poppler `pdftotext -layout`.
- No OCR was applied because these PDFs contain extractable text.
- No content was intentionally summarized, reconciled, corrected, or supplemented from external sources.
- PDF multi-column layouts, mathematical notation, tables, footnotes, and figures can lose structure during plain-text extraction. The original PDFs remain authoritative when exact layout or visual content matters.

## Recommended instruction to the agent

> Store/ingest these five primary-source extractions as reference sources. Do not analyze, compare, summarize, infer a research gap, alter the locked research chain, or draft manuscript text yet. Preserve each paper as an independent source and wait for the next task.
