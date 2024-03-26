class SignInPage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def input_username(self, username):

        username_input = self.driver.find_element_by_id("username")
        username_input.clear()
        username_input.send_keys(username)

    def input_password(self, password):

        password_input = self.driver.find_element_by_id("password")
        password_input.clear()
        password_input.send_keys(password)

    def click_continue_button(self):

        continue_button = self.driver.find_element_by_xpath("//button[@id='continue']")
        continue_button.click()

