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
