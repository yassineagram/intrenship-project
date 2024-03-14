from pages.Base_page import BasePage
from pages.Main_page import MainPage
from pages.Sign_In import SignIn



class Application:

    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.main_page = MainPage(driver)
        self.sign_in_page = SignIn(driver)



