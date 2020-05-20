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
    return [driver, wait ,mouseaction]
