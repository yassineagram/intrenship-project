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


driver.find_element(By.XPATH, "//class[@aria-label='Amazon']")
driver.find_element(By.XPATH, "//input[@name='metadat1']")
driver.find_element(By.XPATH, "//input[@aria-labelledby='continue-announce']")
driver.find_element(By.XPATH, "//div[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")
driver.find_element(By.XPATH, "//div[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
driver.find_element(By.XPATH, "//div[@class='a-link-normal']")
driver.find_element(By.XPATH, "//div[@href='/gp/help/customer/account-issues/ref=ap_login_with_otp_claim_collection?ie=UTF8']")
driver.find_element(By.XPATH, "//span[@id='createAccountSubmit']")







