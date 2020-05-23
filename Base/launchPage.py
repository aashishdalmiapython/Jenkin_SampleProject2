from Libraries import configRead

def click_menu(driver,section,key):
    driver.find_element_by_xpath(configRead.locatorRead(section,key)).click()


def click_submenu(driver,section,key):
    driver.find_element_by_xpath(configRead.locatorRead(section,key)).click()