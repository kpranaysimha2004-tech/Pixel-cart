from selenium.webdriver.common.by import By

class ContactPage:

    def __init__(self, driver):
        self.driver = driver

    def click_contact_link(self):
        self.driver.find_element(By.LINK_TEXT, "Contact").click()

    def enter_contact_email(self, email):
        self.driver.find_element(By.ID, "recipient-email").send_keys(email)

    def enter_contact_name(self, name):
        self.driver.find_element(By.ID, "recipient-name").send_keys(name)

    def enter_message(self, message):
        self.driver.find_element(By.ID, "message-text").send_keys(message)

    def click_send_message(self):
        self.driver.find_element(By.XPATH, "//button[text()='Send message']").click()