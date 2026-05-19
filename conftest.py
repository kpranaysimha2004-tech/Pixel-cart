import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


def wait(driver):
    return WebDriverWait(driver, 10)


def accept_alert(driver):
    alert = wait(driver).until(EC.alert_is_present())
    text = alert.text
    alert.accept()
    return text