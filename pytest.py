import time
import xlrd
import FirstTest
import turtle
from selenium import webdriver
from xlwt.Workbook import Workbook

#Check the Driver sheet and iterate
file_location = "V:\PythonWorkspace\PyTest\Resources\Driver.xls"
wbook = xlrd.open_workbook(file_location)
sheet=wbook.sheet_by_name("Driver")

for i in range(1,sheet.nrows):
    execute_Flag = sheet.cell(i,1).value
    if execute_Flag:

        driver = webdriver.Firefox()

        for j in range(1,sheet.ncols):
            if sheet.cell(i,j).value !="":
                eval("FirstTest."+sheet.cell(i,j).value+"(driver)")


