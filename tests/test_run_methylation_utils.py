from pymethylation_utils.utils import run_epimetheus
import pytest
import os
import platform

def test_run_epimetheus(capsys):
    code = run_epimetheus(
        pileup = "p",
        assembly = "a",
        motifs = ["m"],
        threads = 1,
        min_valid_read_coverage = 1,
        output = "out.csv"
    )

    assert code == 1, "The function did not fail"

def test_file_exists():
    system = platform.system()
    tool = "epimetheus"
    if system == "Windows":
        tool += ".exe"

    bin_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "pymethylation_utils", "bin")
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
    data_dir = os.path.join(os.path.dirname(__file__), "data")

    bed = os.path.join(data_dir,"geobacillus-plasmids.pileup.bed")
    assembly = os.path.join(data_dir,"geobacillus-plasmids.assembly.fasta")
    print("File exists:", os.path.exists(bed))
    print("File exists:", os.path.exists(assembly))

    code = run_epimetheus(
        pileup = bed,
        assembly = assembly,
        motifs = ["GATC_a_1"],
        threads = 1,
        min_valid_read_coverage = 1,
        output = cleanup_output
    )

    assert code == 0
    assert os.path.exists(cleanup_output)
