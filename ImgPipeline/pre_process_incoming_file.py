import standardize_Img as sti
import csv

def yield_rows_from_csv(csv_pth):
    with open(csv_pth,'rt')as file:
        data = csv.reader(file)
        for row in data:
                yield row
