from selenium import webdriver
from Libraries import configRead
from Pages import Bootstrap_Date_picker
from Pages import jQuery_Date_picker
from Assersions import Forms_Assersions
from Pages import Simple_Form_Demo
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import pytest
import datetime

def test_008_TC_checkboxes1_section_heading(startbrowser):
    driver = startbrowser[0]
    wait = startbrowser[1]
    mouseaction = startbrowser[2]
    driver.find_element_by_xpath("//a[contains(text(),'Input Forms')]").click()
    driver.find_element_by_xpath("//a[contains(text(),'Checkbox Demo')]").click()
    #heading = driver.find_element_by_xpath("//div[text()='Single Checkbox Demo']").text
    #assert heading =="Single Checkbox Demo"

def test_009_TC_validate_checkbox1(startbrowser):
    driver = startbrowser[0]
    wait = startbrowser[1]
    mouseaction = startbrowser[2]
    driver.find_element_by_xpath("//input[@id='isAgeSelected']").click()
    #status = driver.find_element_by_xpath("//input[@id='isAgeSelected']").is_enabled()
    #assert status == True
    driver.find_element_by_xpath("//input[@id='isAgeSelected']").click()

def test_010_TC_Multiple_Checkbox_Demo_heading(startbrowser):
    driver = startbrowser[0]
    wait = startbrowser[1]
    mouseaction = startbrowser[2]
    heading = driver.find_element_by_xpath("//div[text()='Multiple Checkbox Demo']").text
    #assert heading =="Multiple Checkbox Demo"

def test_011_TC_Multiple_checkbox_select(startbrowser):
    driver = startbrowser[0]
    wait = startbrowser[1]
    mouseaction = startbrowser[2]
    driver.find_element_by_xpath("//label[text()='Option 1']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//label[text()='Option 2']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//label[text()='Option 3']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//label[text()='Option 4']").click()
    time.sleep(1)
    attvalue = driver.find_element_by_xpath("//input[@id='check1']").get_attribute("value")
    #assert attvalue == "Uncheck All"

def test_012_TC_uncheck_all_checkbox_click(startbrowser):
    driver = startbrowser[0]
    wait = startbrowser[1]
    mouseaction = startbrowser[2]
    driver.find_element_by_xpath("//input[@id='check1']").click()
    checkbox_state = driver.find_element_by_xpath("//input[@id='check1']").get_attribute("value")
    #assert checkbox_state =="Check All"








