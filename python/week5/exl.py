import openpyxl


wb = openpyxl.load_workbook("example.xlsx")
print(type(wb))
sheet = wb[wb.sheetnames[0]]
print(type(sheet["C1"].value))
print(sheet)

for i in sheet:
    print(i)