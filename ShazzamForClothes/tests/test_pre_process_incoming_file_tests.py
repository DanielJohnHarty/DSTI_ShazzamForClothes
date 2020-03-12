import os
import pytest
from ShazzamForClothes.img_preprocessor import pre_process_incoming_file, standardise_img
from ShazzamForClothes.tests import TESTS_ROOT_DIR


test_csv = os.path.join(TESTS_ROOT_DIR, "TestFiles", "ex_export_data.csv")


def test_yield_row_from_csv():
    gen_rows = pre_process_incoming_file.yield_rows_from_csv(test_csv)
    assert len(list(gen_rows)) == 3


def test_yield_row_from_csv2():
    gen_rows = pre_process_incoming_file.yield_rows_from_csv(test_csv)
    for i in gen_rows:
        print(i)
