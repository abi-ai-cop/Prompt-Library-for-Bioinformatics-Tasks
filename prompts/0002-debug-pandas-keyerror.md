# 0002 — Debug a pandas KeyError in a gene counts pipeline

## Metadata

| Field | Value |
|---|---|
| **ID** | 0002 |
| **Domain** | Coding & pipelines |
| **Organism or data type** | Any; gene-level count matrix (CSV) |
| **Author** | Aïda Ouangraoua, Université de Sherbrooke, ORCID: 0000-0002-2040-4948 |
| **Date tested** | {{2026-08-31}} |
| **Models tested** | GPT-5.6 Luna, Gemini 2.5 Flash |
| **Licence** | CC BY 4.0 |

## Objective

Help a beginner Python user diagnose and fix a `KeyError` raised when grouping a
counts table, and learn a repeatable way to inspect column names.

## Biological and computational context

It assumes a gene-level count matrix exported from featureCounts, HTSeq, or similar,
read into pandas. The user is a beginner. The answer must explain.
Common real cause: the exported file has a comment header line, or the column is
named `Geneid` rather than `gene_id`.

## Inputs required

- The failing code block
- The error message, verbatim

## The task

The script below fails against `fixtures/0002/counts.csv`, a realistic featureCounts
export. Three faults are layered in it: a `#` comment line parsed as the header,
a gene column named `Geneid` instead of `gene_id`, and no `count` column at all
(counts are per-sample). A fix addressing only the first two still raises a KeyError.

```python
import pandas as pd

df = pd.read_csv("counts.csv")
counts = df.groupby("gene_id")["count"].sum()
print(counts.head())
```

Error: `KeyError: 'gene_id'`

This entry measures whether the model finds all three faults, and whether
it admits it is guessing about a file it cannot see.

## Prompt variants

### Variant A: Beginner, explanation requested

```text
I am a beginner Python user. I am getting a KeyError: '{{COLUMN_NAME}}' when
running the Python code below.

{{PASTE CODE HERE}}

Please:
1. Explain the cause of the error.
2. Identify the problematic line.
3. Suggest a corrected version of the code.
4. Recommend debugging steps to verify the column names in the dataframe.

Assume I am new to pandas. Explain each step before giving code. Do not suggest
switching to a different library.
```

### Variant B: Expert in the domain, uncertainty required

```text
Act as an experienced bioinformatician debugging a colleague's analysis script.

The script below fails with KeyError: '{{COLUMN_NAME}}'. The input file is a gene
count matrix; I have not shown you its contents.

{{PASTE CODE HERE}}

Please:
1. List every assumption this code makes about the input file's structure.
2. For each assumption, state how it could be wrong for a real count matrix
   exported from a standard quantification tool.
3. Give the commands you would run to inspect the file before changing anything.
4. Only then propose a corrected version.

Do not guess the file's column names. Where you need information you do not have,
say so explicitly and tell me what to check.
```

### Variant C: Minimal fix only

```text
Fix the error in this Python script with the smallest possible code modification
and explain the change briefly.

{{PASTE CODE HERE}}
```

## Expected output format

Variant A: four numbered sections matching the four requests, corrected code in a
fenced block, debugging steps as runnable commands. Variant B: an assumptions list
before any code. Variant C: one code block and a sentence.

## Cross-model comparison

Each variant run in a separate, fresh chat on each model.

| Variant | Model | Comment line | `Geneid` | No `count` column | Asked to see the file? | Proposed code runs? |
|---|---|---|---|---|---|---|
| A | ChatGPT GPT-5.6 Luna | No | No | No | No | **No** |
| A | Gemini 2.5 Flash | No | No | No | No | **No** |
| B | ChatGPT GPT-5.6 Luna | Yes | Yes | Yes | Yes | Withheld code pending inspection |
| B | Gemini 2.5 Flash | Yes | Yes | Yes | Yes | **Yes — verified against the fixture** |
| C | ChatGPT GPT-5.6 Luna, run 1 | No | No | No | No | No-op |
| C | ChatGPT GPT-5.6 Luna, run 2 | No | No | No | No | Still fails |
| C | Gemini 2.5 Flash | No | No | No | Yes | No change proposed |

### Response extracts

**Variant A — both models.** Both attributed the error to whitespace or
capitalisation and recommended inspecting `df.columns`. Both then supplied a
"corrected" script whose grouping line is unchanged from the original:

```python
df.columns = df.columns.str.strip()
counts = df.groupby("gene_id")["count"].sum()
```

This fails identically to the input. Neither model mentioned comment lines,
`Geneid`, or the absence of a `count` column.

**Variant B — ChatGPT.** Enumerated ten assumptions, including that a file may
"contain a comment line beginning with #", that real matrices use names such as
`Geneid`, and that standard outputs often have one count column per sample rather
than a single `count`. It predicted the next failure explicitly: that fixing
`gene_id` would produce `KeyError: 'count'`. It refused to give final code and
requested `df.columns.tolist()`.

**Variant B — Gemini.** Reached the same three conclusions and was more
specific. It tabulated the column conventions of four tools — HTSeq, featureCounts
(`Geneid`, with `Chr, Start, End, Strand, Length` alongside), Salmon, Kallisto —
listed "no metadata/comment lines" as an explicit assumption, and gave
`# Program:featureCounts...` as the example comment line. That is an accurate
description of this entry's fixture, produced without seeing it.

It then supplied two conditional templates. Scenario A was executed against the
fixture and **runs correctly**, returning the right per-gene totals:

```python
df = pd.read_csv("counts.csv", sep=",", comment="#", index_col=0)
annotation_cols = ["Chr", "Start", "End", "Strand", "Length"]
count_matrix = df.drop(columns=[c for c in annotation_cols if c in df.columns])
count_matrix = count_matrix[~count_matrix.index.str.startswith("__")]
counts_per_gene = count_matrix.sum(axis=1)
```

It also filtered HTSeq-style `__no_feature` summary rows — a fault the fixture does
not contain, so the guard is defensive rather than lucky.

**Variant C — ChatGPT** Correctly stated that the CSV lacks a column of that name, 
and added `print(df.columns)` before the grouping line. The grouping line itself is
unchanged, so the script still fails, but nothing was fabricated. 

**Variant C — Gemini.** Suggested the cause might be pandas not being installed or 
the file being absent, and asked for the traceback.

### Results

**The prompt variant determined the outcome.** Two model
families  gave the same result on each variant: A failed on
both, B succeeded on both, C failed on both. So, for this task, prompt strategy
dominated model choice.

The mechanism is visible in the responses. Variant B withheld the file and
demanded an assumptions list, and both models then reasoned from what a real
quantification output looks like, which includes `Geneid`, the `#` comment line,
and the per-sample columns. Variant A invited explanation without
requiring uncertainty, and both models filled the gap with plausible generic
causes. Variant C's minimal-fix framing did not allow any reason at all.

The two Variant C failures are not equivalent. Gemini declined and asked for
evidence; ChatGPT presented a no-op as a repair. 

Under Variant B the models also diverged, though both diagnosed correctly.
ChatGPT withheld code entirely until it could see `df.columns.tolist()`. Gemini
supplied conditional templates, one of which happened to be executable on this
fixture. Both behaviours could be good depending of the user.: withholding is 
the more rigorous reading of "do not guess", while conditional templates are 
more useful to someone who then has to do the work. This is worth watching
across other entries.

Note also that Gemini reached `Geneid` and the `#` comment line under Variant B
but not under Variant A. So, the prompt determined whether it was used.

**Limit in interpretation:** Variant A's failure is partly forgivable, in that
both models correctly told the user to inspect the columns. The problem is that
each then supplied a "corrected version" that was not corrected. Offering unusable
code alongside sound advice is worse than offering the advice alone, because the
code is what a beginner will copy.

## Known limitations

One fixture, one language, two hosted models, one run each. Single runs cannot
distinguish a strategy effect from sampling variance. The variant effect here is
large and consistent across two models from different families, but repeat runs 
would strengthen it. No open-weight or locally deployed model has been tested.

Withholding the file is deliberate and is what the entry measures. In practice,
supplying `head -n 5` of the CSV would likely resolve all three faults under any
variant.

## Failure modes observed

- *Presented a "corrected version" that is functionally identical to the failing
  code. Both models, under Variant A, added whitespace-stripping and print
  statements while leaving `groupby("gene_id")["count"]` intact — GPT-5.6 Luna 
  and Gemini 2.5 Flash — 2026-08-31 — detected by running the proposed
  script, which raised the original KeyError.*
- *Asserted the absence of an error that had been reported in the prompt. Under
  Variant C, Gemini stated the script contained no syntax or logical errors and
  attributed the failure to a missing library or missing file — Gemini 2.5 Flash
  — 2026-08-31 — detected on reading the response.*
- *Converged on the same wrong hypothesis across models. Under Variant A, both
  models independently attributed the error to whitespace or capitalisation, and
  neither raised comment lines, `Geneid`, or per-sample count columns — both
  models — 2026-08-31 — detected by comparing against the known faults in
  `fixtures/0002`.*

## Validation performed

Each model's proposed code was checked against the three known faults in
the fixture and run where the model supplied final code. Variant A's proposed code
was executed and reproduced the original `KeyError: 'gene_id'`. Variant C
(ChatGPT) output diffed against the input and found identical. Gemini's Variant B
Scenario A template was executed against the fixture and returned correct per-gene
totals. This was verified by hand against the source rows.


**Outstanding:** not applicable.

## Related entries

None yet.
