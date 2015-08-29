from selenium import webdriver
import xlrd
import time
from selenium.webdriver.common.action_chains import ActionChains

def loginToFlipkart(driver):

    try:
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
    except:
        print("Failure")
    #
    # if (driver.find_element_by_xpath("//*[@id='fk-mainhead-id']/div[1]/div/div[2]/div[1]/ul/li[7]/a").get):
    #     print("Hi there")
    #     return True
    # else:
    #     return False

def searchProduct(driver):

    try:
        file_location = "V:\PythonWorkspace\PyTest\Resources\Datasheet.xls"
        wbook = xlrd.open_workbook(file_location)
        sheet=wbook.sheet_by_name("Search")

        searchValue = sheet.cell(1,1).value

        driver.find_element_by_css_selector("#fk-top-search-box").send_keys(searchValue)
        driver.find_element_by_css_selector(".search-bar-submit.fk-font-13.fk-font-bold").click()
    except:
        print("Failure")

def logoutFlipkart(driver):

    try:
        hover = ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[@id='fk-mainhead-id']/div[1]/div/div[2]/div[1]/ul/li[7]/a"))
        hover.perform()
        driver.find_element_by_partial_link_text("Logout").click()
        driver.quit()
    except:
        print("Failure")
    #print(driver.find_element_by_xpath("//*[@id='fk-mainhead-id']/div[1]/div/div[2]/div[1]/ul/li[7]/a").is_displayed())