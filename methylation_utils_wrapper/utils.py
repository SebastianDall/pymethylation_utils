# utils.py
import os
import subprocess
import platform
import logging

UTIL_NAME = {
    "Linux": "methylation_utils-linux",
    "Windows": "methylation_utils-windows.exe",
    "Darwin": "methylation_utils-macos",
}

def run_methylation_utils(
    pileup,
    assembly,
    motifs,
    threads,
    min_valid_read_coverage,
    output
):
    logger = logging.getLogger(__name__)
    system = platform.system()

    # Path to the downloaded binary
    bin_dir = os.path.join(os.path.dirname(__file__), "bin")

    tool = UTIL_NAME[system]
    bin_path = os.path.join(bin_dir, tool)

    # Configure environment
    env = os.environ.copy()
    env["POLARS_MAX_THREADS"] = str(threads)

    logger.info("Running methylation_utils")
    try:
        cmd_args = [
            "--pileup", pileup,
            "--assembly", assembly,
            "--motifs", *motifs,
            "--threads", str(threads),
            "--min-valid-read-coverage", str(min_valid_read_coverage),
            "--output", os.path.join(output, "motifs-scored-read-methylation.tsv")
        ]

        subprocess.run([bin_path] + cmd_args, check=True, env=env)
    except subprocess.CalledProcessError as e:
        logger.error(f"Command '{e.cmd}' failed with return code {e.returncode}")
        logger.error(f"Output: {e.output}")
        return e.returncode

