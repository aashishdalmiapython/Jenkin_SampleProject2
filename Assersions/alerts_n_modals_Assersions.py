from selenium import webdriver
from Libraries import configRead

def assert_alerts_menu_title(driver):
    alert_menu_name = driver.find_element_by_xpath(configRead.locatorRead("Alerts","alerts_modal_Menu_xpath")).text
    alert_menu_name = alert_menu_name.strip()
    assert alert_menu_name == configRead.locatorRead("Alerts","alert_menu_name")

def assert_window_popup_modal_title(driver):
    window_popup_menu_name = driver.find_element_by_xpath(configRead.locatorRead("Alerts","window_popup_modal_SubMenu_xpath")).text
    window_popup_menu_name = window_popup_menu_name.strip()
    assert window_popup_menu_name == configRead.locatorRead("Alerts","window_popup_modal_SubMenu_name")


def assert_facebook_title(driver):
    win_title = driver.title
    assert win_title == configRead.locatorRead("Alerts_window_popup_modal", "Facebook_title")
