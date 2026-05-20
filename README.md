# Prompt-Library-for-Bioinformatics-Tasks

A curated collection of high-quality prompts designed to assist with a wide range of bioinformatics workflows and analyses using AI tools. This collection provides valuable resources for prompt engineering, including training materials, educational resources, and reusable high-quality prompts for genome annotation, literature review, variant interpretation, workflow generation, coding assistance, protein analysis, scientific writing, and more.

## Coding Assistance

AI-powered prompt engineering can significantly improve coding assistance in bioinformatics by helping researchers debug workflows, optimize pipelines, generate scripts, explain errors, and improve reproducibility. Modern AI models can assist with workflow languages such as Nextflow, WDL, Snakemake, Bash, Python, and R, making it easier for bioinformaticians to identify issues in complex HPC and sequencing analysis pipelines. By providing clear and structured prompts, users can compare how different AI models interpret, debug, and improve the same piece of code.

For example, the following Nextflow workflow will generate an error because the file missing_file.txt does not exist:

```nextflow
#!/usr/bin/env nextflow

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

<img width="1920" height="1200" alt="Screenshot from 2026-05-20 14-41-38" src="https://github.com/user-attachments/assets/8be8f71b-95f6-4c61-a2d5-0829c84a168a" />

Example prompts that can be tested across different AI models:

### Prompt 1 — Basic Debugging

```
This Nextflow DSL2 workflow generates an error during execution. Identify the issue, explain why it happens, and provide a corrected version of the code.
[PASTE CODE HERE]
```

### Prompt 2 — Bioinformatics Workflow Expert
```
You are an expert bioinformatics workflow engineer specialized in Nextflow and HPC systems. Analyze the following workflow, identify execution errors, explain the root cause, and rewrite the workflow following best practices for reproducibility and error handling.

[PASTE CODE HERE]
```

### Prompt 3 — Teaching Style
```
Explain this Nextflow error step-by-step as if teaching a beginner bioinformatics student. Show what causes the problem and how to fix it.

[PASTE CODE HERE]
```
### Prompt 4 — Production-Level Optimization
```
Review the following Nextflow workflow for errors, robustness, and production-readiness. Improve the code by adding proper input validation, error handling, and cleaner workflow structure.

[PASTE CODE HERE]
```
### Prompt 5 — Minimal Fix Only
```
Fix the error in this Nextflow script with the smallest possible code modification and explain the change briefly.

[PASTE CODE HERE]
```
## Models Benchmarking
Here, we'll test Prompt 5 — Minimal Fix Only On different AI Models, We'll use `ChatGPT plus`, and `Gemini 3.5 Flash`, to see how each model can debug that error.

### User:

```
User: Fix the error in this Nextflow script with the smallest possible code modification and explain the change briefly.
```
And then Paste the Code
```
#!/usr/bin/env nextflow

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
### ChatGPT Response:

The error happens because the script tries to read a file that does not exist:

```bash
cat missing_file.txt
```

The smallest possible fix is to create the file before reading it.

```nextflow
#!/usr/bin/env nextflow

nextflow.enable.dsl=2

process SAY_HELLO {

    output:
    path "hello.txt"

    script:
    """
    echo "Hello Saif" > hello.txt
    touch missing_file.txt
    cat missing_file.txt
    """
}

workflow {
    SAY_HELLO()
}
```

### What changed?

Added this line:

```bash
touch missing_file.txt
```

This creates an empty file named `missing_file.txt`, so the `cat` command no longer fails.


### Gemeni Flash Response:
The error in this script happens because `cat missing_file.txt` tries to read a file that doesn't exist. By default, Nextflow catches this non-zero exit code and crashes the pipeline.

To fix it with the smallest possible modification, add the `ignoreError true` directive to the process. This tells Nextflow to carry on even if a command inside the script block fails.

Here is the corrected script:

```nextflow
#!/usr/bin/env nextflow

nextflow.enable.dsl=2

process SAY_HELLO {
    ignoreError true

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

### What changed?

* **Added `ignoreError true`:** This directive allows the process to finish successfully and output `hello.txt`, ignoring the fact that `cat missing_file.txt` failed.

*(Note: If you actually needed `missing_file.txt` to exist, you would instead pass it into the process via an `input:` block, but `ignoreError true` is the cleanest way to bypass the explicit failure in the script as written.)*

As you can see, each AI model approached the same debugging task from a completely different perspective.  ChatGPT focused on fixing the root cause of the error directly by creating the missing file with a minimal code modification (`touch missing_file.txt`), which preserves the intended workflow execution and prevents the pipeline from failing. In contrast, Gemini 3.5 Flash handled the problem from a workflow-management perspective by adding `ignoreError true`, allowing the process to continue even though the underlying issue still exists. This is how different AI models may prioritize different debugging philosophies: some models aim to resolve the actual source of failure, while others focus on maintaining pipeline execution and fault tolerance. You can see also the importance of prompt engineering in bioinformatics coding assistance, where the same prompt can produce substantially different interpretations, fixes, and best-practice recommendations across models.
