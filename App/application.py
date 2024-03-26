from pages.Base_page import BasePage
from pages.Main_page import MainPage
from pages.Sign_in import SignInPage
from selenium import webdriver
class Application:
    def __init__(self, driver):
        self.Base_page = BasePage(driver)
        self.Main_page = MainPage(driver)
        self.sign_in_page = SignInPage(driver)







