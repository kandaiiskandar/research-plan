# Supervisory Comments — Revised Discussion Brief

**On:** "PhD Research Direction — Supervisor Discussion Brief", 17 November 2026 (revision) · **Written:** 17 November 2026

**What this is.** Comments I would make reviewing this as your supervisor. **Not Prof. Rayner Alfred's views** — do not represent them as his. A rehearsal, so the real meeting is not the first time you hear these questions.

---

## 1. The revision is much better

One page instead of fourteen. Findings before limitations. The identity volunteered in the second paragraph rather than confessed in section six. Decisions reopened for supervision rather than announced. And in §3 you now propose the auditing procedure as the contribution, with the honest rider that you have not checked whether it is novel.

That is the right shape. Three substantive problems remain, and the first is the one I raised most strongly last time and you have not acted on.

---

## 2. You left out the most important finding

§2 still reads: *"Wave conditions accounted for 97.6% of CAUTION activations… This result raises an important question: whether all specified components make a meaningful contribution."*

That is the weak form, and an examiner will go straight through it:

> *Is wave dominant because wave matters most, or because of where you put your thresholds?*

Your own data answers this. The wave CAUTION onset is **1.0 m** against a site p90 of roughly **1.12 m** — the threshold sits **inside** the operating distribution, so it is crossed regularly. The wind CAUTION onset is **21.6 kn** against a maximum observed wind of **21.80 kn in 43,848 hours** — the threshold sits essentially **at the top of the observed range**, so it is almost never crossed. Rainfall behaves the same way.

**So the finding is not about which environmental factor is dangerous. It is about threshold placement relative to the local distribution.** Write it as:

> A component's effective contribution to intermediate-state classification is determined not by its physical importance but by where its threshold falls within the local distribution of that variable. At this site one threshold falls inside the operating distribution and three fall at or beyond its edge, so a specified five-component classifier behaves as a single-component classifier in practice. A specification can therefore be empirically over-specified relative to its deployment environment — and this is detectable before deployment.

**This is not a presentational preference. It is now load-bearing for §3.** Your procedure lists *"the effective contribution of individual classifier components"* as something it assesses. Without the threshold-placement insight the procedure can detect *that* a component contributes nothing but cannot say *why*, and "why" is the part that tells a practitioner whether to drop the component or move the threshold. **As currently specified your procedure is incomplete at exactly the point where it would be most useful.** Add the distributional-position diagnostic and the procedure becomes something a reader could act on.

---

## 3. A structural trap you have walked into

Read your §3 and your §4 together. §3 proposes the auditing procedure as the computer science contribution. §4 proposes retaining RQ1–RQ3 unchanged.

Now read frozen RQ2: *"…how frequently does the intermediate safety state produce a stricter admissible recommendation set than a participation-only gate, and how sensitive is that frequency to defensible environmental-threshold and data configurations?"*

**RQ2 asks for the results of the audit. It does not ask for the audit.** So if the procedure is your contribution, your contribution answers no research question — which is precisely the defect that closed Path A, reappearing in a new place. An examiner who notices will ask which RQ the methodology answers, and there is no good answer.

**Three ways out. I would take the third.**

| | Option | Assessment |
|---|---|---|
| **(a)** | Treat the procedure as **methodology**, in the methods chapter, claiming no contribution for it | Safe, reopens nothing, and wastes your best generalisable material |
| **(b)** | **Revise RQ2** to encompass the procedure | Honest, but reopens a set you froze deliberately, and invites the question of what else is unsettled |
| **(c)** | **Claim the procedure in the journal paper; keep the thesis on RQ1–RQ3 with the procedure as methodology** | **Recommended.** Journal papers are not bound by your RQ set. The paper carries the methodological claim and the negative finding; the thesis carries the empirical answers with the procedure as method. You get both without touching the freeze, and the paper becomes the citable methodological artefact |

If you take (c), say so explicitly in the brief. A supervisor should not have to infer that the paper and the thesis are making different claims.

---

## 4. The novelty check you have correctly flagged — where to look

You write that you *"have not yet established that this combination is methodologically novel compared with existing robustness and model-auditing methods."* That is the right admission, and it is now the critical path: you cannot propose the procedure as the contribution while not knowing whether it exists. **This is a bounded literature task, not a research project.** Four places to look, in order of threat:

**1. Specification curve analysis and multiverse analysis.** This is your closest precedent and it is probably the one that decides the question. Enumerating every defensible analytic specification and reporting the distribution of results across them is an established method — Simonsohn and colleagues on specification curves, Steegen and colleagues on multiverse analysis — developed in psychology and economics in response to researcher degrees of freedom. **Your 56-configuration envelope is a specification curve.** If you claim the procedure as novel without addressing this, a reviewer who knows the reproducibility literature will say so in the first round.

**2. Global sensitivity analysis.** Variance-based attribution over model parameters is a mature field. Your component attribution is close to a first-order sensitivity analysis, and someone will ask why you did not use Sobol indices.

**3. Assurance cases and safety-case evidence auditing.** Tracking the provenance of each claim's supporting evidence is the core of this tradition. Your sourced / superseded / researcher-defined stratification will look familiar to anyone in certification.

**4. Ablation studies.** The obvious ML comparator. Weakest threat, because ablation removes components whereas you vary thresholds, but expect the question.

**My honest prior, and you should hear it before you spend a month on this.** Steps 1–4 will probably establish that each element of your procedure exists somewhere. What may survive is the *combination applied to a deterministic governance specification*: provenance stratification of thresholds, plus a rule that no point estimate may be reported without its envelope, plus — and this is the part I have not seen elsewhere — **the explicit separation of mathematical consequences of the policy design from empirical findings.** That last item is the one genuinely unusual thing in your procedure. You discovered your headline was definitional because you went looking; most specification-curve work has no such step, because in a statistical model there is no governance policy whose design can make a result definitional.

**So position the novelty there if it survives**, and nowhere else. And be prepared to find that it does not, in which case §3's procedure becomes methodology under option (a) and the thesis rests on the empirical findings — which, with §2 fixed, is still a thesis.

---

## 5. Direct answers to your five questions

**Q1 — Is a governance-auditing procedure a suitable CS direction?** **Yes, conditionally**, and you have named the condition yourself. The suitability turns entirely on §4. Do that check before you build the framing on it.

**Q2 — Sufficient empirical depth, or add something?** **The depth is adequate. Do not add experiments.** What is missing is not evidence, it is two things: the threshold-placement finding in §2, and the positioning in §3–§4. You have more evidence than you are currently claiming.

**Q3 — Retain or revise RQ1–RQ3?** **Revise one thing only: demote RQ1.** By your own earlier account it is answered by construction and proof of established mechanisms. Keep its substance — four boundaries sourced, three load-bearing choices researcher-defined — as a provenance audit in the methods chapter, where it strengthens RQ2. Leave RQ2 and RQ3 exactly as frozen. If you take option (c) in §3, nothing else needs reopening.

**Q4 — Evaluation methodology, empirical study, or both?** **Both, but hierarchically, and the hierarchy matters more than the choice.** The methodology is the claim. The fisheries evaluation is the demonstration. The negative finding — that the specified multi-component structure is inert at its own site — is the result that gives the methodology its point, because it shows the audit finds things worth finding. Positioned as "both" without that ordering, you get a paper with two half-contributions and reviewers who cannot tell which one they are assessing.

**Q5 — What comparison would I require before approving?** Three things, and only the first is substantial:

1. **The §4 check, written up as one page**: for each of the four literatures, what it does, what your procedure does that it does not, and your honest verdict. **I will not approve the methodological framing without this.**
2. **Two or three comparator empirical papers** with a one-page table of what each measured against what you measured. I asked for this before and it is still the single most useful thing you can produce.
3. **The reframed §2 finding** with the distributional evidence beside it.

---

## 6. Smaller points

- **§2, data configuration: put the numbers back.** "Influenced by both wave-model and record-length effects" loses the interesting part. The two effects are **+1.97 and −0.64 points, acting in opposite directions and partially cancelling** — that is why resolution alone cannot explain the difference, and it is one clause.
- **§2, activation: add the envelope to the same sentence as the 5.81%.** Your own lock requires that the headline never appear without it. In a one-page brief that discipline matters more, not less.
- **The four documentation defects have vanished from the brief.** Fine for a one-pager — but confirm they are still tracked, particularly the **−1.4 versus −1.2 gradient**. A figure that does not reproduce from your own published endpoints, sitting in the document you call authoritative, is the kind of thing that costs an examiner's confidence in material that is otherwise sound.
- **§3's last line is doing you a disservice.** *"We have not yet established that this combination is methodologically novel"* is honest, and it is also the first thing a skimming reader will remember. Put it as a question in §5 instead: *"What comparison would you require before I position this as a methodological contribution?"* Same honesty, better placement.

---

## 7. Position

**Path B approved in principle.** Revise §2 as in §2 above, adopt option (c) in §3, and bring me the §4 check and the comparator table. I will give you a view on doctoral sufficiency then — not before, because any answer now would be a guess you would hold me to.

One thing worth saying plainly. Between the two versions of this brief you cut two-thirds of the length, moved the uncomfortable mathematical fact to the front, and reopened a decision you had closed. Those are three difficult edits and most candidates make none of them. The one piece of advice you did not take is the one that would most strengthen your best result — so take it now, and we can have a much shorter meeting.
