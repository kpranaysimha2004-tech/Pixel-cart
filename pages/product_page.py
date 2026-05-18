from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProductCategoryPage(BasePage):

    # Locators
    PHONES_CATEGORY = (By.LINK_TEXT, "Phones")
    LAPTOPS_CATEGORY = (By.LINK_TEXT, "Laptops")
    MONITORS_CATEGORY = (By.LINK_TEXT, "Monitors")
    PRODUCT_CARDS = (By.CSS_SELECTOR, "div.card-block")
    PRODUCT_TITLES = (By.CSS_SELECTOR, "div.card-block h4 a")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        """Opens the Demoblaze homepage using base_page open_url."""
        self.open_url()

    def click_phones_category(self):
        """Clicks on Phones category."""
        wait = WebDriverWait(self.driver, 10)
        phones = wait.until(
            EC.element_to_be_clickable(self.PHONES_CATEGORY)
        )
        phones.click()

    def click_laptops_category(self):
        """Clicks on Laptops category."""
        wait = WebDriverWait(self.driver, 10)
        laptops = wait.until(
            EC.element_to_be_clickable(self.LAPTOPS_CATEGORY)
        )
        laptops.click()

    def click_monitors_category(self):
        """Clicks on Monitors category."""
        wait = WebDriverWait(self.driver, 10)
        monitors = wait.until(
            EC.element_to_be_clickable(self.MONITORS_CATEGORY)
        )
        monitors.click()

    def get_product_titles(self):
        """Returns list of all visible product titles."""
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_TITLES)
        )
        return [element.text for element in elements]

    def get_product_count(self):
        """Returns number of products displayed."""
        wait = WebDriverWait(self.driver, 10)
        products = wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_CARDS)
        )
        return len(products)

    def is_products_displayed(self):
        """Returns True if products are visible on page."""
        try:
            wait = WebDriverWait(self.driver, 10)
            elements = wait.until(
                EC.presence_of_all_elements_located(self.PRODUCT_CARDS)
            )
            return len(elements) > 0
        except:
            return False