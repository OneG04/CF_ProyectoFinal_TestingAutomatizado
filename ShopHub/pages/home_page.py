from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    URL = "https://shophub-commerce.vercel.app/"

    def __init__(self, driver : WebDriver):
        self.driver = driver
        self.singupbutton = (By.XPATH, "//button[text()='Sign Up']")

    def gosingup(self):
        self.driver.find_element(*self.singupbutton).click()