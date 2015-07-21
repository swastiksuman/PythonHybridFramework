from selenium import webdriver
import xlrd
import time

def loginToFlipkart(driver):
    
    file_location = "V:\PythonWorkspace\PyTest\Resources\Datasheet.xls"
    wbook = xlrd.open_workbook(file_location)
    sheet=wbook.sheet_by_name("Login")
    
    username = sheet.cell_value(1,1)
    password = sheet.cell_value(1,2)
    
    driver.get("http://www.flipkart.com")
    driver.maximize_window()
    driver.find_element_by_css_selector(".no-border.js-login.login-required").click()
    driver.find_element_by_css_selector(".fk-input.login-form-input.user-email").send_keys(username)
    driver.find_element_by_css_selector(".fk-input.login-form-input.user-pwd").send_keys(password)
    driver.find_element_by_css_selector(".submit-btn.login-btn.btn").click()
    
    time.sleep(5)
    
    return True


def searchProduct(driver):
    
    file_location = "V:\PythonWorkspace\PyTest\Resources\Datasheet.xls"
    wbook = xlrd.open_workbook(file_location)
    sheet=wbook.sheet_by_name("Search")
    
    searchValue = sheet.cell(1,1).value
    
    driver.find_element_by_css_selector("#fk-top-search-box").send_keys(searchValue)
    driver.find_element_by_css_selector(".search-bar-submit.fk-font-13.fk-font-bold").click(
                                                                                            )

    





                                              

    