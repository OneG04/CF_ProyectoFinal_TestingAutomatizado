from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

#crear driver de selenium antes de ejecutar todos los escenarios

def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

#Hacer driver quit, al terminar de ejecutar todos los escenarios

def after_all(context):
    context.driver.quit()