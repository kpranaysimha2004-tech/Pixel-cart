from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):

    login_link = (By.ID, "login2")
    username_box = (By.ID, "loginusername")
    password_box = (By.ID, "loginpassword")
    login_button = (By.XPATH, "//button[text()='Log in']")
    user_name = (By.ID, "nameofuser")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def open_login_page(self):
        self.open_url()

    def click_login_link(self):
        self.wait.until(EC.element_to_be_clickable(self.login_link)).click()

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.username_box)).clear()
        self.driver.find_element(*self.username_box).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password_box)).clear()
        self.driver.find_element(*self.password_box).send_keys(password)

    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def verify_login(self):
        return self.wait.until(EC.visibility_of_element_located(self.user_name)).is_displayed()