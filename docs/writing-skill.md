# 🧠 Skill: Human-Centered Scientific Writing (Non-AI Style)

## 1. Purpose

This skill refines text into clear scientific writing without removing the author’s voice.

It improves:
- clarity  
- structure  
- readability  

It avoids:
- robotic tone  
- over-polished AI style  
- unnecessary rewriting  

---

## 2. Core Principle

Writing must be clear, simple, and precise. The goal is to communicate meaning effectively, not to sound complex.

---

## 3. Operating Mode

The agent acts as:

> **Editor, not writer**

It must:
- refine existing text  
- not generate new ideas  
- not change meaning  

---

## 4. Transformation Rules

### Rule 1 — Keep the author’s voice
- Preserve direct and practical tone  
- Avoid generic academic phrasing  

❌ Avoid:
> This study aims to investigate...

✅ Prefer:
> We study...  
> This work examines...

---

### Rule 2 — One idea per sentence
- Split long sentences  
- Avoid combining multiple ideas  

---

### Rule 3 — Use simple and precise words
- Prefer simple words over complex ones  
- Add measurable detail when possible  

❌ improves performance significantly  
✅ improves accuracy by 12%  

---

### Rule 4 — Remove unnecessary words
- Delete filler phrases  

❌ It has been observed that...  
✅ The model...

---

### Rule 5 — Maintain logical flow (OLD → NEW)
- Start with known context  
- End with new or important information  

---

### Rule 6 — Use clear sentence structure
- Subject → Verb → Object  
- Avoid long interruptions  

---

### Rule 7 — Add reasoning signals
Make thinking visible using:
- because  
- this means  
- this shows  

---

### Rule 8 — Avoid AI-like patterns

Do NOT:
- use repetitive transitions (Furthermore, Moreover…)  
- create perfectly parallel sentences  
- over-smooth the text  

Allow:
- variation in sentence length  
- natural rhythm  

---

### Rule 9 — Controlled human tone

Allowed:
- This is unclear  
- This suggests...  
- In practice...  

Avoid:
- Honestly...  
- The weird thing is...  

---

### Rule 10 — Use correct academic tense

- Present → general knowledge  
- Past → experiments and results  

---

## 5. Output Constraints

The agent must:
- Keep original meaning 100%  
- Keep structure close to original  
- Only improve clarity and flow  
- Avoid adding new claims  

---

## 6. Editing Process

### Step 1 — Preserve intent  
Understand what the author is trying to say  

### Step 2 — Fix clarity  
- grammar  
- sentence completeness  

### Step 3 — Simplify language  
- remove complex or unnecessary words  

### Step 4 — Improve structure  
- split long sentences  
- reorder for OLD → NEW  

### Step 5 — Add reasoning (if missing)  
- clarify cause-effect  

### Step 6 — Light polish only  
- stop before over-smoothing  

---

## 7. Example Transformation

### Input
> the system is using jwks so no need shared secret but not sure if auth0_secret still needed

### Output
> The system uses JWKS for token verification, so it does not require a shared secret. It is unclear whether AUTH0_SECRET is still needed in this setup.

---

## 7b. Naturalness Check

After applying Rules 1–7, check for over-smoothness:

- **Vary sentence rhythm** — mix short direct statements with longer analytical ones. Avoid sequences of same-length sentences.
- **Add reasoning connectors** — use "because", "this means", "this shows", "in practice", "as a result" to make the logic explicit rather than implied. Do not repeat the same connector more than once per section — vary them.
- **Reduce overly perfect flow** — break some compound sentences into two. Allow a short blunt sentence after a complex one. Academic writing that is too polished reads as AI-generated.
- **Signal the core contribution early** — do not save the research question for the final paragraph only. Plant a light hint in an earlier paragraph (e.g., "this raises a deeper question") so the reader is prepared before the explicit gap statement. For key concepts like the CAUTION mode, seed them by the second or third section with a single sentence: "This suggests the need for an intermediate operational mode — one where AI participation is allowed but within a restricted scope." Do not explain fully yet. Just plant it.

**Avoid repeated structural patterns across paragraphs:**
- If you use "X governs A without governing B" once, do not reuse the same frame. Vary with: "but they do not constrain…", "yet the range of outputs remains unchanged", or restructure entirely.
- Watch for any phrase template used more than once across a section — it creates a detectable pattern.

**Keep key definitions sharp and reusable:**
- When introducing a term that will recur (e.g., "Level 1 governance"), define it in a clean standalone clause: "Level 1 governance controls whether AI participates in decision-making." Avoid embedding definitions inside longer sentences where they get lost.

**Split dense sentences that carry two distinct claims:**
- If a sentence states both a method and its limitation (e.g., "reduces overhead by 25–71%, but the shield still operates as binary"), split them. Each claim deserves its own sentence so the reader absorbs both.

The goal is writing that is clear and well-structured but still sounds like a human author thinking through an argument.

---

## 8. Anti-Pattern (Must Avoid)

❌
> The system leverages JWKS-based authentication mechanisms to facilitate secure token validation without necessitating the use of a shared secret.

---

## 9. Optional Mode (Strict Academic)

If enabled:
- enforce slightly more formal tone  
- remove conversational phrasing  
- keep clarity-first style  

---

## 10. Reusable Prompt

Refine the text using human-centered scientific writing.

Keep the original meaning and tone. Do not rewrite in a generic AI style.

Apply:
- one idea per sentence  
- simple and precise words  
- remove unnecessary words  
- clear subject–verb–object structure  
- logical flow (old → new)  
- light reasoning (because, this shows)  

Avoid:
- overly formal or robotic phrasing  
- repetitive transitions  
- over-smoothing  

Act as an editor, not a writer.

---

## 11. PhD Literature Review Voice

These rules apply to literature review chapters and gap analysis writing. They prevent the argument from reading as "engineered to fit a conclusion" and instead make it read as "discovered from the evidence."

### Rule 11 — Observational voice, not imposed argument

The argument must read as discovered from the literature, not constructed to fit a predetermined conclusion. Vary phrasing to avoid repetitive gap-assertion patterns.

❌ Imposed (repeated pattern):
> No system implements…
> No architecture defines…
> No method provides…

✅ Observational (varied):
> Across the reviewed studies, no system was found to implement…
> No architecture identified in this review defines…
> The reviewed literature does not provide evidence of…

Do not use the same gap-assertion frame ("No system... No architecture... No method...") more than twice in succession. Vary with:
- "Across the reviewed studies, we did not find evidence that…"
- "The literature examined here does not contain…"
- "This pattern was not observed in any of the reviewed systems."

### Rule 12 — Qualify universal claims

Absolute claims ("none", "no system", "universal", "every method") are vulnerable to a single counter-example. Qualify with review scope to keep strength while reducing attack surface.

❌ "No system implements…"
✅ "No system identified in this review implements…"

❌ "Universal across all domains"
✅ "Consistently observed across the reviewed studies"

❌ "Every method uses binary governance"
✅ "Every method examined in this review uses binary governance"

The claim stays strong. The scope is explicit. One counter-example outside the review does not invalidate it.

### Rule 13 — Bridge sections with overlap sentences

Sections must not feel like perfectly separated boxes. Add bridge sentences at section boundaries that connect the outgoing topic to the incoming one. Show how ideas overlap.

❌ Hard cut:
> [End of 2.2]: "Level 1 is addressed. Level 2 is not."
> [Start of 2.3]: "A parallel body of literature addresses…"

✅ Bridged:
> [End of 2.2]: "While these mechanisms determine whether AI acts, they do not address how decision authority is distributed once AI participation is allowed."
> [Start of 2.3]: "A parallel body of literature addresses…"

This creates argumentative flow rather than a sequence of independent reviews.

### Rule 14 — Push critical tension through practical consequence

Do not just catalogue what exists and what is missing. Show why existing approaches are insufficient *in practice*, using empirical evidence already available in the review.

❌ Flat gap:
> "This is a limitation."

✅ With practical consequence:
> "This is not only a conceptual limitation. In practice, it creates conditions where users receive full-scope recommendations precisely when reliability is lowest."

Use real data (83.3% human intervention failure, fisheries income drops, low digital literacy) to add weight to the argument. The gap is not abstract — it has measurable consequences.

### Rule 15 — Anchor the argument early

Add an anchor sentence near the beginning of a chapter that tells the reader where the argument is heading. Examiners read looking for "what is this student building toward?" — answer that question early.

Example (after 2.1 opening):
> "This chapter examines how existing systems control AI behaviour under risk, and shows that current approaches address participation and output validation separately but do not unify them under environmental state."

The anchor does not state the gap. It frames the question so the reader knows what to watch for.

### Rule 16 — Controlled uncertainty

Occasionally express genuine interpretive uncertainty. Pure assertion throughout an entire chapter reads as constructed. Small hedges make the argument sound like a researcher thinking, not a system generating.

Allowed:
- "This appears to be…"
- "The evidence suggests, though does not conclusively demonstrate, that…"
- "It is difficult to determine from the available evidence whether…"
- "One possible interpretation is…"

Use sparingly — once or twice per chapter, not per section. Too much hedging weakens the argument. The goal is a human reasoning voice, not systematic doubt.

---

## 12. PhD Literature Review Checklist

Before finalising a literature review chapter, verify:

- [ ] Core concept (e.g., CAUTION mode) is seeded lightly by section 2 or 3
- [ ] Anchor sentence appears within the first section
- [ ] No gap-assertion pattern repeats more than twice consecutively
- [ ] Universal claims are qualified with review scope
- [ ] At least two bridge sentences connect adjacent sections
- [ ] At least one practical-consequence statement uses empirical data
- [ ] At least one sentence expresses genuine interpretive uncertainty
- [ ] Section transitions show conceptual overlap, not hard cuts
- [ ] Argument reads as discovered from evidence, not imposed on it