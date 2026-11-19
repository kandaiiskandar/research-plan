# Supervisory Comments on "PhD Research Progress and Proposed Direction (Path B)"

**On:** your document of 17 November 2026 · **Written:** 17 November 2026

**What this is.** These are the comments I would make if I were reviewing your progress document as your supervisor. **They are not Prof. Rayner Alfred's views and must not be represented as his** — he may well take a different line, particularly on scope. Use this as a rehearsal: it is an attempt to ask you the questions a supervisor and an examiner will ask, so that you are not hearing them for the first time in the meeting.

---

## 1. Headline

Your document is honest, well-organised and unusually clear about its own limits. That is to your credit and it is rarer than it should be. I would accept **Path B in principle.**

But I would not sign off on the thesis as currently *framed*, and my reason is not the one you are worried about. You ask whether the empirical contribution is original enough. The sharper risk is different:

> **As written, a computer science examiner will ask what the computer science is.**

Your classifier is a maximum over five threshold functions. Your experiment evaluates it on a weather archive. Your three findings are measurements of one deterministic specification at one site over one five-year record. Framed that way, this reads as applied environmental data analysis with a governance wrapper — and an examiner in a CS faculty will say so.

**The good news is that the material to fix this is already in your results.** You have a *method* and a *transferable finding*, and you are currently reporting both as site-specific numbers. §4 is where I would concentrate your effort.

---

## 2. Direct answers to your five questions

### Question 1 — Is the empirical contribution substantial enough?

**Conditionally yes, and not as currently stated.**

An activation frequency, a sensitivity envelope and a component attribution *at one site* is a case study. Three case-study findings do not make a doctorate in computer science, however carefully measured.

What makes it doctoral is the generalisable layer you have built but not claimed: **a reproducible procedure for auditing a deterministic safety-gating specification against the provenance of its own thresholds.** 78 executions over 56 configurations, with every threshold classified as externally sourced, superseded, or researcher-defined, and the headline result reported as a disclosed envelope rather than a point. That procedure applies to any threshold-based governance gate in any domain. **That is the contribution a CS examiner can evaluate.** The Kota Kinabalu numbers become the demonstration, not the claim.

### Question 2 — Is the analysis sufficiently distinct given that graduated gating is established?

**Yes, but you are defending the wrong perimeter.**

You concede mechanism novelty, which is correct and which I would not reopen. The distinctness is not in the gate; it is in having *measured what the gate does and found that most of its specified structure does nothing at the site it was designed for*. Almost nobody does that to their own architecture. Papers propose gates; they rarely publish the finding that four-fifths of their classifier is inert in deployment conditions.

**But I will not accept "distinct" on your word, and neither will your examiners.** See §5, condition C1: I need to see the two or three papers you expect to be compared against. You cannot ask me whether your contribution is sufficient while naming no comparator.

### Question 3 — Retain RQ1–RQ3, or expand?

**Retain the set. But I want to challenge two things you have treated as settled.**

**First, RQ1 should not be a research question.** By your own account it is *"answered by construction and proof, not measurement"*, and its properties are formalisations of established mechanisms. A research question whose answer is a design property invites the examiner to ask what was researched. Its genuinely interesting content — *four boundaries externally sourced, three load-bearing choices researcher-defined* — is a provenance audit, and that belongs in your methodology chapter where it strengthens RQ2 rather than standing as a question in its own right. **I am not asking you to delete it. I am asking you to stop calling it a research question.** You will tell me the RQ set is frozen. See the next point.

**Second, "the research chain is locked" is an argument you have made to yourself.** The freeze is an internal document of your own authorship. It is excellent discipline and I want it maintained — but it does not bind your examiners, and it must not become a reason to protect a thin thesis. If the contribution turns out to be insufficient, the correct response is to reopen the set under supervision, not to decline the work because a document you wrote says the set is closed. Do not use your own governance against yourself.

### Question 4 — Can the wave-dominance finding be a central result?

**Yes — and this is the most important paragraph in my comments, because the finding you have is sharper than the one you are reporting.**

You report: wave accounts for 97.6% of intermediate-state activations; wind for none. An examiner will ask the obvious question, and you must have the answer ready:

> *Is that because wave matters most, or because of where you put the thresholds?*

Look at your own numbers. Your wave CAUTION onset is 1.0 m, and the site's wave distribution has p90 ≈ 1.12 m — the threshold sits **inside** the distribution, so it is crossed often. Your wind CAUTION onset is 21.6 kn, and the maximum wind observed in 43,848 hours is **21.80 kn** — the threshold sits at the **extreme upper tail**, so it is essentially never crossed. The rainfall boundary behaves similarly.

**So the attribution result is not primarily a statement about which environmental factor is dangerous. It is a statement about where each threshold sits relative to the local distribution of that variable.** If you present it as "wave conditions dominate maritime risk here", you will be corrected in the viva and it will look as though you did not understand your own result. If you present it as the following, you have a finding with reach:

> In a multi-component safety classifier, a component's effective contribution is determined not by its physical importance but by the position of its threshold within the local distribution of that variable. At this site, one component's threshold falls inside the operating distribution and three fall outside it, so the specified five-component structure behaves as a single-component classifier in practice. A specification can therefore be empirically over-specified relative to its deployment environment, and this is detectable before deployment by the procedure in Chapter 4.

That claim transfers to any threshold-gated system anywhere. **It is your strongest result and you are currently burying it as a site observation.** Make it Chapter 5 and put it in the abstract.

### Question 5 — Journal 1 V2 positioning?

**Yes to emphasising sensitivity, robustness and attribution. No to the phrasing you proposed.**

If the paper describes the architecture as "an application of established governance principles", a reviewer's first question is why it needs publishing. A paper needs a claim. Yours should be: *here is a method for auditing a deterministic advisory-governance specification against its own threshold provenance, and here is what it found when applied to a real architecture — including that the architecture is over-specified for its site.*

Lead with the method and the negative finding. The architecture is the object of study, not the contribution. And state the activation identity in the paper's own introduction — see §3.

---

## 3. The three things that would worry me at your viva

**W1 — The identity, if you let the examiner find it.** Δ_L2 is identically P(CAUTION). You have understood this and you plan to explain it. Good — but I want it **volunteered in the first paragraph of your results, in the abstract of the paper, and in your opening viva statement.** The difference between "I discovered my headline comparison is definitional and here is what that means" and "yes, you're right, it is" is the difference between a strong candidate and a damaged one.

Have this answer memorised: *What would have been different if you had used two states instead of three?* The honest answer is **nothing measurable**, because the result is invariant to the content of `A_AI(CAUTION)`. Say it before you are asked.

**W2 — Volume and balance.** You have one frequency, one envelope, one attribution table and one decomposition. By the standards of a CS thesis that is thin on substantive chapters, and three of your four findings are negative or limiting. I do not think negativity is a problem — a thesis of careful negative results is respectable and often more honest than the alternative. But **thinness is a problem**, and the fix is §4, not more experiments.

**W3 — "Computer science" as a category question.** Covered in §1. If the examiners decide this is environmental data analysis, no amount of rigour in the analysis rescues it. The method framing is your defence.

---

## 4. What I would have you do, and it needs no new experiments

In priority order.

| | Task | Why |
|---|---|---|
| **1** | **Reframe the sensitivity machinery as a method, with its own chapter.** Name it. Specify it so somebody else could apply it to a different gate: threshold inventory, provenance stratification (sourced / superseded / researcher-defined), configuration enumeration, envelope reporting, component attribution with definitional zeros separated, and the prohibition on reporting a point without its envelope | This is the generalisable contribution and it is the answer to Question 1 |
| **2** | **Restate the attribution finding as the threshold-placement result** (§2, Q4), with the distributional evidence beside it: wave onset at p90 of the local distribution, wind onset above the observed maximum | Converts a site observation into a transferable claim |
| **3** | **Demote RQ1 to methodology**, keeping the provenance audit as its substance | Removes an RQ that an examiner will read as unanswered-by-measurement |
| **4** | **Add one short chapter section: what this procedure would detect in another architecture.** Not an experiment — a worked argument on one or two published gating designs, showing what the audit would ask of them | Demonstrates reach without new data. This is the cheapest thing on this list and the most persuasive |
| **5** | Fix the four documentation defects you listed | Necessary hygiene. One week, not one month. The −1.4 versus −1.2 gradient is the urgent one: a figure that does not reproduce from your own published endpoints, sitting in the document you call authoritative, is the kind of thing that costs you an examiner's confidence in everything else |

---

## 5. Conditions before I would sign off

**C1 — Bring me the comparators.** Two or three papers, full text, that an examiner would hold up against your thesis, with a one-page table of what each measured and what you measured that they did not. Without this I cannot answer Question 1 and nor can you. **This is the single most useful thing you can do before our next meeting**, and I would rather have it than any of §4.

**C2 — One page on the method's transferability.** Task 4 above, in draft.

**C3 — A reframed contribution statement**, one paragraph, that a CS examiner reads as computer science. If the first sentence is about Sabah, it is wrong. If the first sentence is about auditing a specification, it is right.

**C4 — The viva answer to the identity question, written out.** Three sentences. I want to read them.

---

## 6. Comments on the document itself

You will be writing documents like this for the rest of your career, so these matter.

- **It is too long, and the length hurts you.** Fourteen sections to ask five questions. Your supervisor is busy. Lead with the five questions and your recommendation on one page, then the evidence. A reader who stops after page one should still know what you are asking.
- **You answer before you ask.** Section 10 announces Path B before the reader has been given the material to judge it. Present the evidence, then the recommendation.
- **The self-criticism is calibrated but over-weighted.** Sections 6, 8 and 9 are a sustained account of what you cannot claim. Each statement is correct and I would not remove one. But the cumulative effect reads as a candidate arguing against their own thesis, and a supervisor skimming it may conclude the work is weaker than it is. **Put the three substantive findings before the limitations, not interleaved with them.** Honesty is in the content, not in the ordering.
- **Section 9's NO-GO is presented as closed.** You investigated a methodological extension, found prior-art overlap, and decided against it — three rounds, documented. That is good work and probably the right call. But you have told me a decision rather than asked for one. **Supervisors dislike finding out that a direction was closed without them.** Present it as a recommendation with the evidence attached, and let me disagree if I want to.
- **Section 2 is domain motivation and reads well, but it is doing no work for the contribution.** Shorten it. Nobody disputes that small-scale fishers face incomplete information.

---

## 7. On Path A, briefly

I accept your recommendation against it, and your reasons are sound — I have no quarrel with a judgement built on sample size, data resolution and licensing.

But I want one thing on the record. Your own analysis says the question of whether a real wave forecast has useful skill at short intra-window leads is **untested**. That is an honest statement and it is also a loose thread. If a committee member asks "did you check whether a real forecast would help?", the answer *"no, and we reasoned it probably would not"* is weaker than *"no, and here is the one test that would settle it, which we specify and recommend as future work"*. **Make sure that test is specified in your future-work chapter**, not merely mentioned. Future work that names its own entry criterion reads as controlled scoping. Future work without one reads as an exit.

---

## 8. Overall

You have done something slightly unusual, and I want to say so plainly before the criticism above settles into the only thing you remember from this. You took a plausible architecture, measured it properly, and discovered that its headline comparison was definitional and that most of its structure is inert at its own deployment site. Then you wrote that down instead of hiding it. Many candidates would have published the 5.81% and hoped nobody checked.

**That instinct is the thing that will make you a researcher.** It is also, at the moment, aimed inward rather than outward: you have been auditing yourself more rigorously than you have been positioning your work against the field. §5 C1 is where to redirect it.

**My position:** Path B approved in principle, with the reframing in §4 and the four conditions in §5. I will give you a view on doctoral sufficiency when I have seen the comparators — not before, because any answer I give you now would be a guess, and you would quite reasonably hold me to it.

Bring C1 and C3 to our next meeting. Leave the documentation fixes to the week after; they are not what we need to discuss.
