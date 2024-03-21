from behave import given
from pages.Sign_In import SignIn

# Define your step definitions related to Sign In page here
# For example:
@given('I navigate to sign in page')
def navigate_to_sign_in(context):
    context.sign_in_page.navigate_to_sign_in_page()

