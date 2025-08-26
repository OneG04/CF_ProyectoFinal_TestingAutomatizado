from selenium import webdriver

#crear driver de selenium antes de ejecutar todos los escenarios

def before_all(context):
    context.driver = webdriver.Chrome()

#Hacer driver quit, al terminar de ejecutar todos los escenarios

def after_all(context):
    context.driver.quit()