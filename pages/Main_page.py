
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open_off_plan(self):
        off_plan_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Off Plan')]"))
        )
        off_plan_link.click()





