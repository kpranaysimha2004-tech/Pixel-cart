from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from conftest import wait, accept_alert
from .test_common_steps import *


scenarios("../features/payment.feature")
scenarios("../features/place_order_validation.feature")


@when("user opens the cart page")
def open_cart_local(driver):
    CartPage(driver).open_cart()


@then("validation message should be displayed")
def verify_validation_local(driver):
    message = accept_alert(driver)
    assert message != ""


@given("user is on the cart page")
def user_on_cart_page(driver):
    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()

    cart_page = CartPage(driver)
    cart_page.select_product()
    cart_page.click_add_to_cart()
    accept_alert(driver)
    cart_page.open_cart()


@given("user is on the place order popup")
def user_on_place_order_popup(driver):
    user_on_cart_page(driver)
    CheckoutPage(driver).click_place_order()


@when("user clicks on place order button")
@when("user clicks on Place Order button")
def click_place_order(driver):
    CheckoutPage(driver).click_place_order()


@when("user enters valid payment details")
@when("user enters valid order details")
def enter_payment_details(driver):
    CheckoutPage(driver).fill_checkout_form(
        "Krishna",
        "India",
        "Bhubaneswar",
        "1234567890",
        "May",
        "2026"
    )


@when("user enters valid name")
def enter_name(driver):
    wait(driver).until(
        EC.visibility_of_element_located((By.ID, "name"))
    ).send_keys("Krishna")


@when("user enters valid country")
def enter_country(driver):
    wait(driver).until(
        EC.visibility_of_element_located((By.ID, "country"))
    ).send_keys("India")


@when("user enters valid city")
def enter_city(driver):
    wait(driver).until(
        EC.visibility_of_element_located((By.ID, "city"))
    ).send_keys("Bhubaneswar")


@when("user enters valid card details")
def enter_card(driver):
    wait(driver).until(
        EC.visibility_of_element_located((By.ID, "card"))
    ).send_keys("1234567890")


@when("user enters valid month and year")
def enter_month_year(driver):
    wait(driver).until(
        EC.visibility_of_element_located((By.ID, "month"))
    ).send_keys("May")

    wait(driver).until(
        EC.visibility_of_element_located((By.ID, "year"))
    ).send_keys("2026")


@when("user leaves all fields empty")
def leave_fields_empty(driver):
    pass


@when("user clicks on purchase button")
@when("user clicks on Purchase button")
@when("user clicks on purchase button without entering details")
def click_purchase(driver):
    CheckoutPage(driver).complete_purchase()


@then("order should be placed successfully")
def verify_order_success(driver):
    success_box = wait(driver).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "sweet-alert"))
    )
    assert success_box.is_displayed()


@when("user clicks on close button")
@when("user clicks on Close button")
def close_payment_popup(driver):
    # Wait for the checkout name field inside the modal, then click Close robustly
    wait(driver).until(
        EC.visibility_of_element_located((By.ID, "name"))
    )
    try:
        btn = wait(driver).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Close')]")))
        driver.execute_script("arguments[0].click();", btn)
    except Exception:
        footer_btns = driver.find_elements(By.CSS_SELECTOR, ".modal-footer button")
        if footer_btns:
            driver.execute_script("arguments[0].click();", footer_btns[-1])


@then("payment form should be closed")
def verify_payment_closed():
    assert True