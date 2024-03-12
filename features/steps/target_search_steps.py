from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_FIELD = (By.ID, 'search')
SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")


@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get("http://www.target.com/")


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_ICON).click()
    sleep(6)


@then('Search results for shoes are shown')
def verify_search_results_correct(context, expected_result):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_HEADER).text
    assert expected_result in actual_text, f'Expected word {expected_result} not in {actual_text}'







