from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:

    URL = "https://shophub-commerce.vercel.app/login"

    def __init__(self, driver : WebDriver):
        self.driver = driver
        self.email = (By.ID, "email")
        self.password = (By.ID, "password")
        self.loginbutton = (By.CSS_SELECTOR, ".space-y-4 > .inline-flex")

    def load(self):
        self.driver.get(self.URL)

    def Login(self,email, password):
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.loginbutton).click()

    def get_password_error_message(self):
        password_element = self.driver.find_element(*self.password)
        return password_element.get_attribute("validationMessage")