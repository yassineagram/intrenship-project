from behave import given
from pages.Base_page import BasePage

@given('I navigate to: {url}')
def navigate_to(context, url):
    context.base_page.open_url(url)

