from behave import  given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ShopHub.pages.login_page import LoginPage

@given('el usuario ingresa a la web Login')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.load()

@when('el usuario llena los campos obligatorios')
def step_impl(context):
    context.login_page.Login("juan@mail.com", "contra123")

@then('se redirige a la página de "Login exitoso"')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("success")
    )

    url_actual = context.driver.current_url
    assert "success" in url_actual, f"La URL {url_actual} no contiene 'success'"