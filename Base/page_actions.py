from Libraries import configRead
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def add_wait_for_element(driver,wait,section,key):
    wait.until(EC.presence_of_element_located((By.XPATH,configRead.locatorRead(section,key))))

def click_button(driver,section,key):
    driver.find_element_by_xpath(configRead.locatorRead(section,key)).click()

def click_button_with_Wait(driver,wait,section,key):
    wait.until(EC.presence_of_element_located((By.XPATH,configRead.locatorRead(section,key))))
    driver.find_element_by_xpath(configRead.locatorRead(section,key)).click()

def get_all_open_windows(driver):
    allopenwindows = driver.window_handles
    return allopenwindows

