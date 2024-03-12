from pages.Base_page import  Page
from pages.Header import Header

class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.header = Header(driver)



