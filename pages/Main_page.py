
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

@given('I navigate to: https://soft.reelly.io/sign-in')
def navigate_to_sign_in(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://soft.reelly.io/sign-in")

@when('I input username: {username}')
def input_username(context, username):
    username_input = context.driver.find_element(By.ID, "username")
    username_input.send_keys(username)

@when('I input password: {password}')
def input_password(context, password):
    password_input = context.driver.find_element(By.ID, "password")
    password_input.send_keys(password)

@when('I click button: Continue')
def click_continue_button(context):
    continue_button = context.driver.find_element(By.ID, "continue-button")
    continue_button.click()

@when('I click "off plan” button at the left side menu')
def click_off_plan(context):
    off_plan_link = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Off Plan')]"))
    )
    off_plan_link.click()

@then('I see URL contains text: off plan')
def verify_url_contains_off_plan(context):
    assert "/off-plan" in context.driver.current_url, "URL does not contain 'off-plan'"

@when('I click on button: "filter" and filter by sale status of “Out of Stocks”')
def filter_by_out_of_stocks(context):
    sale_status_dropdown = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "sale-status-dropdown"))
    )
    sale_status_dropdown.click()

    out_of_stock_option = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//ul[@id='sale-status-options']/li[text()='Out of Stocks']"))
    )
    out_of_stock_option.click()

@then('I click button "Apply filter"')
def apply_filter(context):
    apply_filter_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "apply-filter-button"))
    )
    apply_filter_button.click()

@then('I verify each product contains the Out of Stocks tag')
def verify_out_of_stock_tags(context):
    products = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "product"))
    )
    assert verify_out_of_stock_tags(products), "Not all products contain the Out of Stocks tag"




