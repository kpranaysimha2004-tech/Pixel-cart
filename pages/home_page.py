from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Import your BasePage
from base_page import BasePage 

# 2. Inherit BasePage by passing it into the class
class HomePage(BasePage):
    
    def click_phones_category(self):
        phones_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Phones']"))
        )
        phones_link.click()

    def click_laptops_category(self):
        laptops_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Laptops']"))
        )
        laptops_link.click()
        
    def click_monitors_category(self):
        # Adding the Monitors category using the exact same explicit wait pattern
        monitors_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Monitors']"))
        )
        monitors_link.click()
        
    def click_product(self, product_name):
        product_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[text()='{product_name}']"))
        )
        product_link.click()