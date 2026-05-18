from selenium.webdriver.common.by import By

class ProductCategoryPage:

    def __init__(self, driver):
        self.driver = driver

    def click_phones_category(self):
        self.driver.find_element(By.LINK_TEXT, "Phones").click()

    def click_laptops_category(self):
        self.driver.find_element(By.LINK_TEXT, "Laptops").click()

    def click_monitors_category(self):
        self.driver.find_element(By.LINK_TEXT, "Monitors").click()

    def get_product_titles(self):
        products = self.driver.find_elements(By.CLASS_NAME, "hrefch")
        return [product.text for product in products]