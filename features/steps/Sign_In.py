
from selenium.webdriver.common.by import By
from behave import given, when, then




@given('Open Target main page')
def open_target_main_page(context):
    context.app.target_homepage.open()

@when('Click Sign In')
def click_sign_in(context):
    context.app.target_homepage.click_sign_in()

@when('From right side click Sign In')
def click_sign_in_from_right_side(context):
    context.app.target_homepage.click_sign_in_from_right_side()

@then('Verify Sign In form opened')
def verify_sign_in_form_opened(context):
    context.app.target_signin_page.verify_sign_in_form_opened()
