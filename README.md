# ABI AI CoP — Shared Prompt Library for Bioinformatics

A community-authored, citable collection of tested prompts for LLM-assisted
bioinformatics, built by the **ABI Community of Practice on AI for Bioinformatics**.

**Status:** v0.1 in progress · target release December 2026

| Entry | Domain | State |
|---|---|---|
| [0001](prompts/0001-nextflow-failing-process-debug.md) Nextflow process debugging | Coding & pipelines | **Tested** — 5 variants x 2 models, 3 failure modes confirmed at runtime |
| [0002](prompts/0002-debug-pandas-keyerror.md) pandas KeyError debugging | Coding & pipelines | **Tested** — 3 variants × 2 models, reproducible fixture, 3 failure modes |
| [0003](prompts/0003-literature-synthesis-table.md) Literature synthesis | Literature & writing | *Untested draft — Owner :Yaa Adutwumwaa Obeng* |
| [0004](prompts/0004-plasmodium-variant-interpretation.md) *P. falciparum* variant interpretation | Genomics & annotation | *Untested draft — owner needed* |

The entries are marked tested only after they have been run and the results recorded.

---

## Specificity of the library


1. **Anchored in African biological data.** Pathogen genomics, crop genomics,
   populations underrepresented in reference panels, and workflows written for
   constrained compute. 

2. **Failure modes are the most important content.** Every entry records where the model
   hallucinated, what it silently assumed, and how that was detected.    
   Entry 0001 has two: a Nextflow directive that appears not to exist, and a fix
   that makes a pipeline report success on data that was never there.

3. **Versioned and re-tested.** Every entry is stamped with model, version, and
   date. The library is re-validated annually, so behavioural drift becomes
   longitudinal data.

## Contributing takes about twenty minutes

You need a laptop and access to any LLM. No compute cluster, no funding, no
prior AI research experience.

1. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) and the reference entry,
   [`prompts/0001`](prompts/0001-nextflow-failing-process-debug.md).
2. Copy [`PROMPT_TEMPLATE.md`](PROMPT_TEMPLATE.md), or open a
   [new prompt issue](../../issues/new?template=new_prompt.yml) if you prefer a form.
3. Fill every field, including **Failure modes observed**.
4. Submit. Two peers will score it with [`SCORING_SHEET.md`](SCORING_SHEET.md).

Extending an existing entry by adding a variant, or running one on a different model, counts as much as a new entry.

The contributors are named in `CONTRIBUTORS.md` and in the Zenodo record.
The authorship on the resource paper follows [`AUTHORSHIP_CRITERIA.md`](AUTHORSHIP_CRITERIA.md).

## Structuration of an entry

Each entry consists in one **task**, several **prompt variants** for it, tested 
across **more than one model**. Holding the task constant and varying the prompt 
isolates the effect of the prompt rather than the effect of the problem. This 
design comes from Saifeldeen Elshahawy's original prompt library, on which this 
repository is built.

## Structure

```
prompts/           one file per entry, NNNN-short-title.md
PROMPT_TEMPLATE.md the entry template 
SCORING_SHEET.md   the five-criterion review rubric
CONTRIBUTING.md    how to submit and how review works
AUTHORSHIP_CRITERIA.md
CONTRIBUTORS.md    running list, updated after every session
CITATION.cff
```

## Domains

| Domain | Lead | Working session |
|---|---|---|
| Literature & writing | Yaa Adutwumwaa Obeng | October 2026 |
| Coding & pipelines | Saifeldeen Elshahawy | November 2026 |
| Genomics & annotation | Not yet confirmed | December 2026 |

## Licence and citation

Prompts and documentation: **CC BY 4.0**. Cite via `CITATION.cff` or the Zenodo DOI.

## Responsible use

Every entry is a starting point requiring human validation. The outputs may contain
fabricated references, incorrect biological claims, or code that fails silently.
Do not paste sensitive or identifiable data into third-party models. Please see the
data-sovereignty guidance in `CONTRIBUTING.md`. Always declare AI use in the
resulting publications.
