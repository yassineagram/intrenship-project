

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def input_text(self, text, locator):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def wait_for_clickable_element_and_click(self, locator, ):
        element = WebDriverWait(self.driver).until(EC.element_to_be_clickable(locator))
        element.click()
