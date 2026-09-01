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

<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/f844a69b-0b81-458c-9149-3aa99da840fe" />

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

### Result:

<img width="783" height="282" alt="image" src="https://github.com/user-attachments/assets/f3d6e49e-1da5-4a26-9fb3-8a681d0971d4" />

As you can see here. ChatGpt solution worked perfectly and fixed the root error

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

### Result

<img width="814" height="268" alt="image" src="https://github.com/user-attachments/assets/61452bf2-8367-4c99-973f-4b74231b8378" />

Gemini response resulted with another error as the suggested directive is not even from Nextflow defined directives. The correct directive should be `errorStrategy 'ignore'`. and when running the workflow again with this directive it will work well as you can see below

<img width="897" height="296" alt="image" src="https://github.com/user-attachments/assets/d108d1e4-1176-4c5f-8bad-1d067ac31fba" />

Look at the Note section as it is showing that the workflow had an ignored error but it continued to run without terminating the entire process.

### Conclusion:
The two AI models approached the same debugging task from substantially different perspectives. ChatGPT focused on addressing the immediate source of the pipeline failure by creating the missing file through a minimal code modification (`touch missing_file.txt`). Although this allows the workflow to proceed, it does not necessarily establish why the file was missing or whether creating an empty file is biologically or computationally appropriate. In contrast, Gemini 3.5 Flash approached the problem from a workflow-management perspective by suggesting the use of `ignoreError true`, allowing the process to continue despite the underlying error. However, this recommendation represents a form of AI hallucination, as Gemini invented `ignoreError true`, and it was not an appropriate or valid solution for the specific workflow context and would effectively mask a genuine pipeline failure rather than resolve its underlying cause.

This example highlights how different AI models can adopt fundamentally different debugging philosophies: one may attempt to modify the input or environment to allow execution to continue, while another may prioritize workflow robustness by suppressing errors. Importantly, neither approach necessarily addresses the most critical diagnostic question: **why was the expected file missing in the first place, and was its absence intentional?** This demonstrates the importance of prompt engineering and human validation in AI-assisted bioinformatics coding, where the same prompt can lead to substantially different interpretations, proposed fixes, and recommendations for best practices. In computational biology workflows, where silently bypassing an error or generating artificial input files can compromise downstream analyses, AI-generated solutions should therefore be evaluated not only for whether they make a pipeline execute successfully, but also for whether they preserve the intended scientific logic of the workflow.
