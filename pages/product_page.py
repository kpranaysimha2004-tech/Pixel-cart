from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProductPage(BasePage):

    phones_category = (By.LINK_TEXT, "Phones")
    laptops_category = (By.LINK_TEXT, "Laptops")
    monitors_category = (By.LINK_TEXT, "Monitors")
    product_cards = (By.CSS_SELECTOR, "div.card-block")
    product_titles = (By.CSS_SELECTOR, "div.card-block h4 a")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        self.open_url()

    def click_phones_category(self):
        self.wait.until(
            EC.element_to_be_clickable(self.phones_category)
        ).click()

    def click_laptops_category(self):
        self.wait.until(
            EC.element_to_be_clickable(self.laptops_category)
        ).click()

    def click_monitors_category(self):
        self.wait.until(
            EC.element_to_be_clickable(self.monitors_category)
        ).click()

    def get_product_titles(self):
        elements = self.wait.until(
            EC.presence_of_all_elements_located(self.product_titles)
        )
        return [element.text for element in elements]

    def get_product_count(self):
        products = self.wait.until(
            EC.presence_of_all_elements_located(self.product_cards)
        )
        return len(products)

    def is_products_displayed(self):
        try:
            products = self.wait.until(
                EC.presence_of_all_elements_located(self.product_cards)
            )
            return len(products) > 0
        except Exception:
            return False