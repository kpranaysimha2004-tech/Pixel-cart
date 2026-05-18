from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    first_product = (By.XPATH, "//a[contains(text(),'Samsung galaxy s6')]")
    add_to_cart = (By.XPATH, "//a[text()='Add to cart']")
    cart_button = (By.ID, "cartur")
    delete_button = (By.XPATH, "//a[text()='Delete']")

    def __init__(self, driver):
        super().__init__(driver)

    def open_cart_page(self):
        self.open_url()

    def select_product(self):
        self.driver.find_element(*self.first_product).click()

    def click_add_to_cart(self):
        self.driver.find_element(*self.add_to_cart).click()

    def open_cart(self):
        self.driver.find_element(*self.cart_button).click()

    def remove_product(self):
        self.driver.find_element(*self.delete_button).click()