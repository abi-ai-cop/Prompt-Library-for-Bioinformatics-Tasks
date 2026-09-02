# Contributing

## Style of an entry

An entry should have **one task** and **several prompt variants**,
tested across **more than one model**. The comparison is meaningful because 
the task is constant while the prompt varies. This  isolates the effect of 
the prompt rather than the effect of the problem.

Read [`prompts/0001-nextflow-failing-process-debug.md`](prompts/0001-nextflow-failing-process-debug.md)
first — it is the reference entry and shows the file style.

A single-variant, single-model entry,  is accepted, but that scores lower on Robustness.
Someone else may extend it later, which is encouraged, and shares credit.

## Instructions

1. Pick a task you have **actually worked on**. 
2. Copy `PROMPT_TEMPLATE.md` into `prompts/` as `NNNN-short-title.md`, using the next
   free number. Or open a [new prompt issue](../../issues/new?template=new_prompt.yml)
   and a maintainer will convert it. Use this if you do not know how to work with Git.
3. Fill **every** field. Write "not applicable" rather than deleting one.
4. Open a pull request, or submit the issue.

This should not take longer than twenty minutes.

## Accepted entries

- Entries for tasks you have run and can describe their output
- Prompts that failed, if the failure is documented and instructive
- **Extensions to existing entries**: a new variant, or an existing variant run on a
  Different model. Open a pull request against the entry. In this case, credit is shared 
  and it counts toward authorship exactly as a new entry.
- Failure-mode reports against existing entries, as issues
- Confirmations or corrections of an unconfirmed failure mode. The verification of someone
  else's observation is a real contribution

## Rejected entries

- Untested prompts
- Entries with an empty **Failure modes observed** section
- Entries with no model version or no test date
- Prompts copied from other libraries without attribution and without your own testing
- Anything containing patient-identifiable data, unpublished third-party data used
  without permission, or credentials

## Review

Two peers score each submission with `SCORING_SHEET.md`. To be accepted, a submission 
needs **≥ 15/25 overall and ≥ 3 on Documentation**. Reviewers leave their scores and 
notes in the pull request or issue thread, publicly. Turnaround target: **10 days**.

Reviewing qualifies reviewers for authorship. If you want to review, add yourself to the
reviewer list in `CONTRIBUTORS.md`.

## Writing good failure modes

This is the part with the most scientific value. For instance, a weak entry would says 
"sometimes hallucinates". A strong entry would say:

> *Classified a pfcrt variant as an established chloroquine-resistance marker and
> cited a 2019 paper whose DOI does not resolve — {{model + version}} — 2026-10-14 —
> detected by DOI lookup on every reference.*

Format: **observation — model and version — date — how you detected it.**

Two categories can be specifically looked for. Entry 0001 contains one of each:
**fabricated technical detail**: a tool flag, a config directive, an accession, a 
function argument that looks right but does not exist. 
**fixes that suppress rather than resolve** for instance, an output that makes an 
error disappear while leaving the cause in place. 

If you suspect a failure mode but have not verified it, record it and mark it
**needs confirmation**. Someone else can confirm it, and it will be a contribution.

## Data sovereignty and privacy

Most contributors will use hosted third-party models. Before pasting anything, please 
Sure you follow these rules:

- Never submit patient-identifiable data, consented-use-restricted data, or
  sequence data whose sharing agreement you have not checked.
- Use synthetic or public example data in the entry itself. Real data can inform
  the prompt without appearing in it.
- Where an institution's policy prohibits hosted models, note in the entry whether
  the prompt was tested on a locally deployed open-weight model.
- If a prompt only works with data that cannot leave your institution, state so under
  **Known limitations**. 

## Recognition

Every accepted contribution puts your name in `CONTRIBUTORS.md` and the Zenodo
record. The contribution list is public.

## Questions

Raise an issue, or bring it to a working session. The answer will be faster than by email.
