from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SingupPage:

    URL = "https://shophub-commerce.vercel.app/signup"

    def __init__(self, driver : WebDriver):
        self.driver = driver
        self.firstname = (By.ID, "firstName")
        self.lastname = (By.ID, "lastName")
        self.email = (By.ID, "email")
        self.zipcode = (By.ID, "zipCode")
        self.password = (By.ID, "password")
        self.singupbutton = (By.CSS_SELECTOR, ".space-y-4 > .inline-flex")
        self.email_error = (By.XPATH, "//*[contains(text(), 'Incluye una') and contains(text(), '@')]")

    def load(self):
        self.driver.get(self.URL)

    def formulario(self, firstname, lastname, email, zipcode, password):
        self.driver.find_element(*self.firstname).send_keys(firstname)
        self.driver.find_element(*self.lastname).send_keys(lastname)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.zipcode).send_keys(zipcode)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.singupbutton).click()

    def get_email_error_message(self):
        email_element = self.driver.find_element(*self.email)
        return email_element.get_attribute("validationMessage")
