from Base import launchPage
from Base import page_actions
from Libraries import configRead
from Assersions import alerts_n_modals_Assersions
import time

class Alert_and_modals_Class():

    def __init__(self, objdriver, objwait):
        global driver
        global wait
        driver = objdriver
        wait= objwait

    def click_Alerts_Menu(self):
        launchPage.click_menu(driver,"Alerts","alerts_modal_Menu_xpath")

    def click_window_popup_modal_SubMenu(self):
        launchPage.click_submenu(driver,"Alerts","window_popup_modal_SubMenu_xpath")

    def click_facebook_like_button(self):
        page_actions.click_button_with_Wait(driver,wait,"Alerts_window_popup_modal","Facebook_Like_button_xpath")

    def switch_to_facebook_window(self):
        windows = page_actions.get_all_open_windows(driver)
        abc = driver.current_window_handle
        for win in windows:
            driver.switch_to.window(win)
            if str(driver.current_url) == str(configRead.locatorRead("Alerts_window_popup_modal","Facebook_url")):
                alerts_n_modals_Assersions.assert_facebook_title(driver)
        driver.switch_to.window(abc)
        driver.close()




