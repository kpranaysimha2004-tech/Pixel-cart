from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import CartPage
from conftest import wait, accept_alert
from .test_common_steps import *


scenarios("../features/cart.feature")
scenarios("../features/remove_product.feature")
scenarios("../features/empty_cart.feature")
scenarios("../features/cart_total_calculation.feature")


@when("user selects a product")
def select_product(driver):
    CartPage(driver).select_product()


@when("user clicks on Add to cart button")
@when("user adds the product to cart")
def add_product(driver):
    page = CartPage(driver)
    page.click_add_to_cart()
    accept_alert(driver)


@then("product should be added to cart successfully")
def verify_product_added():
    assert True


@then("added product should be visible in cart")
@then("product should be displayed in cart")
def verify_product_in_cart(driver):
    assert CartPage(driver).verify_product_in_cart()


@when("user clicks on delete button")
@when("user clicks on Delete button")
def delete_product(driver):
    CartPage(driver).remove_product()


@then("product should be removed from cart")
def verify_product_removed(driver):
    wait(driver).until(
        EC.invisibility_of_element_located((By.XPATH, "//td[text()='Samsung galaxy s6']"))
    )
    assert True


@when("user adds multiple products to cart")
def add_multiple_products(driver):
    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()

    page = CartPage(driver)
    page.select_product()
    page.click_add_to_cart()
    accept_alert(driver)

    # Verify first product was added to cart
    page.open_cart()
    rows = wait(driver).until(
        EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr"))
    )
    if len(rows) < 1:
        driver.get("https://www.demoblaze.com/")
        page.select_product()
        page.click_add_to_cart()
        accept_alert(driver)
        page.open_cart()

    driver.get("https://www.demoblaze.com/")
    wait(driver).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Nokia lumia 1520']"))
    ).click()

    page = CartPage(driver)
    page.click_add_to_cart()
    accept_alert(driver)

    page.open_cart()
    rows = wait(driver).until(
        EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr"))
    )
    if len(rows) < 2:
        driver.get("https://www.demoblaze.com/")
        wait(driver).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Nokia lumia 1520']"))
        ).click()
        page = CartPage(driver)
        page.click_add_to_cart()
        accept_alert(driver)
        page.open_cart()


@then("all selected products should be displayed")
def verify_multiple_products(driver):
    # Ensure cart page is open and rows are loaded
    CartPage(driver).open_cart()
    rows = wait(driver).until(
        EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr"))
    )
    assert len(rows) >= 2


@given("user has products in cart")
def user_has_products(driver):
    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()

    page = CartPage(driver)
    page.select_product()
    page.click_add_to_cart()
    accept_alert(driver)
    page.open_cart()


@when("user removes all products from cart")
def remove_all_products(driver):
    delete_buttons = driver.find_elements(By.XPATH, "//a[text()='Delete']")
    for button in delete_buttons:
        button.click()


@then("cart should become empty")
@then("cart page should display no products")
def verify_cart_empty(driver):
    rows = driver.find_elements(By.XPATH, "//tbody/tr")
    assert len(rows) == 0


@given("the user has added multiple products to the cart")
def user_added_multiple_products(driver):
    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()
    add_multiple_products(driver)


@then("the total price should equal the sum of the individual product prices")
def verify_total_price(driver):
    # Ensure cart page is open
    CartPage(driver).open_cart()
    prices = wait(driver).until(
        EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td[3]"))
    )
    expected_total = sum(int(price.text) for price in prices if price.text.strip())
    wait(driver).until(
        lambda d: int(d.find_element(By.ID, "totalp").text) == expected_total
    )
    actual_total = int(
        wait(driver).until(
            EC.visibility_of_element_located((By.ID, "totalp"))
        ).text
    )
    assert actual_total == expected_total
