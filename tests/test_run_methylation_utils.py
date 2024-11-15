from methylation_utils_wrapper.utils import run_methylation_utils
import pytest
import os
import platform

def test_run_methylation_utils(capsys):
    code = run_methylation_utils(
        "p",
        "a",
        ["m"],
        1,
        1,
        "out.csv"
    )

    assert code == 1, "The function did not fail"

def test_file_exists():
    system = platform.system()
    tool = "methylation_utils"
    if system == "Windows":
        tool += ".exe"

    bin_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "methylation_utils_wrapper", "bin")
    )
    tool_path = os.path.join(bin_dir, tool)

    # Assert that the tool exists
    assert os.path.isfile(tool_path), f"The tool '{tool}' does not exist at '{tool_path}'"

@pytest.fixture
def cleanup_output():
    outfile = "out.tsv"
    yield outfile  # Provide the output file path to the test
    # Clean up after the test
    if os.path.exists(outfile):
        os.remove(outfile)

def test_actual_run(cleanup_output):
    print("Current working directory:", os.getcwd())
    print("File exists:", os.path.exists("methylation_utils_wrapper/data/geobacillus-plasmids.pileup.bed"))
    print("File exists:", os.path.exists("methylation_utils_wrapper/data/geobacillus-plasmids.assembly.fasta"))

    code = run_methylation_utils(
        "methylation_utils_wrapper/data/geobacillus-plasmids.pileup.bed",
        "methylation_utils_wrapper/data/geobacillus-plasmids.assembly.fasta",
        ["GATC_a_1"],
        1,
        1,
        cleanup_output
    )

    assert code == 0
    assert os.path.exists(cleanup_output)
