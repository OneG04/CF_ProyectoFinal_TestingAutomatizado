from behave import  given, when, then
from selenium.webdriver.support.wait import WebDriverWait

from ShopHub.pages.singup_page import SingupPage


@given('el usuario ingresa a la web de Sing Up')
def step_impl(context):
    context.singup_page = SingupPage(context.driver)
    context.singup_page.load()

@when ('el usuario ingresa credenciales válidas')
def step_impl(context):
    context.singup_page.formulario("Juan", "Gomez", "juan@mail.com", "123", "123456")

@then ('validar página Login')
def step_impl(context):
    context.time.sleep(5)
    url_actual = context.driver.current_url
    assert url_actual == "https://shophub-commerce.vercel.app/signup/success"