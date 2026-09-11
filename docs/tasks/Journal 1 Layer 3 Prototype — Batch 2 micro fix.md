# Journal 1 Layer 3 Prototype — Batch 2

## SINGLE RESIDUE FIX

Independent final review found exactly one remaining current-status residue.

Do NOT perform another broad audit.
Do NOT modify scientific evidence.
Do NOT modify candidate rules.
Do NOT modify Appendix C.
Do NOT resolve OPEN-L3-3.
Do NOT begin Batch 3.

Modify only:

```text
data/journal1-layer3-prototype/closure-batch2.json
```

In:

```text
open_items_status.OPEN-L3-1_concrete_rule_content
```

the current value still states:

```text
PARTIALLY RESOLVED in Batch 2 —
Go CONDITIONALLY SUPPORTED;
Delay SUPPORTED/CONDITIONALLY SUPPORTED;
DepartureTime deferred (OPEN-L3-1C);
Duration deferred (OPEN-L3-1D)
```

This is stale.

Replace it with wording equivalent to:

```text
PARTIALLY RESOLVED in Batch 2 —
Go CONDITIONALLY SUPPORTED;
Delay candidates CONDITIONALLY SUPPORTED;
DepartureTime deferred (OPEN-L3-1C);
Duration deferred (OPEN-L3-1D)
```

The reason is that all current Delay candidates, including R-CAUTION-001, are now classified as:

```text
CONDITIONALLY SUPPORTED
```

R-CAUTION-001 specifically has:

```text
P_ENV = Level A
P_ADV = Level C inferred
overall rule status = CONDITIONALLY SUPPORTED
```

Do not reintroduce `SUPPORTED` as the overall status.

After the edit:

1. Parse `closure-batch2.json` using `json.load`.
2. Confirm no current-status field contains:

```text
Delay SUPPORTED/CONDITIONALLY SUPPORTED
```

3. Historical repair records may retain historical counts such as:

```text
57 PASS / 0 FAIL / 1 OPEN / 58 total
```

when explicitly describing an earlier repair round. Do not rewrite historical provenance merely to match the current 90-check state.

4. Confirm the current semantic summary remains:

```text
89 PASS
0 FAIL
1 OPEN
90 total
```

5. Confirm OPEN-L3-3 remains:

```text
OPEN — BLOCKING
```

6. Confirm Batch 3 remains blocked.

7. Confirm no protected canonical file changed.

Return only:

* JSON parse result
* corrected OPEN-L3-1 current status
* current semantic counts
* OPEN-L3-3 status
* Batch 3 gating status
* protected canonical integrity
* exact Batch 2 status line

The exact Batch 2 status line must remain:

```text
JOURNAL 1 LAYER 3 PROTOTYPE BATCH 2 REMAINS OPEN —
CAUTION ADVISORY SEMANTICS REQUIRE AUTHORITY RESOLUTION
```
