# Prompt scoring sheet

Five criteria used by reviewers, by participants during working sessions, and by judges at
the hackathon

Score each criterion 1–5. **Total 25.** An entry needs **≥ 15 overall and ≥ 3 on
Documentation** to be accepted.

---

### 1. Clarity — *is the objective unambiguous?*

| Score | Meaning |
|---|---|
| 1 | Objective must be guessed from the prompt text |
| 3 | Objective is stated, but some instructions are open to interpretation |
| 5 | Objective is explicit, and every instruction is clear |

### 2. Effectiveness — *does it produce accurate, useful, complete responses?*

| Score | Meaning |
|---|---|
| 1 | Output is unusable or wrong |
| 3 | Output is usable after moderate manual correction |
| 5 | Output is correct and complete, with validation evidence provided |

### 3. Reusability — *can another researcher use it with minimal modification?*

| Score | Meaning |
|---|---|
| 1 | Prompt is hard-coded to one dataset, and would need rewriting |
| 3 | prompt is adaptable, but the parts to change are not marked |
| 5 | Variables in prompt marked as placeholders, and adaptation is easy  |

### 4. Robustness — *does it cover multiple variants and models?*

| Score | Meaning |
|---|---|
| 1 | One variant, one model, one input |
| 3 | Several variants on one model, or one variant on ≥ 2 models |
| 5 | Several variants **and** ≥ 2 models, with the divergence analysed |

### 5. Documentation — *are purpose, inputs, outputs, assumptions, limitations clear?*

| Score | Meaning |
|---|---|
| 1 | Some template fields are left blank |
| 3 | All fields are filled, but the failure modes are generic |
| 5 | All fields are filled; with specific failure modes with model version and date |

---

### Note for reviewers

An entry that reports a model failing is not necessarily a weak entry. You should 
score Effectiveness on the prompts, and credit a well-documented failure under
Documentation. The library's value also depends on people being willing to publish 
what did not work.

### Reviewer notes

**Strongest aspect:**

**Must fix before acceptance:**

**Would improve it further:**

---

*Reviewer name / date / total score       /25*

---

### Weakly supervised hypothesis-driven machine-learning pipelines
**Submitter:** Oleg Reva, University of Pretoria (0000-0002-5459-2772)

**Review by** @aidayo — 2026-10-19

| Criterion | /5 |
|---|---|
| Clarity | 5 |
| Effectiveness | 2 |
| Reusability | 5 |
| Robustness | 1 |
| Documentation | 4 |
| **Total** | **17/25** |

**Reviewer notes** 

**Strongest aspect:** the explicit rationale for why Variant E scores lower on
Robustness. The addition of a "Potential AI/prompt failure modes" list after review
is correct.

**Must fix before acceptance:**

1. **No model output is recorded.** The worked example describes your published
   S. enterica pipeline. We are rather expecting what ChatGPT returned. A short 
   extract of the actual ChatGPT response would increase Effectiveness from 2 to 4.
2. **Cross-model comparison** is outstanding. Just adding pne variant on a second model
   would complete the entry.
3. The AI failure modes are listed as *potential* rather than observed. Did they actually
   occur or not?

**Would improve it further:** Comparing what the models propose against your published
pipeline as ground truth would provide an independent standard to measure against.

Review by @saifeldeen-bio — 2026-10-22
Criterion | Score
-- | --
Clarity | 5
Effectiveness | 3
Reusability | 5
Robustness | 2
Documentation | 5
Total | 20/25

#### Reviewer notes

**Strongest aspect:** The prompt is clearly structured and provides a well-defined framework for evaluating how an AI model handles the task. The instructions, worked example, and explicit procedures for handling uncertain predictions and insufficient data provide useful criteria for assessing model behaviour and identifying potential failure modes.

**Must fix before acceptance:** The submission has only been tested with one AI model, making it difficult to assess whether the prompt performs consistently across different models. Test at least two models using identical inputs and document their outputs, differences in behaviour, adherence to the instructions, and observed failure modes in a dedicated Results section. The comparison should identify where the models agree, disagree, fail to follow the prompt, or produce unsupported conclusions.

**Would improve it further:** Distinguish between failures caused by ambiguous or incomplete prompt instructions and those arising from model-specific limitations. Where relevant, include concrete examples of these failures and explain whether the prompt could be improved to prevent or reduce them.

---

### Automatic core/accessory genome and pathway analysis using Panaroo, MAUVE, and EggNOC
**Submitter:** Oleg Reva, University of Pretoria (0000-0002-5459-2772)

**Review by** @aidayo — 2026-10-19

| Criterion | /5 |
|---|---|
| Clarity | 5 |
| Effectiveness | 2 |
| Reusability | 5 |
| Robustness | 1 |
| Documentation | 4 |
| **Total** | **17/25** |

**Reviewer notes**

**Strongest aspect:** the constraints written into the prompts are 
Very well-targeted.

**Must fix before acceptance:**

1. **Cross-model comparison** says "to be performed".
2. **No recorded output**, Which failure modes were observed, and which
   are anticipated?
3. "EggNOC" in the title should be **eggNOG**.

**Would improve it further:** the task section has 26 numbered requirements.
It makes the entry hard to reuse selectively. Splitting the core/accessory
identification from the pathway representation analysis would give two entries that
could be used independently.

**Review by** @saifeldeen-bio — 2026-10-19
Criterion | Score
-- | --
Clarity | 5
Effectiveness | 1
Reusability | 5
Robustness | 3
Documentation | 5
Total | 19/25

**Reviewer notes**

**Strongest aspect:** The prompts anticipate several important technical challenges, including Mauve alignment coordinates, KEGG module logic, pathway coverage scoring, and appropriate statistical testing.

**Must fix before acceptance:** The submission needs a documented comparison of at least two AI models, including a Results section describing their performance on identical data and highlighting differences in the generated implementations.

**Would improve it further:** The extensive list of 26 requirements makes the task difficult to adapt to narrower research needs. Separating genome partitioning from downstream functional and pathway analysis would make both components more modular and independently reusable.

---

### Lift a variant call set from GRCh37 to GRCh38 without corrupting it
**Submitter:** Chioma Oselu

**Review by** @aidayo — 2026-10-19

| Criterion | /5 |
|---|---|
| Clarity | 5 |
| Effectiveness | 1 |
| Reusability | 4 |
| Robustness | 1 |
| Documentation | 2 |
| **Total** | **13/25** |

**Reviewer notes**

**Strongest aspect:** the biological and computational context is very well written. 
This task deserves an entry, and the judgement that re-mapping by rsID or re-calling 
against the correct build beats converting is also an interesting guidance.

**Must fix before acceptance:**

1. **Run it.** Worked example, known limitations, failure modes and validation are
   all TBC, and the date tested is empty.
2. **Model version** — add the full version for "Opus 4.8".
3. **Author field** needs an ORCID, and the affiliation.
4. **Cross-model comparison** — the entry's a good candidate for two models/

**Would improve it further:** Variant B asks the model to review a colleague's 
conversion that completed with no errors. That is a well-designed trap, because 
the correct answer is to not trust the absence of errors. It would be interesting
To record explicitly whether each model falls into it.

**Review by** @saifeldeen-bio — 2026-10-28

Criterion | Score
-- | --
Clarity | 3
Effectiveness | 3
Reusability | 4
Robustness | 2
Documentation | 2
Total | 14/25

**Reviewer notes**
**Strongest aspect:** The prompt highlights important risks of genome-build conversion, particularly coordinate conventions, contig naming mismatches, unmapped variants, and allele mismatches in inverted regions. The two variants provide useful approaches for beginners and experienced bioinformaticians.

**Must fix before acceptance:** The submission has not been tested, and no cross-model comparison has been performed. Test both prompt variants using at least two AI models, record their outputs, and include a Results section documenting their behaviour and any errors.

**Would improve it further:** Complete the Worked example, Known limitations, Failure modes observed, and Validation performed sections. Include a small example VCF and demonstrate how to verify the lifted coordinates and REF alleles against the GRCh38 reference. Also clarify the input requirements and expected outputs so the workflow can be reproduced and independently evaluated.

---
### script to minimize structure model
**Submitter:** fakher

**Review by** @aidayo — 2026-10-19

| Criterion | /5 |
|---|---|
| Clarity | 4 |
| Effectiveness | 1 |
| Reusability | 4 |
| Robustness | 1 |
| Documentation | 3 |
| **Total** | **13/25** |

**Reviewer notes** 

**Strongest aspect:** the five variants are very well differentiated by strategy, and
the biological framing is sound.

**Must fix before acceptance:**

1. **Model version.** "GPT" is recorded. We need the version string. Without it,
   the entry cannot be re-tested later.
2. **Author field** reads "fakher". Please add full name, affiliation and ORCID.
3. **Cross-model comparison** is empty.
4. **Failure modes observed** lists failure modes of *energy minimisation* — PDB
   preparation failures, force-field parameterisation, non-convergence. These are
   interesting but they should be listed under Known limitations. This section asks
   where the *language model* went wrong. For example, did it invent an OpenMM or 
   GROMACS parameter? 
5. **Validation performed** is it prospective ("the minimized structure is
   evaluated by…"), or was it actually done ?

**Would improve it further:** running one variant on two models and recording what 
each returned.

**Review by** @saifeldeen-bio — 2026-10-28
Criterion | Score
-- | --
Clarity | 3
Effectiveness | 2
Reusability | 3
Robustness | 2
Documentation | 2
Total | 12/25

**Reviewer notes**
**Strongest aspect:** The submission identifies relevant challenges in protein structure minimization and proposes useful quality checks, including RMSD, steric clashes, and Ramachandran analysis.

**Must fix before acceptance:** The cross-model comparison section incorrectly contains prompt variants rather than a comparison between different AI models. Test the same prompt and inputs with at least two models, then document their outputs, differences, and observed failures. The reported failure modes describe potential issues with the structural modelling workflow, not failures observed in the tested AI models.

**Would improve it further:** Provide a reproducible worked example with an actual PDB input and concrete results. Clarify which validation metrics were actually measured and which are only proposed, and complete the documentation with evidence from the experiments.

---
### Using the wrong FastQC input format
**Submitter:** Yossra-ElTony

**Review by** @aidayo — 2026-10-19

| Criterion | /5 |
|---|---|
| Clarity | 4 |
| Effectiveness | 4 |
| Reusability | 3 |
| Robustness | 4 |
| Documentation | 3 |
| **Total** | **18/25** |

**Reviewer notes**

**Strongest aspect:** the error analysis is excellent. 
There are five variants on two models.

**Must fix before acceptance:**

1. **Author field** contains only an ORCID URL. Please add name and affiliation.
2. **Expected output format** currently shows an error message rather than a
   description of what a correct response looks like. The error should go in the
   task section.
3. **Failure modes observed** describes Gemini's teaching-style explanation rather
   than identifying a model error, such as a model that invents a FastQC flag, miss one
   of the three faults, or produce code that still fails
4. Known limitations says variants "A–D", while there are five variants (A–E).

**Would improve it further:** the comparison is mainly qualitative ("more
detailed", "no significant differences"). It would improve it to add a small table 
recording, per variant and model, which of the three faults were caught.

**Review by** @saifeldeen-bio — 2026-10-28
Criterion | Score
-- | --
Clarity | 4
Effectiveness | 3
Reusability | 4
Robustness | 3
Documentation | 3
Total | 17/25

**Reviewer notes**
**Strongest aspect:** The submission compares two named AI models across five prompt framings and describes differences in their debugging explanations and code improvements. It also reports a specific observed issue and includes a Bash reproduction environment.

**Must fix before acceptance:** The author field is incomplete: provide the author's full name and affiliation alongside the ORCID. Also, verify and record the exact model version identifiers, as the current names may not be sufficient for reproducibility. The cross-model comparison would be stronger with actual outputs or a structured comparison of the errors each model identified, the corrections made, and any incorrect or missing fixes. The validation section confirms reproduction of the original failure but does not clearly document tests of the corrected scripts or their results.

**Would improve it further:** Clarify the discrepancy between the stated FASTQ filenames and the filenames used in the script, and ensure the expected output reflects the full debugging task rather than just one error message.
