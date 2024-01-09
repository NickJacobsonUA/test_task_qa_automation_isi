import datetime
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://test-hg.isi-technology.com/#!/login")
    driver.maximize_window()
    # Login
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="username"]')))
    login = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
    login.send_keys("automation-qa")
    password = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
    password.send_keys("automationQAtest")
    accept_terms = driver.find_element(By.CSS_SELECTOR, 'input[name="accept_terms_and_conditions"]')
    accept_terms.click()
    button = driver.find_element(By.CSS_SELECTOR, 'button[class="login-button btn btn-default btn-block btn-lg mb15 ng-binding ng-scope"]')
    button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body[class="isi-dark-theme"]')))
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f'{datetime.datetime},', attachment_type=allure.attachment_type.PNG)
    yield driver
    driver.quit()