from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select
import datetime


class jQueryClass():

    def __init__(self,obj,objaction):
        global driver
        global mouseaction
        global wait
        driver = obj
        mouseaction = objaction


    def select_jQuery_date_menu(self):
        driver.find_element_by_xpath("//a[text()='JQuery Date Picker']").click()
    def select_jquery_date_field1(self):
        driver.find_element_by_xpath("//input[1]").click()

    def click_first_date_field(self):
        time.sleep(5)
        mouseaction.reset_actions()
        for tab in range(1, 21):
            mouseaction.send_keys(Keys.TAB)
        # finally execute the all keyboard action perfromed
        mouseaction.perform()

    def select_date_in_firstdate_field(self):
        month_dd = Select(driver.find_element_by_xpath(
            "//input[1]/parent::div/parent::div/parent::div/parent::div/parent::div/following-sibling::div/div/div/select"))
        month_dd.select_by_value("3")
        time.sleep(5)
        daterows = driver.find_elements_by_xpath(
            "//input[1]/parent::div/parent::div/parent::div/parent::div/parent::div/following-sibling::div/table/tbody/tr")
        datescolmn = driver.find_elements_by_xpath(
            "//input[1]/parent::div/parent::div/parent::div/parent::div/parent::div/following-sibling::div/table/tbody/tr[1]/td")
        for r in range(1, len(daterows)):
            for c in range(1, len(datescolmn)):
                date = driver.find_element_by_xpath(
                    "//input[1]/parent::div/parent::div/parent::div/parent::div/parent::div/following-sibling::div/table/tbody/tr[" + str(
                        r) + "]/td[" + str(c) + "]")
                # print(date.text)
                if date.text == "15":
                    date.click()
                    break
        time.sleep(5)

    def get_date(self):
        day = (datetime.date.today().day)
        month = (datetime.date.today().month)
        year = (datetime.date.today().year)
        date = (str(month) + "/" + str(day) + "/" + str(year))
        return date