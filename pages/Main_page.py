class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def click_off_plan_button(self):

        off_plan_button = self.driver.find_element_by_xpath("//button[@id='off_plan']")
        off_plan_button.click()

    def get_current_url(self):

        return self.driver.current_url

    def filter_by_out_of_stocks(self):

        filter_button = self.driver.find_element_by_xpath("//button[@id='filter']")
        filter_button.click()

    def click_apply_filter_button(self):

        apply_filter_button = self.driver.find_element_by_xpath("//button[@id='apply_filter']")
        apply_filter_button.click()

    def verify_out_of_stocks_tags(self):

        product_elements = self.driver.find_elements_by_class_name("product")
        for product_element in product_elements:
            if "Out of Stocks" not in product_element.text:
                return False
        return True
