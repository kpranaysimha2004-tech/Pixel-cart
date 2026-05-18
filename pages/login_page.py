from selenium.webdriver.common.by import By


class LoginPage:

    login_link = (By.ID, "login2")
    username_box = (By.ID, "loginusername")
    password_box = (By.ID, "loginpassword")
    login_button = (By.XPATH, "//button[text()='Log in']")
    user_name = (By.ID, "nameofuser")

    def __init__(self, driver):
        self.driver = driver

    def click_login_link(self):
        self.driver.find_element(*self.login_link).click()

    def enter_username(self, username):
        self.driver.find_element(*self.username_box).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_box).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def verify_login(self):
        return self.driver.find_element(*self.user_name).is_displayed()