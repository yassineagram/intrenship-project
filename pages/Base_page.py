from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
url = "https://soft.reelly.io/"
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    def click_element(self, by, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((by, locator))
        )
        element.click()

    def input_text(self, by, locator, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((by, locator))
        )
        element.send_keys(text)


