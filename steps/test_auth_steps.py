from pytest_bdd import scenarios, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from conftest import wait, accept_alert
from .test_common_steps import *


scenarios("../features/login.feature")
scenarios("../features/logout.feature")
scenarios("../features/signup.feature")


@when("user clicks on login button")
def click_login_button(driver):
    LoginPage(driver).click_login_link()


@when("user enters valid username and password")
def enter_valid_login(driver):
    if not getattr(driver, "test_username", None):
        from .test_common_steps import register_test_user

        register_test_user(driver)

    page = LoginPage(driver)
    page.enter_username(driver.test_username)
    page.enter_password(driver.test_password)


@when("user enters invalid username and password")
def enter_invalid_login(driver):
    page = LoginPage(driver)
    page.enter_username("wronguser")
    page.enter_password("wrongpass")


@when("user leaves username and password empty")
def leave_login_empty(driver):
    pass


@when("user clicks on login submit button")
def submit_login(driver):
    LoginPage(driver).click_login_button()


@then("user should login successfully")
def verify_login(driver):
    assert LoginPage(driver).verify_login()


@then("user should see login error message")
def verify_login_error(driver):
    message = accept_alert(driver)
    assert message != ""


@when('user clicks on "Log out" in navbar')
def click_logout(driver):
    wait(driver).until(
        EC.element_to_be_clickable((By.ID, "logout2"))
    ).click()


@then('user should see "Log in" option in navbar')
def verify_login_option(driver):
    assert wait(driver).until(
        EC.visibility_of_element_located((By.ID, "login2"))
    ).is_displayed()


@then('user should not see "Log out" option')
def verify_logout_hidden(driver):
    logout = driver.find_element(By.ID, "logout2")
    assert logout.value_of_css_property("display") == "none"


@when("the user opens the Sign Up modal")
def open_signup_modal(driver):
    SignupPage(driver).click_signup_link()


@when(parsers.parse('the user enters a unique "{username}" and "{password}"'))
def enter_signup_details(driver, username, password):
    if username.startswith("<") and password.startswith("<"):
        from .test_common_steps import generate_random_credentials

        username, password = generate_random_credentials()

    driver.test_username = username
    driver.test_password = password

    page = SignupPage(driver)
    page.enter_username(username)
    page.enter_password(password)


@when("the user submits the registration form")
def submit_signup(driver):
    SignupPage(driver).click_signup_button()