class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
    def open_url(self):
        """Navigates to the Demoblaze homepage and maximizes the window."""
        self.driver.get("https://www.demoblaze.com/")
        self.driver.maximize_window()