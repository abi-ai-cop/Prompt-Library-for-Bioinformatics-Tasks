# Prompt entry template

Copy this file into `prompts/`, rename it `NNNN-short-title.md`, and fill every field.
The fields map onto the five evaluation criteria in `SCORING_SHEET.md`.
Do not delete fields — write "not applicable".

**Style:** an entry should have **one task** and **several prompt variants** for it,
tested across **more than one model**. Holding the task constant and varying the
prompt isolates the effect of the prompt rather than the effect of the problem, 
and makes the comparison meaningful. A single-variant, single-model entry, 
is accepted, but scores lower on Robustness.

---

## Metadata

| Field | Value |
|---|---|
| **ID** | `NNNN` (next free number in `prompts/`) |
| **Title** | Task-first. "Debug a failing Nextflow DSL2 process" |
| **Domain** | Literature & writing / Coding & pipelines / Genomics & annotation / Other |
| **Organism or data type** | e.g. *Plasmodium falciparum* WGS; human RNA-seq; not applicable |
| **Author** | Name, affiliation, ORCID |
| **Date tested** | YYYY-MM-DD |
| **Models tested** | Name **and version** for each. "GPT-5.5", "Gemini 3.5 Flash", "Llama 4 70B (local)" |
| **Licence** | CC BY 4.0 |

## Objective

One sentence. State what this accomplishes and for whom?

## Biological and computational context

State what the user is assumed to have: data type, experimental design, reference genome
or annotation build, available compute, software installed. State assumptions
explicitly.

## The task

Define one concrete task, and give the exact input every variant is tested against:
the failing script, the variant table, the paper set. The shared input is what makes
the variants comparable.

```text
{{THE INPUT — code, data selection, or description}}
```

## Inputs required

- Input 1 — format, approximate size
- Input 2 — ...

## Prompt variants

Give each variant a name describing its strategy, not its wording. Mark variable
parts with `{{DOUBLE_BRACES}}`. Two variants is a reasonable minimum; five is a
good entry.

### Variant A — {{strategy, e.g. Minimal instruction}}

```text
{{prompt text}}
```

### Variant B — {{strategy, e.g. Expert researcher}}

```text
{{prompt text}}
```

### Variant C — {{strategy, e.g. Teaching style}}

```text
{{prompt text}}
```

## Expected output format

State what a correct response looks like: structure, length, whether table, code, etc.
If you constrained the format in the prompt, repeat it here.

## Cross-model comparison

Pick each one variant and run it on **two or more models**. Summarise, then give
the evidence.

| Variant | Model + version | Correct? | Approach taken | Notes |
|---|---|---|---|---|
| A | {{model}} | Yes / Partly / No | {{one line}} | |
| A | {{model}} | Yes / Partly / No | {{one line}} | |
| B | {{model}} | Yes / Partly / No | {{one line}} | |
| B | {{model}} | Yes / Partly / No | {{one line}} | |
| C | {{model}} | Yes / Partly / No | {{one line}} | |
| C | {{model}} | Yes / Partly / No | {{one line}} | |

### Response extract

Truncated real responses, enough to judge the comparison. Do not paste pages.

### Results

With two or three sentences, describe where did the models diverge, and does the divergence
matter scientifically? For instance, a fix that makes a pipeline pass while hiding the bug is a
different outcome from a fix that resolves it.

## Known limitations

State where this entry is weak: input sizes it cannot handle, tasks it is not for, model
versions where behaviour differed.

## Failure modes observed

**This is as valuable as the prompts themselves. Do not leave empty.**
Format each as: *observation — model + version — date — how you detected it.*

You must look especially for:

- Fabricated references, tool flags, directives, or accession numbers
- Fixes that suppress a symptom rather than resolve the cause
- Silent assumptions about reference genome, annotation build, or population panel
- Recommendations assuming compute you do not have
- Divergent behaviour across models or across runs

## Validation performed

Explain how you checked the output was correct. For instance, "The code ran" is a 
weaker claim than "the code ran and counts matched featureCounts output". For code, 
state whether you executed it.

## Related entries

Entries that chain with, or supersede, this one.
