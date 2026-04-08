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
- **Signal the core contribution early** — do not save the research question for the final paragraph only. Plant a light hint in an earlier paragraph (e.g., "this raises a deeper question") so the reader is prepared before the explicit gap statement.

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