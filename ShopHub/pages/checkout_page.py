from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time

class Checkout:

    URL = "https://shophub-commerce.vercel.app/checkout"

    def __init__(self, driver : WebDriver):
        self.driver = driver
        self.firstname = (By.ID, "firstName")
        self.lastname = (By.ID, "lastName")
        self.email = (By.ID, "email")
        self.phone = (By.ID, "phone")
        self.direccion = (By.ID, "address")
        self.ciudad = (By.ID, "city")
        self.zipcode = (By.ID, "zipCode")
        self.pais = (By.ID, "country")
        self.placeorderbutton = (By.ID, "place-order-button")
        self.overlay = (By.CSS_SELECTOR, "div.fixed.inset-0.z-50")

    def load(self):
        self.driver.get(self.URL)

    def customerInfo(self,firstname, lastname, email, phone, direccion, ciudad, zipcode, pais):
        self.driver.find_element(*self.firstname).send_keys(firstname)
        self.driver.find_element(*self.lastname).send_keys(lastname)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.phone).send_keys(phone)
        self.driver.find_element(*self.direccion).send_keys(direccion)
        self.driver.find_element(*self.ciudad).send_keys(ciudad)
        self.driver.find_element(*self.zipcode).send_keys(zipcode)
        self.driver.find_element(*self.pais).send_keys(pais)

        wait = WebDriverWait(self.driver, 10)

        try:
            # Esperar a que el overlay desaparezca
            wait.until(EC.invisibility_of_element_located(self.overlay))
        except TimeoutException:
            print("⚠️ Overlay no desapareció a tiempo, intentando igualmente...")

        time.sleep(1)  # 👈 darle un respiro extra

        try:
            # Intentar clic normal
            button = wait.until(EC.element_to_be_clickable(self.placeorderbutton))
            button.click()
        except ElementClickInterceptedException:
            print("⚠️ Usando JS click porque el overlay bloqueó el botón")
            button = self.driver.find_element(*self.placeorderbutton)
            self.driver.execute_script("arguments[0].click();", button)

    def get_phone_error_message(self):
        password_element = self.driver.find_element(*self.phone)
        return password_element.get_attribute("validationMessage")
