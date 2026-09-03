# 0001 — Debug a failing Nextflow DSL2 process

> **Reference entry.** This is the main example: one task, five prompt
> variants, tested across two models. New contributors should read this
> before writing their own.

## Metadata

| Field | Value |
|---|---|
| **ID** | 0001 |
| **Domain** | Coding & pipelines |
| **Organism or data type** | Not applicable; workflow code |
| **Author** | Saifeldeen Elshahawy, University of Cape Town, ORCID: 0000-0003-0143-2596 |
| **Date tested** | 2026-05-20 |
| **Models tested** | ChatGPT Plus (GPT-5.6 Luna), Gemini 3.5 Flash |
| **Licence** | CC BY 4.0 |

## Objective

Diagnose and repair a Nextflow DSL2 process that terminates with a non-zero exit
status, and compare how different prompting strategies and different models
approach the same failure.

## Biological and computational context

It assumes Nextflow 24.10.6, local executor, and no container. The task is deliberately 
minimal so that the models' reasoning is visible rather than buried in pipeline 
complexity. The failure is representative of a common class: a script block references 
a file that does not exist, so the process exits non-zero and Nextflow halts the run.

The scientifically interesting question is not whether a model can make the error
go away. It is whether the model asks the right question, *is this file supposed
to exist?*, before proposing a fix.

## The task

```groovy
#!/usr/bin/env next flow
nextflow.enable.dsl=2

process SAY_HELLO {
    output:
    path "hello.txt"

    script:
    """
    echo "Hello Saif" > hello.txt
    cat missing_file.txt
    """
}

workflow {
    SAY_HELLO()
}
```

Observed error: `Process 'SAY_HELLO' terminated with an error exit status (1)`,
caused by `cat: missing_file.txt: No such file or directory`.

## Inputs required

- The failing workflow script
- The Nextflow error output, verbatim

## Prompt variants

### Variant A — Basic debugging

```text
This Nextflow DSL2 workflow generates an error during execution. Identify the
issue, explain why it happens, and provide a corrected version of the code.

{{PASTE CODE HERE}}
```

### Variant B — Expert in the domain

```text
You are an expert bioinformatics workflow engineer specialized in Nextflow and HPC
systems. Analyze the following workflow, identify execution errors, explain the
root cause, and rewrite the workflow following best practices for reproducibility
and error handling.

{{PASTE CODE HERE}}
```

### Variant C — Teaching style

```text
Explain this Nextflow error step-by-step as if teaching a beginner bioinformatics
student. Show what causes the problem and how to fix it.

{{PASTE CODE HERE}}
```

### Variant D — Production-level optimisation

```text
Review the following Nextflow workflow for errors, robustness, and
production-readiness. Improve the code by adding proper input validation, error
handling, and cleaner workflow structure.

{{PASTE CODE HERE}}
```

### Variant E — Minimal fix only

```text
Fix the error in this Nextflow script with the smallest possible code modification
and explain the change briefly.

{{PASTE CODE HERE}}
```

## Expected output format

Cause, location, corrected script, brief explanation of the change. Variants C and
D additionally expect pedagogical or structural commentary.

## Cross-model comparison

Variant E (minimal fix) run on two models:

| Variant | Model + version | Correct? | Approach taken | Notes |
|---|---|---|---|---|
| E | ChatGPT Plus (GPT-5.6 Luna) | Partly | Added `touch missing_file.txt` before the `cat` | Pipeline passes; underlying bug concealed |
| E | Gemini 3.5 Flash | No | Added a process directive to ignore the error | Directive does not exist; and the real equivalent would mask the failure |

### Response extracts

**ChatGPT** created the missing file so `cat` would not fail:

```groovy
echo "Hello Saif" > hello.txt
touch missing_file.txt
cat missing_file.txt
```

**Gemini** suppressed the error at the process level, using a directive that does
not exist:

```groovy
process SAY_HELLO {
    ignoreError true
    ...
}
```

### Results

Both models removed the symptom, but neither addressed the cause. ChatGPT's fix
fabricates an empty input so the pipeline reports success on data that was never
there. Gemini's is more dangerous: suppressing the exit status means the
process reports success while its command fails, which in a real pipeline produces
silent data loss downstream.

Neither model asked whether `missing_file.txt` was supposed to exist — which is the
first question a bioinformatician would ask, and the only route to a correct fix
(supply the file as a declared process input, or remove the line). The
minimal-fix framing in Variant E probably encouraged this. Running Variants B and D
on both models is the obvious next experiment, and is left open for a contributor.

## Known limitations

One toy workflow, one Nextflow version, two models. Variants A–D have not yet been
run across models. The behaviour on real pipelines with containers and HPC executors is
untested.

## Failure modes observed

- *Fabricated a process directive. Proposed `ignoreError true`. No such directive
  exists in Nextflow. The documented mechanism is `errorStrategy 'ignore'` —
  Gemini 3.5 Flash — 2026-05-20 — verified 2026-08-31 against the Nextflow process
  reference and the official patterns documentation, neither of which contains
  `ignoreError`. A search for the term returns no Nextflow results at all. Confirmed at runtime.*
- *Even the correct directive would not have been a correct fix. Under
  `errorStrategy 'ignore'` the process does not halt the run and the workflow
  completes with exit status 0 unless `workflow.failOnIgnore = true` is set — so
  the proposed approach yields a pipeline reporting success while its command
  fails — Gemini 3.5 Flash — 2026-05-20 — established from the Nextflow
  documentation, 2026-08-31.*
- *Resolved a missing-input error by creating an empty placeholder file, allowing the
  pipeline to report success on absent data — ChatGPT Plus (GPT-5.6 Luna) — 2026-05-20
  — detected by inspecting the corrected script.*
- *Neither model requested context about the intended input before proposing a fix —
  both models — 2026-05-20 — detected on reading the responses.*

## Validation performed

The original failure was reproduced on Nextflow 24.10.6, local executor. The `ignoreError`
directive was checked against the Nextflow process reference and the official
patterns documentation on 2026-08-31. Tt does not exist there, and the documented
mechanism is `errorStrategy 'ignore'`.

**Outstanding:** Run both corrected scripts and record what Nextflow does at parse
time with an unrecognised directive. The documentation settles whether the
directive exists. The run would show how loudly it fails, which is what determines
whether a user would notice.

## Related entries

[0002](0002-debug-pandas-keyerror.md) — a comparable debugging task in Python.
