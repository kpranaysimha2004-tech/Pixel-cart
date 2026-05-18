from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SignupPage(BasePage):

    signup_link     = (By.ID, "signin2")
    username_field  = (By.ID, "sign-username")
    password_field  = (By.ID, "sign-password")
    signup_btn      = (By.XPATH, "//button[text()='Sign up']")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.open_url()

    def click_signup_link(self):
        self.driver.find_element(*self.signup_link).click()

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_signup_button(self):
        self.driver.find_element(*self.signup_btn).click()

    def is_signup_successful(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return "sign up successfully" in alert_text.lower()
        except:
            return False