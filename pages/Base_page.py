
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TargetHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def open(self):
        self.driver.get("https://www.target.com")

    def click_sign_in_from_navigation(self):
        sign_in_nav_locator = (By.XPATH, "//button[@data-test='account']")
        self.wait.until(EC.element_to_be_clickable(sign_in_nav_locator)).click()

class TargetSignInPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def verify_sign_in_form_opened(self):
        sign_in_form_locator = (By.XPATH, "//form[@data-test='signinForm']")
        self.wait.until(EC.visibility_of_element_located(sign_in_form_locator))

