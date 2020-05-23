from Pages import alert_n_modals_Page
from Assersions import alerts_n_modals_Assersions

def test_18_TC_verify_alert_menu_title(startbrowser):
    driver = startbrowser[0]
    wait = startbrowser[1]
    alerts = alert_n_modals_Page.Alert_and_modals_Class(driver,wait)
    alerts.click_Alerts_Menu()
    alerts_n_modals_Assersions.assert_alerts_menu_title(driver)


def test_19_TC_verify_Window_Popup_Modal_menu_title_n_click(startbrowser):
    driver = startbrowser[0]
    wait = startbrowser[1]
    window_popup_modal = alert_n_modals_Page.Alert_and_modals_Class(driver,wait)
    alerts_n_modals_Assersions.assert_window_popup_modal_title(driver)
    window_popup_modal.click_window_popup_modal_SubMenu()

def test_20_verify_single_window_open_for_facebook(startbrowser):
    driver = startbrowser[0]
    wait = startbrowser[1]
    facebookwindow = alert_n_modals_Page.Alert_and_modals_Class(driver,wait)
    facebookwindow.click_facebook_like_button()
    facebookwindow.switch_to_facebook_window()


