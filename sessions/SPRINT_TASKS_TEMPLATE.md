# Sprint task list — template

*Copy this file to `sessions/sprint_tasks_<domain>.md` and replace the examples with
your own. See [`DOMAIN_LEAD_KIT.md`](DOMAIN_LEAD_KIT.md) for how the sprint runs.*

---

## Session

**Domain:** {{Literature & writing / Coding & pipelines / Genomics & annotation}}
**Lead:** {{name}}
**Date:** {{date}}
**Target:** {{N}} entries

## How to use this list during the sprint

Share it at 0:25, after your walkthrough. Each participant picks **one** task, or
brings their own. 

Write **6–8 tasks**, so there is one per participant with a little spare.

## Description of good task

A good task names a **specific problem** with a **specific input**, and says how many
variants and how many models.

- Good: *Take a failing script from your own work. Write three prompt variants asking
  for a fix — minimal instruction, expert persona, minimal-change-only — and run at
  least one on two different models.*
- Bad: *Try prompts for genome annotation.*

Every task should be completable in the 40-minute sprint. If it needs data that the
participant does not already have, it is too big.

**Anchor tasks in African data wherever you can** — pathogen genomics, crop genomics,
populations underrepresented in reference panels, workflows for constrained compute.
That is the library's distinctive contribution, and the task list is where it gets
built in.

---

## Tasks

### Task 1 — {{short title}}

**Input:** {{what the participant brings or is given}}
**Variants:** {{how many, and which strategies}}
**Models:** {{how many}}
**Record:** {{what to watch for — the failure modes this task is likely to highlight}}

### Task 2 — ...

---

## Worked examples

*Replace these with your own. They are here to show the format.*

### Literature & writing

**Find the citations.** Take a paragraph from your own introduction, remove the
citations, and ask three models to supply them. Use a paragraph from a recent
preprint, so the models cannot recall the originals. Record whether web search was
enabled — this changes everything. Score each returned reference in three
categories: exists and supports the claim; exists but does not support it; does not
exist.

**Paired-topic coverage.** Ask each model for the ten key papers on a globally
studied subject, and on a closely matched African-specific counterpart (human
variant calling versus variant calling in African reference panels, for example).
Before prompting, do your own PubMed and AJOL search as the reference standard.
Compare fabrication rates and author locations between the two.

**Summarise without inventing.** Attach three papers you know well and ask for a
comparison table. Check every cell against the source. Watch for cells quietly
filled from a different paper in the set.

### Coding & pipelines

**Debug a real failure.** Take a script from your own work that failed, and the error
message. Write three variants — minimal instruction, expert researcher with an explicit
demand for assumptions, and minimal-fix-only. Run at least one on two models. Watch
for fixes that make the error disappear without resolving it. See
[`../prompts/0002-debug-pandas-keyerror.md`](../prompts/0002-debug-pandas-keyerror.md).

**Constrained compute.** Ask for a workflow to process a dataset on 8 GB of RAM and
no cluster. Record whether the model recommends tools that cannot run in that
budget, and whether it says so or fails silently.

**Invented flags.** Ask for a command line using a tool you know well. Check every
flag and option against the actual documentation.

### Genomics & annotation

**Resistance markers.** Give a variant table from a pathogen you work on and ask for
classification of known resistance markers with references. Verify every DOI, and
check whether the model states its assumption about the reference build. See
[`../prompts/0004-plasmodium-variant-interpretation.md`](../prompts/0004-plasmodium-variant-interpretation.md).

**Reference build assumptions.** Give coordinates without naming the build. Record
whether the model asks, assumes silently, or states its assumption.

**Underrepresented organisms.** Ask the same annotation question about a
well-studied model organism and about a locally important crop or pathogen. Compare
the specificity and accuracy of the two answers.

---

## After the sprint

Collect the submission links and send them to the chair for `CONTRIBUTORS.md`.
Note which tasks produced the most interesting failures, those are worth reusing
in a later session.
