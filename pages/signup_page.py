from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SignupPage(BasePage):

    signup_link     = (By.ID, "signin2")
    username_field  = (By.ID, "sign-username")
    password_field  = (By.ID, "sign-password")
    signup_btn      = (By.XPATH, "//button[text()='Sign up']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.open_url()

    def click_signup_link(self):
        self.wait.until(
            EC.element_to_be_clickable(self.signup_link)
        ).click()

    def enter_username(self, username):
        self.wait.until(
            EC.visibility_of_element_located(self.username_field)
        ).send_keys(username)

    def enter_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located(self.password_field)
        ).send_keys(password)

    def click_signup_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.signup_btn)
        ).click()

    def is_signup_successful(self):
        try:
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return "sign up successfully" in alert_text.lower()
        except:
            return False