from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.product_page import ProductPage
from conftest import wait


scenarios("../features/product_detail.feature")
scenarios("../features/product_navigation.feature")
scenarios("../features/productcategory.feature")
scenarios("../features/search.feature")


@when("user clicks on Phones category")
def click_phones(driver):
    ProductPage(driver).click_phones_category()


@when("user clicks on Laptops category")
def click_laptops(driver):
    ProductPage(driver).click_laptops_category()


@when("user clicks on Monitors category")
def click_monitors(driver):
    ProductPage(driver).click_monitors_category()


@then("only phone products should be displayed")
@then("all phone products should be displayed")
@then("only laptop products should be displayed")
@then("all laptop products should be displayed")
@then("only monitor products should be displayed")
@then("all monitor products should be displayed")
def verify_products_displayed(driver):
    assert ProductPage(driver).is_products_displayed()


@when("user selects a phone product")
def select_phone_product(driver):
    wait(driver).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Samsung galaxy s6']"))
    ).click()


@then("product details page should open")
@then("product details page should be displayed")
def verify_product_details_page(driver):
    assert wait(driver).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "name"))
    ).is_displayed()


@when('user clicks on "Samsung galaxy s6"')
@when("user clicks on a product image")
def click_samsung_product(driver):
    wait(driver).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Samsung galaxy s6']"))
    ).click()


@then("user should see product name")
def verify_product_name(driver):
    assert wait(driver).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "name"))
    ).is_displayed()


@then("user should see product price")
def verify_product_price(driver):
    assert wait(driver).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "price-container"))
    ).is_displayed()


@then("user should see product description")
def verify_product_description(driver):
    assert wait(driver).until(
        EC.visibility_of_element_located((By.ID, "more-information"))
    ).is_displayed()


@then('user should see "Add to cart" button')
def verify_add_cart_button(driver):
    assert wait(driver).until(
        EC.visibility_of_element_located((By.XPATH, "//a[text()='Add to cart']"))
    ).is_displayed()


@given("user is on product details page")
def user_on_product_page(driver):
    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()

    wait(driver).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Samsung galaxy s6']"))
    ).click()


@when("user clicks on Home button")
def click_home_button(driver):
    wait(driver).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Home ']"))
    ).click()


@then("user should navigate back to home page")
def verify_home_page(driver):
    assert wait(driver).until(
        EC.visibility_of_element_located((By.ID, "cat"))
    ).is_displayed()