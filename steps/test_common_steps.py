import random
import string

from pytest_bdd import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from conftest import wait, accept_alert


@given("user opens the Demoblaze website")
@given("the user is on the Demoblaze homepage")
@given("user is on the Demoblaze home page")
@given("user is on Demoblaze homepage")
def open_demoblaze(driver):
    HomePage(driver).open()


def generate_random_credentials():
    username = "user_" + "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    password = "Pass" + "".join(random.choices(string.ascii_letters + string.digits, k=8))
    return username, password


def register_test_user(driver):
    page = SignupPage(driver)
    page.open()
    page.click_signup_link()
    username, password = generate_random_credentials()
    driver.test_username = username
    driver.test_password = password
    page.enter_username(username)
    page.enter_password(password)
    page.click_signup_button()
    message = accept_alert(driver)
    assert message != ""
    return username, password


@given("user is logged in to Demoblaze")
def user_is_logged_in(driver):
    if not getattr(driver, "test_username", None):
        register_test_user(driver)

    page = LoginPage(driver)
    page.open_login_page()
    page.click_login_link()
    page.enter_username(driver.test_username)
    page.enter_password(driver.test_password)
    page.click_login_button()
    assert page.verify_login()


@given("user adds a product to the cart")
@when("user adds a product to the cart")
def add_product_to_cart(driver):
    HomePage(driver).open()
    cart_page = CartPage(driver)
    cart_page.select_product()
    cart_page.click_add_to_cart()
    accept_alert(driver)


@given("user opens the cart page")
@when("user opens the cart page")
@when("user clicks on Cart option")
@when("user navigates to cart page")
@when("the user views the Cart page")
def open_cart(driver):
    CartPage(driver).open_cart()


@then("success alert should be displayed")
@then("a success alert should appear")
def verify_success_alert(driver):
    message = accept_alert(driver)
    assert message != ""


@then("user should see validation message")
@then("user should see a validation message")
def verify_validation_message(driver):
    message = accept_alert(driver)
    assert message != ""


@then("product details page should open")
def verify_product_details_open(driver):
    assert wait(driver).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "name"))
    ).is_displayed()
