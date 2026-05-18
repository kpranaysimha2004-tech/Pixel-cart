from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):

    first_product = (By.XPATH, "//a[contains(text(),'Samsung galaxy s6')]")
    add_to_cart = (By.XPATH, "//a[text()='Add to cart']")
    cart_button = (By.ID, "cartur")
    delete_button = (By.XPATH, "//a[text()='Delete']")
    product_in_cart = (By.XPATH, "//td[text()='Samsung galaxy s6']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def open_cart_page(self):
        self.open_url()

    def select_product(self):
        self.wait.until(EC.element_to_be_clickable(self.first_product)).click()

    def click_add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.add_to_cart)).click()

    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_button)).click()

    def remove_product(self):
        self.wait.until(EC.element_to_be_clickable(self.delete_button)).click()

    def verify_product_in_cart(self):
        return self.wait.until(EC.visibility_of_element_located(self.product_in_cart)).is_displayed()