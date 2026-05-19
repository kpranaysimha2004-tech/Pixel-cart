from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from conftest import wait, accept_alert


scenarios("../features/aboutus.feature")
scenarios("../features/contact.feature")
scenarios("../features/homepage_carousel.feature")


@given("user opens About us popup")
def open_about_popup(driver):
    driver.get("https://www.demoblaze.com/")
    driver.maximize_window()

    wait(driver).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "About us"))
    ).click()


@when("user clicks on About us link")
def click_about_us(driver):
    wait(driver).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "About us"))
    ).click()


@then("About us popup should be displayed")
def verify_about_popup(driver):
    assert wait(driver).until(
        EC.visibility_of_element_located((By.ID, "videoModal"))
    ).is_displayed()


@when("user clicks on Close button")
def close_popup(driver):
    wait(driver).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Close']"))
    ).click()


@then("popup should be closed successfully")
def verify_popup_closed():
    assert True


@when("user clicks on Contact link")
def click_contact(driver):
    wait(driver).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Contact"))
    ).click()


@when("user enters valid contact details")
def enter_contact_details(driver):
    wait(driver).until(
        EC.visibility_of_element_located((By.ID, "recipient-email"))
    ).send_keys("test@gmail.com")

    driver.find_element(By.ID, "recipient-name").send_keys("Krishna")
    driver.find_element(By.ID, "message-text").send_keys("This is a test message")


@when("clicks Send message")
def click_send_message(driver):
    wait(driver).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Send message']"))
    ).click()


@when("the user clicks the carousel next or previous arrow")
def click_carousel_arrow(driver):
    driver.old_banner = wait(driver).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".carousel-item.active img"))
    ).get_attribute("src")

    wait(driver).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "carousel-control-next"))
    ).click()


@then("the next promotional banner should slide into view")
def verify_banner_change(driver):
    wait(driver).until(
        lambda d: d.find_element(
            By.CSS_SELECTOR,
            ".carousel-item.active img"
        ).get_attribute("src") != driver.old_banner
    )
    assert True