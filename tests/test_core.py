import pytest
from a5toa4.core import merge_a5_to_a4_pdfs
from pathlib import Path

def test_merge_a5_to_a4_pdfs():

    file1 = "tests/testfiles/A5_horizontal_tikz/A5_A.pdf"
    file2 = "tests/testfiles/A5_horizontal_tikz/A5_B.pdf"
    file_out = "tests/testfiles/output"

    f1path = Path(file1)
    f2path = Path(file2)
    foutpath = Path(file_out)

    merge_a5_to_a4_pdfs([f1path, f2path], foutpath)


    pass