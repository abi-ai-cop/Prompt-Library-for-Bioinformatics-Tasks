# 0004 — Interpret drug-resistance variants from a *Plasmodium falciparum* VCF

> ** UNTESTED DRAFT.** This entry has not been run against any model. The prompt text,
> expected outputs, limitations, and failure modes are just proposals.
> Do not cite or rely on it until it has been tested and the placeholders filled.
> ** OWNER: needed.** Reserved for the December working session (Genomics & annotation).


## Metadata

| Field | Value |
|---|---|
| **ID** | 0004 |
| **Domain** | Genomics & annotation |
| **Organism or data type** | *Plasmodium falciparum*, whole-genome short-read VCF |
| **Author** | {{NAME, AFFILIATION, ORCID}} |
| **Date tested** | {{YYYY-MM-DD}} |
| **Model(s) tested** | {{MODEL + VERSION}} |
| **Licence** | CC BY 4.0 |

## Objective

Given a filtered variant list from clinical *P. falciparum* isolates, produce a
structured interpretation of known drug-resistance markers, with explicit
separation between established markers and speculation.

## Biological and computational context

It assumes variants called against **Pf3D7 v3** and annotated with gene names.
Reference build are important and models will assume one silently.
This entry exists partly as a test case, because resistance marker knowledge is 
the kind of specialised, continent-relevant content where model recall is weak
and confident fabrication is most likely.

## The task

To be completed

## Inputs required

- Variant table: gene, position, ref, alt, amino acid change, allele frequency
- Reference build and annotation source, stated explicitly
- Number of isolates and country of origin

## Prompt variants

Only one variant. To be completed.

```text
Act as a malaria genomic epidemiologist.

Context: I have {{N}} clinical Plasmodium falciparum isolates from {{COUNTRY}},
sequenced with short reads and called against Pf3D7 v3. Below is a filtered
variant table with gene, position, reference and alternate alleles, amino acid
change, and allele frequency.

{{VARIANT_TABLE}}

Task:
1. Identify which variants are established markers of antimalarial drug
   resistance. For each, name the drug or drug class and the resistance
   phenotype.
2. Present these in a table with columns: Gene | Amino acid change | Drug |
   Evidence strength | Primary reference.
3. In "Evidence strength", use only: Established / Associated / Unclear.
   Do not use any other term.
4. Separately list variants you cannot classify, and say what additional
   information would be needed.
5. Do not speculate about clinical treatment decisions.

Constraints: cite only published literature you are confident exists. If you are
unsure a reference is real, write "reference needs verification" instead of
providing one. State explicitly any assumption you make about the reference
build or annotation.
```

## Expected output format

One classification table, one unclassified list, and an explicit assumptions
statement. No treatment recommendations.

## Cross-model comparison

To be completed.

### Response extract

To be completed.

### Results

To be completed.

## Known limitations

To be completed.

Model recall on resistance markers is uneven and skews toward the best-studied
loci. Treat every classification as a hypothesis for manual confirmation against
current WHO and MalariaGEN resources. This prompt supports curation, but does not
replace it.

## Failure modes observed

To be completed.

## Validation performed

To be completed.

{{Cross-check every "Established" call against current WHO guidance and MalariaGEN
resources. Verify every DOI resolves.}}

## Related entries

None yet. Candidate follow-ups: *M. tuberculosis* resistance calling, HIV subtype
assignment, arboviral lineage assignment.
