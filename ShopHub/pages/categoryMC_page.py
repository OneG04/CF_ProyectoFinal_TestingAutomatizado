from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CategoryMC:

    URLMC = "https://shophub-commerce.vercel.app/categories/men-clothes"
    URLEL = "https://shophub-commerce.vercel.app/categories/electronics"

    def __init__(self, driver : WebDriver):
        self.driver = driver
        self.cartbutton = (By.CSS_SELECTOR, "a[href*='cart']")
        self.prod2button = (By.ID, "add-to-cart-2")

    def loadMC(self):
        self.driver.get(self.URLMC)

    def loadEL(self):
        self.driver.get(self.URLEL)

    def pagemc(self):
        self.driver.find_element(*self.prod2button).click()

    def gocart(self):
        self.driver.find_element(*self.cartbutton).click()