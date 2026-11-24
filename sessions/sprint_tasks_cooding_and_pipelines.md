# Sprint tasks — Coding and bioinformatics pipelines

**Domain:** Coding & pipelines\
**Lead:** Saifeldeen Elshahawy\
**Date:** 2027-01-27\
**Target:** 8 entries

---

## How to use this list during the sprint

Pick **one** task, or bring your own. Two people may take the same task. If they use different models, their results combine into a stronger entry.

Everything here should be achievable within the 40-minute sprint. You do not need advanced programming or bioinformatics experience. You can ask the AI to explain the code and guide you through running it.

**Before you start:** Never paste patient-identifiable or restricted data into a hosted model. Use synthetic data, public datasets, or code without sensitive data.

**Important:** Use the same input for both AI models so that their outputs can be compared fairly.

---

## Tasks

### C 1 — Debugging a real bioinformatics script
What you need: A Python, R, Bash, or Nextflow script from your own work that produces an error, together with its error message.

**Prompts:** 
- A. Minimal instruction:
  This script produces the following error. Identify the problem and suggest a fix.
- B. Expert researcher:
  Act as an experienced bioinformatics software engineer. Examine the script and error message. Identify the root cause, explain your reasoning, and suggest a solution. State any assumptions you make.
- C. Minimal-change-only:
  Debug this script while making the smallest possible changes. Do not rewrite the entire script or modify unrelated sections. Explain every modification.

Models: 2

**Record:**
- Did the model identify the actual root cause?
- Did it suggest a fix that resolved the error or merely suppressed it?
- Did it rewrite working sections unnecessarily?
- Did it introduce new errors while fixing the original problem?
- Did it explain assumptions or make unsupported assumptions about the input data?
---

### C 2 — Building a simple RNA-seq pipeline using Nextflow

**What you need:** The following publicly available paired-end FASTQ files.

**Test FASTQ files:**

| Sample    | Condition | File                                                                                                                                                                        |
| --------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GSM461177 | Untreated | [Read 1](https://zenodo.org/record/6457007/files/GSM461177_1_subsampled.fastqsanger) / [Read 2](https://zenodo.org/record/6457007/files/GSM461177_2_subsampled.fastqsanger) |
| GSM461180 | Treated   | [Read 1](https://zenodo.org/record/6457007/files/GSM461180_1_subsampled.fastqsanger) / [Read 2](https://zenodo.org/record/6457007/files/GSM461180_2_subsampled.fastqsanger) |

Organism: *Drosophila melanogaster*

Reference genome: [Download FASTA](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/215/GCF_000001215.4_Release_6_plus_ISO1_MT/GCF_000001215.4_Release_6_plus_ISO1_MT_genomic.fna.gz)

Gene annotation: [Download GTF](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/215/GCF_000001215.4_Release_6_plus_ISO1_MT/GCF_000001215.4_Release_6_plus_ISO1_MT_genomic.gtf.gz)

**Study information:**

- Untreated samples: GSM461176, GSM461177, GSM461178, GSM461182.
- Treated samples (*Pasilla* gene depleted by RNAi): GSM461179, GSM461180, GSM461181.
Tasks
Additional sample information is available from [NCBI GEO](https://www.ncbi.nlm.nih.gov/geo/).

**Note:** The two supplied FASTQ pairs are intended for testing the pipeline. They represent only one sample per condition, so they are not sufficient for reliable biological differential-expression analysis. The other study samples should be included for a proper analysis.

**Prompts:**

- **A. Minimal:**

  *Write a simple Nextflow pipeline to process the supplied RNA-seq FASTQ files. Include downloading the FASTQ files, reference genome, and GTF using the provided links. Explain how to run the pipeline.*

- **B. More detailed:**

  *Develop a Nextflow DSL2 pipeline for RNA-seq analysis using the supplied FASTQ files. Include quality control, read trimming, alignment, and gene expression quantification. Explain each step, the tools used, and the expected output files. Also explain how differential expression analysis could be performed when biological replicates are available.*

- **C. Reproducibility-focused:**

  *Improve the pipeline by including software version management, error handling, and a simple configuration file. Explain how another researcher could run the same pipeline on a different computer.*

**Models:** 2

**Record:**

- Did the model generate valid Nextflow syntax?
- Did it correctly identify paired-end FASTQ files?
- Did it use appropriate tools for each step?
- Did it connect the pipeline processes correctly?
- Did it invent commands or software parameters?
- Could you successfully run at least one stage of the generated pipeline?

---

### C 3 — Running bioinformatics analysis with limited computing resources

**What you need:** A Linux computer with limited resources.

**Scenario:** A researcher has a Linux workstation with 8 GB RAM, 4 CPU cores, and no access to an HPC cluster.

**Example dataset:**

A publicly available BAM file from the 1000 Genomes Project:

[Download HG00096 BAM](https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/phase3/data/HG00096/exome_alignment/HG00096.mapped.ILLUMINA.bwa.GBR.exome.20120522.bam)

**Prompts:**

- **A. General instruction:**

  *I have a Linux computer with 8 GB RAM and 4 CPU cores. Design a simple Nextflow workflow to perform WES variant calling using this BAM file. Explain the tools and commands I need.*

- **B. Resource-aware instruction:**

  *Design a practical WES variant-calling workflow for a Linux workstation with 8 GB RAM and 4 CPU cores. Prioritize memory-efficient tools and approaches. Explain the expected resource requirements of each step and suggest alternatives when a tool cannot run within the available resources.*

**Models:** 2

**Record:**

- Does the model respect the available computing resources?
- Does it recommend tools that require more RAM than available?
- Does it suggest realistic alternatives?
- Does it explain potential limitations?
- Does it acknowledge when the analysis is impractical under the given constraints?

---

### C 4 — Generating bioinformatics commands

**What you need:** A BAM file and a bioinformatics tool.

You can use the BAM file from Task 3.

Examples of tools:

- samtools
- bcftools
- GATK
- BWA
- Manta
- DELLY

**Prompts:**

- **A. Minimal:**

  *Write a command to perform [your selected analysis] using [selected tool].*

- **B. Documentation-driven:**

  *Write a command to perform the same analysis using [selected tool]. Explain each argument and option in simple language. Only use options supported by the official documentation for the specified software version. Provide the relevant documentation reference.*

**Models:** 2

**Record:**

- Are all command-line options valid?
- Does the model invent parameters or arguments?
- Does it confuse different tools or subcommands?
- Does it use the correct input and output formats?
- Does the command work when tested?
- Does the documentation support the suggested command?

**Important:** Choose a tool appropriate for the analysis. For example, samtools can inspect and manipulate BAM files, but it is not itself a structural-variant caller. For SV calling, use an appropriate caller such as Manta or DELLY.

---

### C 5 — Working with genomic file formats

**What you need:** A VCF file and a GFF annotation file.

Example files:

**GFF file:**

[Download human GRCh38 GFF](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/405/GCF_000001405.26_GRCh38/GCF_000001405.26_GRCh38_genomic.gff.gz)

**VCF file:**

[1000 Genomes high-coverage VCF](https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data_collections/1000G_2504_high_coverage/working/20201028_3202_raw_GT_with_annot/20201028_CCDG_14151_B01_GRM_WGS_2020-08-05_others.recalibrated_variants.vcf.gz)

**Scenario:** A researcher wants to identify which genes overlap with the variants in a VCF file.

**Prompts:**

- **A. Minimal:**

  *Write a simple Python or Bash script to identify variants overlapping genes using these GFF and VCF files.*

- **B. Explanation-focused:**

  *Write a script to identify genomic variants overlapping gene regions using the supplied GFF and VCF files. Explain how the script handles chromosome names, genomic coordinates, and overlapping regions. Explain the code in simple language.*

**Models:** 2

**Record:**

- Did the model understand the differences between GFF and VCF coordinates?
- Did it handle chromosome naming consistently?
- Did it correctly identify overlapping variants?
- Did it introduce off-by-one errors?
- Did the script produce the expected results?

**Tip:** These files can be large. Participants can ask the AI to extract a small genomic region for testing rather than processing the entire dataset.

---

### C 6 — Writing tests for bioinformatics scripts

**What you need:** A small Python or R script that performs a bioinformatics task, such as filtering variants, calculating read-depth statistics, or processing gene annotations, from your own work.

**Prompts:**

- **A. Minimal:**\
  *Write unit tests for this script.*
- **B. Test-driven and validation-focused:**\
  *Develop unit tests for this bioinformatics script using appropriate testing frameworks. Include normal inputs, missing values, empty files, malformed records, unexpected data types, and boundary cases. Explain what each test is checking and provide expected outputs.*

**Models:** 2

**Record:**

- Does the model generate executable tests?
- Does it cover realistic bioinformatics edge cases?
- Does it test the biological logic or only the code syntax?
- Does it identify situations where the script produces technically valid but biologically incorrect results?
- Do the tests actually fail when an intentional error is introduced?
- Does it provide meaningful expected outputs?

---

### C 7 — Improving pipeline reproducibility and portability

**What you need:** An existing bioinformatics script or pipeline that runs successfully on your computer but is difficult to reproduce on another machine.

**Scenario:** A researcher has developed a variant-calling workflow on an institutional HPC system and wants to make it portable to another research institution with different infrastructure.

**Prompts:**

- **A. Minimal:**\
  *Improve this pipeline to make it reproducible and portable.*
- **B. Reproducibility-focused:**\
  *Review this bioinformatics pipeline and identify potential reproducibility and portability issues. Suggest improvements involving software version pinning, dependency management, containers, reference genome management, configuration files, logging, and workflow documentation. Do not rewrite working components unnecessarily.*

**Models:** 2

**Record:**

- Does the model identify hidden software dependencies?
- Does it distinguish between software versions and reference genome versions?
- Does it recommend realistic containerization strategies?
- Does it address reproducibility of reference databases and annotation resources?
- Does it introduce unnecessary complexity?
- Could another researcher reproduce the analysis using the resulting documentation and configuration?

---

### C 8 — Diagnosing silent failures and validating biological outputs

**What you need:** A script or small pipeline that completes without errors but produces suspicious results. Examples include an empty VCF, unexpectedly low variant counts, missing genes, or unusually high numbers of detected variants.

**Prompts:**

- **A. Minimal:**\
  *This pipeline completed successfully but produced unexpected results. Help me identify the problem.*
- **B. Validation-focused:**\
  *Act as an experienced bioinformatics pipeline developer. Investigate why this pipeline completed successfully but produced unexpected biological results. Examine the code, input assumptions, intermediate files, filtering criteria, and output statistics. Suggest validation checks at each stage. Distinguish between confirmed problems and possible explanations.*

**Models:** 2

**Record:**

- Does the model distinguish between successful execution and biologically valid results?
- Does it identify potential silent failures?
- Does it examine intermediate outputs rather than focusing only on the final file?
- Does it suggest appropriate quality-control checks?
- Does it invent explanations without sufficient evidence?
- Does it distinguish technical errors from biological explanations?
- Does it propose independent validation strategies?

---

## After the sprint

Collect the submission links and send them to the chair for `CONTRIBUTORS.md`.

For each task, pleases document:

1. The original problem and input.
2. The exact prompts and their variants.
3. The model names and exact model versions.
4. The outputs generated by each model.
5. Whether the generated code or commands worked.
6. The validation performed.
7. The observed failure modes.
8. A comparison of the models' performance.

Prioritize tasks that reveal interesting failure modes, particularly cases where the model generates plausible-looking code that does not produce the expected results.

These are particularly valuable contributions to the ABI Prompt Library.
