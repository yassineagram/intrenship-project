
from selenium.webdriver.common.by import By
from behave import given, when, then
from pages.Sign_in import SignInPage

SIGN_IN = (By.CSS_SELECTOR, "[class='sing-in-text']")
EMAIL_FIELD = (By.ID, "email-2")
PASSWORD_FIELD = (By.ID, "field")
@given('I navigate to: https://soft.reelly.io/sign-in')
def navigate_to_sign_in_page(context):
    context.sign_in_page = SignInPage(context.driver)
    context.sign_in_page.open_url('https://soft.reelly.io/sign-in')

@when('I input username')
def input_username(context):
    context.sign_in_page.input_username('yassine.aitougram@gmail.com')

@when('I input password')
def input_password(context):
    context.sign_in_page.input_password('Yassine89*')

@when('I click button: Continue')
def click_continue_button(context):
    context.sign_in_page.click_continue_button()

@then('I verify page is displayed: Main Page')
def verify_main_page_displayed(context):
    assert 'main_page' in context.sign_in_page.get_current_url(), "Main Page is not displayed"

