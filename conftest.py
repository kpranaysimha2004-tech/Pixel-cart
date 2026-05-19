import pytest
from pytest_bdd import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.cart_page import CartPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def wait(driver):
    return WebDriverWait(driver, 10)


def accept_alert(driver):
    alert = wait(driver).until(EC.alert_is_present())
    text = alert.text
    alert.accept()
    return text


@given("user opens the Demoblaze website")
@given("user is on the Demoblaze home page")
@given("user is on Demoblaze homepage")
@given("the user is on the Demoblaze homepage")
def open_demoblaze(driver):
    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()


@given("user adds a product to the cart")
def add_product_to_cart(driver):
    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()

    cart_page = CartPage(driver)
    cart_page.select_product()
    cart_page.click_add_to_cart()
    accept_alert(driver)


@when("user opens the cart page")
@when("user navigates to cart page")
@when("user clicks on Cart option")
@when("the user views the Cart page")
def open_cart_page(driver):
    CartPage(driver).open_cart()


@then("user should see validation message")
@then("user should see a validation message")
@then("validation message should be displayed")
def check_validation_alert(driver):
    message = accept_alert(driver)
    assert message != ""


@then("success alert should be displayed")
@then("a success alert should appear")
def check_success_alert(driver):
    message = accept_alert(driver)
    assert message != ""


@given("user is logged in to Demoblaze")
def user_logged_in(driver):
    page = LoginPage(driver)
    page.open_login_page()
    page.click_login_link()
    page.enter_username("testuser")
    page.enter_password("test123")
    page.click_login_button()