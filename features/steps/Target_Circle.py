from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



Target_Circle = (By.CSS_SELECTOR, "[data-test='@web/GlobalHeader/UtilityHeader/TargetCircle']")
HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
Benefit_Boxes= (By.CSS_SELECTOR, "[class*='styles__BenefitCardImageContainer-sc-9mx6dj-5 cWWIOF']")



@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get("http://www.target.com/")


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*Target_Circle).click()


@then('Target Circle are shown')
def verify_header(context):
    header = context.driver.find_element(*HEADER)
    context.driver.find_element(*HEADER)


@then('Verify Target Circle has {expected_amount} links')
def verify_Target_Circle_links(context, expected_amount):
    expected_amount = int(expected_amount)
    header_links = context.driver.find_elements(*Benefit_Boxes)
    assert len(header_links) == expected_amount, f'Expected {expected_amount} links, but got {len(header_links)}'


