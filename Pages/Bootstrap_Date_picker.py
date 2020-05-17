from Libraries import configRead
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import datetime


import time

class bootStrapDate_Picker():

    def __init__(self,obj,objaction,objwait):
        global driver
        global mouseaction
        global wait
        driver = obj
        mouseaction = objaction
        wait =objwait



    def select_date_picker_menu(self):
        wait.until(EC.presence_of_element_located((By.XPATH, configRead.locatorRead('Date', 'Dpicker_menu_xpath')))).click()
        time.sleep(3)

    def select_bootstap_menu(self):
        driver.find_element_by_xpath(configRead.locatorRead('Date', 'BDPicker_submenu_xpath')).click()
        time.sleep(10)

    def click_first_date_field(self):
        for tab in range(1, 21):
            mouseaction.send_keys(Keys.TAB)
        # finally execute the all keyboard action perfromed
        mouseaction.perform()

    def month_select(self):
        driver.find_element_by_xpath("//div[@class='datepicker-days']/table/thead/tr[2]/th[2]").click()
        driver.find_element_by_xpath("//div[@class='datepicker-months']/table/tbody/tr/td/span[text()='Mar']").click()

    def date_select(self):
        dates = driver.find_elements(By.XPATH, "//div[@class='datepicker-days']/table/tbody/tr/td")
        for dayo in dates:
            if 31 == int(dayo.text):
                dayo.click()
                break
        time.sleep(5)


    def enter_current_date_in_second_field_section1(self):
        day = datetime.date.today().day
        month = datetime.date.today().month
        year = datetime.date.today().year
        driver.find_element_by_xpath("//div[@id='sandbox-container2']/div[@id='datepicker']/input[1]").send_keys(str(day) + "/" + str(month) + "/" + str(year))

    def select_second_field_section2(self):
        driver.find_element_by_xpath("//div[@id='sandbox-container2']/div[@id='datepicker']/input[2]").click()
    def clear_second_field_section1_value(self):
        driver.find_element_by_xpath("//div[@id='sandbox-container2']/div[@id='datepicker']/input[1]").clear()

    def select_16day_gap_date_value(self):
        day = datetime.date.today().day
        month = datetime.date.today().month
        year = datetime.date.today().year
        gap = 16

        if day - gap >= 1:
            final_start_date = day - gap
            final_month = month
            final_year = year
        else:
            final_start_date = (day - gap) + 30
            if (month >= 2):
                final_month = month - 1
                final_year = year
            else:
                final_month = (month - 1) + 12
                final_year = year - 1

        driver.find_element_by_xpath("//div[@id='sandbox-container2']/div[@id='datepicker']/input[1]").send_keys(
            str(final_start_date) + "/" + str(final_month) + "/" + str(final_year))
        time.sleep(6)

