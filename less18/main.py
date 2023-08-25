import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet


def sum(path):
    workbook: Workbook = openpyxl.load_workbook(path)
    worksheet: Worksheet = workbook.active
    sum = 0
    for row in worksheet.iter_rows():
        for cell in row:
            if isinstance(cell.value, (int, float)):
                sum += cell.value
    return sum


if __name__ == "__main__":
    print(sum("less18/Лист.xlsx"))
