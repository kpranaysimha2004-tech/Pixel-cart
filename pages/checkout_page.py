# checkout_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # Checkout / Cart Page Locators
        self.cart_link = (By.ID, "cartur")
        self.place_order_btn = (By.XPATH, "//button[text()='Place Order']")
        self.name_input = (By.ID, "name")
        self.country_input = (By.ID, "country")
        self.city_input = (By.ID, "city")
        self.card_input = (By.ID, "card")
        self.month_input = (By.ID, "month")
        self.year_input = (By.ID, "year")
        self.purchase_btn = (By.XPATH, "//button[text()='Purchase']")
        self.confirm_message = (By.CLASS_NAME, "sweet-alert")

    def open_checkout_page(self):
        """
        Opens Demoblaze homepage using BasePage method
        and navigates to Cart page.
        """
        self.open_url()   # inherited from BasePage
        self.driver.find_element(*self.cart_link).click()

    def click_place_order(self):
        """Clicks on Place Order button."""
        self.driver.find_element(*self.place_order_btn).click()

    def enter_checkout_details(
        self,
        name,
        country,
        city,
        card,
        month,
        year
    ):
        """Fills checkout form details."""

        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.country_input).send_keys(country)
        self.driver.find_element(*self.city_input).send_keys(city)
        self.driver.find_element(*self.card_input).send_keys(card)
        self.driver.find_element(*self.month_input).send_keys(month)
        self.driver.find_element(*self.year_input).send_keys(year)

    def confirm_purchase(self):
        """Clicks Purchase button."""
        self.driver.find_element(*self.purchase_btn).click()

    def is_order_successful(self):
        """Verifies order confirmation popup is displayed."""
        return self.driver.find_element(*self.confirm_message).is_displayed()