from Base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):
    CART_HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")

    def open_main(self):
        self.open('https://www.target.com/')

    def click_cart_icon(self):
        self.wait_element_clickable_click(*self.CART_ICON)


    def verify_cart_empty_message(self):
            self.wait_element_visible(*self.CART_HEADER)
            self.verify_text('Your cart is empty', *self.CART_HEADER)

