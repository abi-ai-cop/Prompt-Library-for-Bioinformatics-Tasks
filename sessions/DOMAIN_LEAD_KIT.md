# Domain lead kit

*ABI AI CoP — Shared Prompt Library working sessions*

You have agreed to lead one working session. This document guides you in the preparation.
Preparation is two to three hours. It gives you the design and the shape of the session, 
so that you don't start from scratch.

Leading a session meets the authorship criteria for the resource paper 
(`../AUTHORSHIP_CRITERIA.md`). You are also named as session lead in `../CONTRIBUTORS.md`
and in the release notes for the version your session contributed to.

---

## Objective of the session

The session is made to **produce prompt library entries**, not to discuss prompting. 
If it ends with a good discussion and no entries, it has failed.
If it ends with eight entries and a mediocre discussion, it has succeeded.

Please run the session while keeping in mind to protect the sprint block. That is the part
under pressure, and the most important part.

---

## Agenda — 90 minutes

| Time | Block | Who |
|---|---|---|
| 0:00–0:05 | Welcome; state a numeric target: *"we leave with N entries"* | You |
| 0:05–0:25 | Your talk (20 min) | You |
| 0:25–0:35 | Walk through one entry on screen, then hand out the sprint task list | You |
| 0:35–1:15 | **Sprint.** Everyone writes and tests a prompt | Everyone |
| 1:15–1:30 | Peer scoring in pairs, then submissions pushed, and count announced | Everyone |

**Timekeeping is important.** Set an alarm.

### Session lead 20-minute talk

It shouldn't be a tutorial. Rather:

1. **How you actually use LLMs in this domain.** A real task from your own work.
2. **Where it fails.** The concrete case where the model was confidently wrong, and
   how you caught it. This part gives everyone
   permission to submit failures rather than only successes.
3. **Walk through one prompt line by line.** Explain why each instruction is there.

Slides are optional, and a screen share of a real session would be better than slides.

### Sprint

- Share the task list (below). Each person picks one task, or brings their own.
- Ask that everyone works in silence for the first 15 minutes. Otherwise,
  it could become a discussion and nothing gets written.
- You could split the audience in breakout rooms of three or four if the group is large, and circulate in rooms, or use the chat for discussions.
- At 1:10, warn everyone that submissions close in five minutes. 
- At the end, submissions can be made through the issue form. Participants do not need to know Git.

### Peer scoring

Pairs. Each person scores their partner's entry with `../SCORING_SHEET.md` and leaves
the scores as a comment. (10 minutes). 

---

## Preparation of your sprint task list

Write **6–8 concrete tasks** before the session, in `sprint_tasks_<domain>.md`. One
per participant, so that nobody spends sprint time deciding what to do.

A good task names a specific problem with a specific input:

> *Take a failing script from your own work. Write three prompt variants asking for
> a fix — minimal instruction, expert researcher, minimal-change-only — and run at
> least one on two different models.*

A bad task is a topic: *"try prompts for genome annotation."*

**Include African-data anchors wherever you can.** Pathogen genomics, crop genomics,
populations underrepresented in reference panels, workflows for constrained compute.
That is the library's distinctive contribution.

---

## Information for contributors

- An entry is **one task, several prompt variants, tested on more than one model.**
- Read `../prompts/0001-nextflow-failing-process-debug.md` first — it is the reference entry.
- **Failure modes are required**, not optional. Format: *observation — model and
  version — date — how you detected it.*
- Model **version** and test date must be recorded.
- Never paste patient-identifiable or restricted data into a hosted model.

---

## To do before the session

- [ ] Pick your date and time, and  send it to the chair (Check the time works across West, East, North, and Southern Africa)
- [ ] Write your 6–8 sprint tasks
- [ ] Prepare your 20 minutes
- [ ] Run one prompt yourself and submit it through the form, so you can demo a
      path you have walked

## After the session

- [ ] Post the count in the CoP channel the same day — *"we added N entries"*
- [ ] Open a review issue for any entry that did not get scored
- [ ] Send the chair the list of contributors for `../CONTRIBUTORS.md`

---

## Solutions to possible issues

**Only three people turn up.** Run it anyway, as a working call.

**Nobody has a task of their own.** That is why you have to prepare a task list, so you can assign them.

**The sprint turns into a discussion.** Tell everyone to *first write and then discuss
in the last fifteen minutes.* 

**Someone submits a prompt they have not tested.** Accept it as a draft, mark it
untested, and ask them to run it within the week. Do not reject it.

---

## For any questions:

Ask the chair (Aida), the secretary (Rosie), or the repository maintainer (Saifeldeen). This kit is meant to be improved by the people using it, so tell us what is missing from it.
