from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')
driver.find_element(By.CSS_SELECTOR, '.a-spacing-small')
driver.find_element(By.CSS_SELECTOR, 'input#ap_customer_name')
driver.find_element(By.CSS_SELECTOR, '#ap_email')
driver.find_element(By.CSS_SELECTOR, 'input#ap_password')
driver.find_element(By.CSS_SELECTOR, 'input#ap_password_check')
driver.find_element(By.CSS_SELECTOR, "[name='metadata1']")
driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='condition']")
driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='privacy']")
driver.find_element(By.CSS_SELECTOR, "[name='metadata1']")