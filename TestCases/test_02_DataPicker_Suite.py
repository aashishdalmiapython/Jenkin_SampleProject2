from selenium import webdriver
from Libraries import configRead
from Pages import Bootstrap_Date_picker
from Pages import jQuery_Date_picker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import pytest
import datetime

def test_TC_001_bootstrap_date_picker_(startbrowser):
    driver = startbrowser[0]
    wait = startbrowser[1]
    mouseaction = startbrowser[2]
    # Select 31 March of the Last financial Year, irrespective of current date time.
    bootstrap = Bootstrap_Date_picker.bootStrapDate_Picker(driver,mouseaction,wait)
    bootstrap.select_date_picker_menu()
    bootstrap.select_bootstap_menu()
    bootstrap.click_first_date_field()
    bootstrap.month_select()
    bootstrap.date_select()

def test_TC_002_bootstrap_date_range_picker(startbrowser):
    driver = startbrowser[0]
    wait = startbrowser[1]
    mouseaction = startbrowser[2]
    bootstrap = Bootstrap_Date_picker.bootStrapDate_Picker(driver,mouseaction,wait)
    driver.execute_script('window.scrollTo(0, 40)')
    bootstrap.enter_current_date_in_second_field_section1()
    bootstrap.select_second_field_section2()
    bootstrap.clear_second_field_section1_value()
    bootstrap.select_16day_gap_date_value()

def test_TC_003_JQuery_date_range_picker(startbrowser):
    driver = startbrowser[0]
    wait = startbrowser[1]
    mouseaction = startbrowser[2]
    bootstrap = Bootstrap_Date_picker.bootStrapDate_Picker(driver, mouseaction, wait)
    bootstrap.select_date_picker_menu()
    jQuery = jQuery_Date_picker.jQueryClass(driver,mouseaction)
    jQuery.select_jQuery_date_menu()
    jQuery.click_first_date_field()
    jQuery.select_date_in_firstdate_field()
    time.sleep(3)
    driver.find_element_by_xpath("//input[2]").send_keys(jQuery.get_date())
    time.sleep(3)

