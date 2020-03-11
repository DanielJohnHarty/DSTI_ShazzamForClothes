import os
import pytest
from context import img_preparation, tests_root_dir
from img_preparation import pre_process_incoming_file
from img_preparation import standardise_img


test_csv = os.path.join(tests_root_dir, "TestFiles", "ex_export_data.csv")


def test_yield_row_from_csv():
    gen_rows = img_preparation.pre_process_incoming_file.yield_rows_from_csv(test_csv)
    assert len(list(gen_rows)) == 3


def test_yield_row_from_csv2():
    gen_rows = img_preparation.pre_process_incoming_file.yield_rows_from_csv(test_csv)
    for i in gen_rows:
        print(i)
