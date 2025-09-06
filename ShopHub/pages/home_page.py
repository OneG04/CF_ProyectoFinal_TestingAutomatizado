from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class HomePage:
    URL = "https://shophub-commerce.vercel.app/"

    def __init__(self, driver : WebDriver):
        self.driver = driver
        self.singupbutton = (By.XPATH, "//button[text()='Sign Up']")
        self.dealsbutton = (By.CSS_SELECTOR, ":nth-child(3) > .flex > a > .inline-flex")

    def load(self):
        self.driver.get(self.URL)

    def go_deals(self):
        self.driver.find_element(*self.dealsbutton).click()