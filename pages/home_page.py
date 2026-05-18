from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        self.open_url()

    def click_phones_category(self):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Phones']"))
        ).click()

    def click_laptops_category(self):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Laptops']"))
        ).click()

    def click_monitors_category(self):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Monitors']"))
        ).click()

    def click_product(self, product_name):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//a[text()='{product_name}']"))
        ).click()