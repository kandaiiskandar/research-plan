# Duplicate-Result Audit

Two "same title, two identities" pairs existed before this repair. **They are not the same kind of thing**, and the audit's main job was to establish that one was a defect and the other was the intended design.

---

## 1. `Theorem 5.1 (Totality of f)` vs `Theorem 6.1 (Totality of f)` — DEFECT, repaired

### Are they the same result?

**Yes.** Determined by comparing the declared statements directly, not by title alone.

| | §5 L457 (before repair) | §6.2 L629 |
|---|---|---|
| Identifier | `Theorem 5.1` | `Theorem 6.1` |
| Title | Totality of f | Totality of f |
| Statement | "For all E in its domain, f(E) is defined and returns exactly one element of {SAFE, CAUTION, UNSAFE}." | "For all E in its domain, f(E) is defined and returns exactly one element of {SAFE, CAUTION, UNSAFE}." |
| Proof | None — "Proof deferred to Section 6.2." | Full proof, terminated `∎` |

**The statements are character-for-character identical**, and §5's own text deferred its proof to §6.2. This is one result declared twice under two theorem numbers, with the proof attached to only one of them.

### Which identity was retained, and why

**`Theorem 6.1` retained as canonical.** Three reasons, in order of weight:

1. **It is where the proof lives.** A theorem identity belongs with its proof; §5's declaration carried none and pointed at §6.2 for it.
2. **§6 is the canonical home of proved theorems**, per the governing editorial decision, and §6.2's heading is literally "Theorem 6.1: Totality of f".
3. **Downstream references already favoured it.** Before the repair, §§3, 4, 9, 10, 11 and 13 referenced `Theorem 6.1`; only §5's own declaration and one line in §7 used `Theorem 5.1`. Retaining 5.1 would have required changing more references, against the instruction to prefer repairing stale references over renumbering valid canonical declarations.

### What happened to the §5 content

**Nothing was deleted.** The statement remains in place, word for word, demoted from a numbered theorem to an unnumbered specification statement:

```diff
- **Theorem 5.1 (Totality of f).** For all E in its domain, f(E) is defined and
+ **Totality of f.** For all E in its domain, f(E) is defined and
  returns exactly one element of {SAFE, CAUTION, UNSAFE}.

- Proof deferred to Section 6.2. Totality follows from exhaustive domain
+ This result is proved canonically as Theorem 6.1 in Section 6.2. Totality follows from exhaustive domain
  coverage of each gᵢ ... and from the fact that max_≻ over a finite totally
  ordered set is always defined and unique.
```

The second edit is the minimal grammatical consequence of the first: "Proof deferred to Section 6.2" no longer had a theorem to attach to, and the forward reference now names the canonical identity explicitly. **The sentence that follows it — the entire mathematical justification — is untouched.**

### Confirmation that scientific content is unchanged

- The statement of totality is unchanged.
- The justification sentence is unchanged.
- The proof in §6.2 is unchanged.
- No equation, quantifier, domain or codomain was altered.
- Verified mechanically: normalising the pre-repair manuscript by exactly the seven authorised substitutions reproduces the post-repair manuscript **byte for byte** (`no_change_beyond_authorised_identifier_edits`).

---

## 2. `Property 5.3 (Safety Dominance Property)` vs `Theorem 6.3 (Safety Dominance Property)` — INTENTIONAL, preserved

### Are they the same result?

They state the same proposition — `AI(E) ⊆ A_AI(f(E))` — but they are **not two declarations of the same formal object.** They occupy different namespaces and play different roles:

- **`Property 5.3`** is a *specification-level* statement: what the architecture is required to satisfy.
- **`Theorem 6.3`** is the *proved* result: that the specified architecture does satisfy it, under assumptions A1–A4.

### Evidence that this is the manuscript's intended pattern

The manuscript establishes the relationship explicitly and consistently:

1. **Properties 5.1 and 5.2 follow the identical pattern.** `Property 5.1 (Participation Constraint)` and `Property 5.2 (Advisory Restriction Constraint)` are stated in §5.5 and then *discharged* in §6 by a corollary whose title is literally "(Properties 5.1 and 5.2)".
2. That corollary's body says: *"Both governance constraints stated in Section 5.5 follow directly"*, then proves each in turn — §6 treats §5's Properties as obligations it discharges.
3. `Property 5.2`'s discharge reads: *"This is precisely Case 2 of Theorem 6.2, with the strict subset confirmed by Corollary 6.2"* — an explicit property → theorem mapping.

So §5 states three properties and §6 proves all three: 5.1 and 5.2 via the corollary, 5.3 as Theorem 6.3. **`Property 5.3` is the third instance of a pattern the manuscript applies uniformly**, not a stray duplicate.

### Decision

**Preserved unchanged.** This is the structure the governing editorial decision asks for — *specification/property in §5 → canonical theorem and proof in §6* — and eliminating `Property 5.3` would have broken the parallel with Properties 5.1 and 5.2 and removed a specification-level statement the architecture section needs.

Had the defect in case 1 been "fixed" by the same rule applied to case 2, the result would have been to delete a correct statement. The distinction is that **`Theorem 5.1` competed for a theorem identity; `Property 5.3` does not.**

### Note on the repair this implies

The anomaly in case 1 was precisely that §5 stated Totality as a *Theorem* while its three sibling statements are *Properties*. The demotion to an unnumbered statement makes §5 uniformly specification-level and §6 uniformly theorem-level. A new `Property 5.4` was explicitly **not** created: it would have appeared *before* Properties 5.1–5.3 in reading order, reproducing the ordering awkwardness already recorded for Definitions 5.10 and 5.11.
