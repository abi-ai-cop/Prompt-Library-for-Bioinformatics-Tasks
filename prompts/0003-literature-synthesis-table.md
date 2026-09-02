# 0003 — Synthesise a set of papers into a comparison table and background section

> ** UNTESTED DRAFT.** This entry has not been run against any model. The prompt text,
> expected outputs, limitations, and failure modes are just proposals.
> Do not cite or rely on it until it has been tested and the placeholders filled.
> ** OWNER: needed.** Reserved for the October working session (Literature & writing).

## Metadata

| Field | Value |
|---|---|
| **ID** | 0003 |
| **Domain** | Literature & writing |
| **Organism or data type** | Not applicable; PDF full texts |
| **Author** | {{NAME, AFFILIATION, ORCID}} |
| **Date tested** | {{YYYY-MM-DD}} |
| **Model(s) tested** | {{MODEL + VERSION}} |
| **Licence** | CC BY 4.0 |

## Objective

Turn a small set of methods papers into a structured comparison table plus a
drafted background paragraph, for a student beginning a literature review.

## Biological and computational context

It assumes 3–8 papers are attached as full-text PDFs, on a shared methodological topic.
It is important to attach the PDF files. Without them, the model summarises from memory and
fabricates specifics. The output is a **draft to verify**.

## The task

To be completed

## Inputs required

- 3–8 full-text PDFs
- The user's topic and level

## Prompt variants

Only one variant. To be completed.

```text
I am a {{LEVEL, e.g. master's}} student studying {{TOPIC}}.

Using the attached papers only — do not use knowledge from outside them:
1. Summarize each paper in 5–7 bullet points.
2. Extract the datasets, methods, software tools, and key findings.
3. Create a comparison table showing objectives, datasets, methods, performance
   metrics, and conclusions.
4. Draft a 250-word background section suitable for the introduction of a
   literature review.
5. Cite all information using the original paper references.
6. Output the results in clear academic language suitable for graduate students.

If a paper does not report one of the requested items, write "not reported"
rather than inferring it.
```

## Expected output format

Per-paper bullets, one comparison table, one 250-word paragraph with in-text
citations traceable to the attached PDFs.

## Cross-model comparison

To be completed.

### Response extract

To be completed.

### Results

To be completed.

## Known limitations

To be completed.

Degrades beyond roughly eight papers. Performance metrics are the field most often
mis-extracted, because papers report them inconsistently across tables and text.

## Failure modes observed

To be completed.

## Validation performed

To be completed.

Every table cell and every citation checked against the source PDF. Any uncited
claim in the background paragraph is treated as unverified.

## Related entries

None yet.
