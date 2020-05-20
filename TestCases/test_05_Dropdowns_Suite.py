from selenium import webdriver
from Libraries import configRead
from Pages import Bootstrap_Date_picker
from Pages import jQuery_Date_picker
from TestCases import conftest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import pytest
import datetime


def test_16_TC_open_and_Select_Dropdown_Page(startbrowser):
    driver = startbrowser[0]
    wait = startbrowser[1]
    mouseaction = startbrowser[2]
    driver.find_element_by_xpath("//a[contains(text(),'Input Forms')]").click()
    wait.until(EC.presence_of_element_located((By.XPATH,"//div[@id='navbar-brand-centered']/ul/li[1]/ul/li[4]/a[contains(text(),'Select Dropdown List')]")))
    driver.find_element_by_xpath("//div[@id='navbar-brand-centered']/ul/li[1]/ul/li[4]/a[contains(text(),'Select Dropdown List')]").click()
    singledd = Select(driver.find_element_by_xpath("//select[@id='select-demo']"))
    singledd.select_by_value("Tuesday")

def test_17_TC_select_values_from_list_Dropdown(startbrowser):
    driver = startbrowser[0]
    wait = startbrowser[1]
    mouseaction = startbrowser[2]
    driver.execute_script('window.scrollTo(0, 25)')
    multidd = Select(driver.find_element_by_xpath("//select[@id='multi-select']"))
    mouseaction.key_down(Keys.CONTROL)
    multidd.select_by_value("Florida")
    time.sleep(5)
    multidd.select_by_index("3")
    mouseaction.key_up(Keys.CONTROL).perform()
    time.sleep(5)
    driver.find_element_by_xpath("//select[@id='multi-select']/following-sibling::button[2]").click()
    time.sleep(5)
    values = multidd.all_selected_options
    for i in values:
        print(i.text)



