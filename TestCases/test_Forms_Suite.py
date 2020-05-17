from selenium import webdriver
from Libraries import configRead
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

@pytest.fixture(scope="module")
def startbrowser():
    global driver
    global wait
    global mouseaction
    driver = webdriver.Chrome(executable_path=configRead.configRead("path","chrome_exe"))
    driver.get('chrome://settings/clearBrowserData')
    driver.find_element_by_xpath('//settings-ui').send_keys(Keys.ENTER)
    driver.implicitly_wait(30)
    driver.get(configRead.configRead('url','website'))
    driver.maximize_window()
    wait = WebDriverWait(driver,30)
    mouseaction =ActionChains(driver)
    if (wait.until(EC.visibility_of_element_located((By.XPATH,"//html/body/div[4]/div/div[1]/div/div[2]/a"))).is_displayed() == True):
        driver.find_element_by_xpath("//html/body/div[4]/div/div[1]/div/div[2]/a").click()
    yield
    driver.close()


def test_TC_004_title_Simple_Form_One(startbrowser):
    SimpleForm = Simple_Form_Demo.simpleformClass(driver)
    SimpleForm.input_form_link_click()
    SimpleForm.simple_form__demo_link_click()
    title = SimpleForm.get_form_1_title()
    Forms_Assersions.assert_title_form_1(title)

def test_TC_005_Sigle_input_field_check(startbrowser):
    driver.find_element_by_xpath("//input[@id='user-message']").send_keys("Aashish")
    driver.find_element_by_xpath("//button[contains(text(),'Show Message')]").click()
    entredtext = driver.find_element_by_xpath("//div[@id='user-message']/span").text
    assert entredtext == "Aashish"


def test_TC_006_title_sample_form2(startbrowser):
    sample = Simple_Form_Demo.simpleformClass(driver)
    title = sample.get_form2_title()
    Forms_Assersions.assert_title_form_2(title)

def test_TC_007_Double_input_field_check(startbrowser):
    sample = Simple_Form_Demo.simpleformClass(driver)
    sample.enter_form2_field1_value("5")
    sample.enter_form2_field2_value("10")
    sample.click__form2_get_result_button()
    result = sample.check_form2_result()
    assert result == "15"

