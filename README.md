# pymethylation_utils
pymethylation_utils is a Python wrapper package for the methylation_utils binary, a Rust-based tool designed for handling DNA methylation data. This package simplifies the process of downloading, installing, and running methylation_utils from within Python projects.

## Features
 - Automatic Binary Download: The correct version of the methylation_utils binary is downloaded automatically during package installation based on the operating system.
 - Easy Integration: Provides a convenient Python function for calling methylation_utils, with all necessary parameters.
 - Multi-Platform Support: Works on Linux, macOS, and Windows.

## Installation
To install pymethylation_utils, you can use pip. The package will automatically download the correct binary for your system during installation.

```bash
pip install pymethylation_utils
```

## Usage
Once installed, you can import pymethylation_utils and use the run_methylation_utils function to process your DNA methylation data. This function takes the following parameters:

 - `pileup`: Path to the pileup file (BED format).
 - `assembly`: Path to the genome assembly file (FASTA format).
 - `motifs`: List of motifs to analyze [`<motif_sequence>_<mod_type>_<mod_position>`].
 - `threads`: Number of threads for parallel processing.
 - `min_valid_read_coverage`: Minimum valid read coverage threshold.
 - `output`: Path to where the output tsv file should be saved.
Example
Here’s an example usage in Python:

```python
from methylation_utils_wrapper.utils import run_methylation_utils

run_methylation_utils(
    pileup="path/to/pileup.bed",
    assembly="path/to/assembly.fasta",
    motifs=["GATC_a_1", "RGATCY_m_4"],
    threads=4,
    min_valid_read_coverage=3,
    output="path/to/output.tsv"
)
```
This will generate an output file named motifs-scored-read-methylation.tsv in the specified output directory.

## How It Works
The installation process uses a custom command to download the correct version of the methylation_utils binary based on your operating system:

 - Linux: Downloads the Linux binary from GitHub.
 - macOS: Downloads the macOS binary.
 - Windows: Downloads the Windows binary.
The binary is then stored within the package’s directory, ready to be invoked by the Python wrapper.
