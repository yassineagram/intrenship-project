from behave import given, when
from pages.Sign_In import SignIn

@given('I am on the sign-in page')
def open_sign_in_page(context):
    context.sign_in_page = SignIn(context.driver)
    context.sign_in_page.open_sign_in_page()

@when('I enter my username as "{username}"')
def input_username(context, username):
    context.sign_in_page.input_username(username)

@when('I enter my password as "{password}"')
def input_password(context, password):
    context.sign_in_page.input_password(password)

@when('I click on the Continue button')
def click_continue_button(context):
    context.sign_in_page.click_continue_button()
