from behave import given
from pages.Base_page import BasePage

@given('I navigate to: {url}')
def navigate_to_url(context, url):
    context.base_page = BasePage(context.driver)
    context.base_page.open_url(url)


