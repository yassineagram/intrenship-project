from behave import given, when, then
from pages.Main_page import MainPage

@given('I navigate to: https://soft.reelly.io/')
def navigate_to_main_page(context):
    context.main_page = MainPage(context.driver)
    context.main_page.open_url('https://soft.reelly.io/')

@when('I click "off plan" button at the left side menu')
def click_off_plan_button(context):
    context.main_page.click_off_plan_button()

@then('I see URL contains text: off plan')
def verify_url_contains_off_plan(context):
    assert "off plan" in context.main_page.get_current_url(), "URL does not contain 'off plan'"

@when('I click on button: "filter" and filter by sale status of “Out of Stocks”')
def filter_by_out_of_stocks(context):
    context.main_page.filter_by_out_of_stocks()

@when('I click button "Apply filter"')
def click_apply_filter_button(context):
    context.main_page.click_apply_filter_button()

@then('I Verify each product contains the Out of Stocks tag')
def verify_out_of_stocks_tags(context):
    assert context.main_page.verify_out_of_stocks_tags(), "Not all products contain Out of Stocks tag"





