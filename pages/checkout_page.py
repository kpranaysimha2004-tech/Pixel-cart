

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, driver):

        # Inheriting BasePage
        super().__init__(driver)

        # Explicit Wait
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.cart_link = (By.ID, "cartur")
        self.place_order_button = (By.XPATH, "//button[text()='Place Order']")
        self.name = (By.ID, "name")
        self.country = (By.ID, "country")
        self.city = (By.ID, "city")
        self.card = (By.ID, "card")
        self.month = (By.ID, "month")
        self.year = (By.ID, "year")
        self.purchase_button = (By.XPATH, "//button[text()='Purchase']")

    def open_checkout(self):
        """
        Opens website using BasePage open_url()
        and navigates to Cart page
        """

        # Open Demoblaze URL
        self.open_url()

        # Wait and click Cart
        self.wait.until(
            EC.element_to_be_clickable(self.cart_link)
        ).click()

    def click_place_order(self):
        """Wait and click Place Order button"""

        self.wait.until(
            EC.element_to_be_clickable(self.place_order_button)
        ).click()

    def fill_checkout_form(
            self,
            customer_name,
            customer_country,
            customer_city,
            customer_card,
            customer_month,
            customer_year):

        """Wait and fill checkout form"""

        self.wait.until(
            EC.visibility_of_element_located(self.name)
        ).send_keys(customer_name)

        self.wait.until(
            EC.visibility_of_element_located(self.country)
        ).send_keys(customer_country)

        self.wait.until(
            EC.visibility_of_element_located(self.city)
        ).send_keys(customer_city)

        self.wait.until(
            EC.visibility_of_element_located(self.card)
        ).send_keys(customer_card)

        self.wait.until(
            EC.visibility_of_element_located(self.month)
        ).send_keys(customer_month)

        self.wait.until(
            EC.visibility_of_element_located(self.year)
        ).send_keys(customer_year)

    def complete_purchase(self):
        """Wait and click Purchase button"""

        self.wait.until(
            EC.element_to_be_clickable(self.purchase_button)
        ).click()