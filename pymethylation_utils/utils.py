# utils.py
import os
import subprocess
import platform
import logging


def run_epimetheus(
    pileup,
    assembly,
    motifs,
    threads,
    min_valid_read_coverage,
    output,
    batches = 0
):
    logger = logging.getLogger(__name__)
    system = platform.system()

    # Path to the downloaded binary
    bin_dir = os.path.join(os.path.dirname(__file__), "bin")

    tool = "epimetheus"
    if system == "Windows":
        tool += ".exe"
    bin_path = os.path.join(bin_dir, tool)

    logger.info("Running epimetheus")
    try:
        cmd_args = [
            "methylation-pattern",
            "--pileup", pileup,
            "--assembly", assembly,
            "--motifs", *motifs,
            "--threads", str(threads),
            "--min-valid-read-coverage", str(min_valid_read_coverage),
            "--output", output,
            "--batch-size", str(batches)
        ]

        subprocess.run([bin_path] + cmd_args, check=True, text=True)
        return 0
    except subprocess.CalledProcessError as e:
        logger.error(f"Command '{e.cmd}' failed with return code {e.returncode}")
        logger.error(f"Stdout: {e.stdout}")
        logger.error(f"Stderr: {e.stderr}")
        return e.returncode

