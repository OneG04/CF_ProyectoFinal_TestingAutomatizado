import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


class CartPage:
    URL = "https://shophub-commerce.vercel.app/cart"

    def __init__(self, driver : WebDriver):
        self.driver = driver
        self.cartTittle =  (By.CSS_SELECTOR, ".text-3xl.font-bold.mb-8")
        self.emptycart = (By.CSS_SELECTOR, ".text-3xl.font-bold.mb-4")
        self.deleteButton =  (By.CSS_SELECTOR, ".text-right >.inline-flex")
        self.overlay = (By.CSS_SELECTOR, "div.fixed.inset-0.z-50")
        self.continueshopping = (By.CSS_SELECTOR, '[href="/"] > .inline-flex')
        self.checkoutbutton = (By.CSS_SELECTOR, '[href="/checkout"] > .inline-flex')

    def load(self):
        self.driver.get(self.URL)

    def deleteObj(self):
        wait = WebDriverWait(self.driver, 10)

        try:
            # Espera a que el overlay desaparezca
            wait.until(EC.invisibility_of_element_located(self.overlay))
        except TimeoutException:
            print("Overlay no desapareció, intentando igualmente...")

        time.sleep(1)  # 👈 pausa explícita de 1 segundo por seguridad

        try:
            # Intentar clic normal
            button = wait.until(EC.element_to_be_clickable(self.deleteButton))
            button.click()
        except ElementClickInterceptedException:
            print("Overlay bloqueó el botón, usando JavaScript click")
            button = self.driver.find_element(*self.deleteButton)
            self.driver.execute_script("arguments[0].click();", button)

    def waitCart(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.cartTittle))

    def emptyCart(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.emptycart))

    def continueshop(self):
        wait = WebDriverWait(self.driver, 10)

        try:
            # Espera a que el overlay desaparezca
            wait.until(EC.invisibility_of_element_located(self.overlay))
        except TimeoutException:
            print("Overlay no desapareció, intentando igualmente...")

        time.sleep(1)  # 👈 pausa explícita de 1 segundo por seguridad

        try:
            # Intentar clic normal
            button = wait.until(EC.element_to_be_clickable(self.continueshopping))
            button.click()
        except ElementClickInterceptedException:
            print("Overlay bloqueó el botón, usando JavaScript click")
            button = self.driver.find_element(*self.continueshopping)
            self.driver.execute_script("arguments[0].click();", button)

    def checkout(self):
        wait = WebDriverWait(self.driver, 10)

        try:
            # Espera a que el overlay desaparezca
            wait.until(EC.invisibility_of_element_located(self.overlay))
        except TimeoutException:
            print("Overlay no desapareció, intentando igualmente...")

        time.sleep(1)  # 👈 pausa explícita de 1 segundo por seguridad

        try:
            # Intentar clic normal
            button = wait.until(EC.element_to_be_clickable(self.checkoutbutton))
            button.click()
        except ElementClickInterceptedException:
            print("Overlay bloqueó el botón, usando JavaScript click")
            button = self.driver.find_element(*self.checkoutbutton)
            self.driver.execute_script("arguments[0].click();", button)


