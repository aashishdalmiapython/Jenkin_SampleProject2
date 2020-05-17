

class simpleformClass():
    def __init__(self, obj):
        global driver
        driver = obj

    def input_form_link_click(self):
        driver.find_element_by_xpath("//a[contains(text(),'Input Forms')]").click()


    def simple_form__demo_link_click(self):
        driver.find_element_by_xpath("//a[contains(text(),'Simple Form')]").click()


    def get_form_1_title(self):
        form1_title = driver.find_element_by_xpath("//form[@id='get-input']/parent::div/preceding-sibling::div").text
        return form1_title

    def get_form2_title(self):
        for2title = driver.find_element_by_xpath("//form[@id='gettotal']/parent::div/parent::div/div[1]").text
        return for2title

    def enter_form2_field1_value(self,a):
        driver.find_element_by_xpath("//form[@id='gettotal']/div[1]/input[@id='sum1']").send_keys(a)

    def enter_form2_field2_value(self,b):
        driver.find_element_by_xpath("//form[@id='gettotal']/div[2]/input[@id='sum2']").send_keys(b)

    def click__form2_get_result_button(self):
        driver.find_element_by_xpath("//form[@id='gettotal']/button").click()

    def check_form2_result(self):
        result = driver.find_element_by_xpath("//form[@id='gettotal']/following-sibling::div/span").text
        return result



