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

@pytest.fixture(scope="session")
def startbrowser():
    global driver
    global wait
    global mouseaction
    driver = webdriver.Chrome(executable_path=configRead.configRead("path","chrome_exe"))
    driver.get(configRead.configRead('url','website'))
    driver.implicitly_wait(30)
    driver.maximize_window()
    wait = WebDriverWait(driver,30)
    mouseaction =ActionChains(driver)
    if (wait.until(EC.visibility_of_element_located((By.XPATH,"//html/body/div[4]/div/div[1]/div/div[2]/a"))).is_displayed() == True):
        driver.find_element_by_xpath("//html/body/div[4]/div/div[1]/div/div[2]/a").click()
    yield
    driver.close()


def test_013_TC_Open_Radiobutton_page(startbrowser):
    driver.find_element_by_xpath("//a[contains(text(),'Input Forms')]").click()
    wait.until(EC.presence_of_element_located((By.XPATH,"//div[@id='navbar-brand-centered']/ul/li[1]/ul/li[3]/a[contains(text(),'Radio Buttons Demo')]")))
    driver.find_element_by_xpath("//div[@id='navbar-brand-centered']/ul/li[1]/ul/li[3]/a[contains(text(),'Radio Buttons Demo')]").click()
    assert driver.title == "Selenium Easy Demo - Radio buttons demo for Automation"

def test_014_TC_Select_radio_button(startbrowser):
    maleradio = driver.find_element_by_xpath("//div[text()='Radio Button Demo']/following-sibling::div/label[1]/input").is_selected()
    print(maleradio)
    if maleradio==False:
        driver.find_element_by_xpath("//div[text()='Radio Button Demo']/following-sibling::div/label[1]/input").click()
        maleradio2 = driver.find_element_by_xpath("//div[text()='Radio Button Demo']/following-sibling::div/label[1]/input").is_selected()
        print(maleradio2)
        if maleradio2 == True:
            driver.find_element_by_xpath("//div[text()='Radio Button Demo']/following-sibling::div/label[2]/input").click()
            female_radio = driver.find_element_by_xpath("//div[text()='Radio Button Demo']/following-sibling::div/label[2]/input").is_selected()
            print(female_radio)
            assert female_radio ==True


def test_015_TC_Select_dual_radio_button(startbrowser):
    driver.find_element_by_xpath("//div[text()='Group Radio Buttons Demo']/following-sibling::div/div[1]/label[1]").click()
    driver.find_element_by_xpath("//div[text()='Group Radio Buttons Demo']/following-sibling::div/div[2]/label[1]").click()
    driver.find_element_by_xpath("//div[text()='Group Radio Buttons Demo']/following-sibling::div/button").click()
    time.sleep(5)
    sex_text = driver.find_element_by_xpath("//div[text()='Group Radio Buttons Demo']/following-sibling::div/p[2]").text
    sex = str(sex_text).replace("Sex : ",'').strip()
