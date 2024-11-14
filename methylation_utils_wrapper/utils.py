# utils.py
import os
import subprocess
import platform
import logging


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

    tool = "methylation_utils"
    if system == "Windows":
        tool += ".exe"
    bin_path = os.path.join(bin_dir, tool)

    logger.info("Running methylation_utils")
    try:
        cmd_args = [
            "--pileup", pileup,
            "--assembly", assembly,
            "--motifs", *motifs,
            "--threads", str(threads),
            "--min-valid-read-coverage", str(min_valid_read_coverage),
            "--output", output
        ]

        subprocess.run([bin_path] + cmd_args, check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Command '{e.cmd}' failed with return code {e.returncode}")
        logger.error(f"Output: {e.output}")
        return e.returncode

