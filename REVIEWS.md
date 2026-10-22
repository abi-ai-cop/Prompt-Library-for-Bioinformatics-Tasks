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

