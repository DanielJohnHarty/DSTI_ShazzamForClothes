import os
import pytest
import pre_process_incoming_file as ppi

current_path = os.path.dirname(os.path.abspath(__file__))

test_csv = os.path.join(current_path, "TestFiles", "ex_export_data.csv")


def test_yield_row_from_csv():
    gen_rows = ppi.yield_rows_from_csv(test_csv)
    assert len(list(gen_rows)) == 3


def test_yield_row_from_csv2():
    gen_rows = ppi.yield_rows_from_csv(test_csv)
    for i in gen_rows:
        print(i)
