from behave import  given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

from ShopHub.pages.login_page import LoginPage

@given('el usuario ingresa a la web Login')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.load()

@when('el usuario llena los campos obligatorios')
def step_impl(context):
    context.login_page.Login("juan@mail.com", "contra123")

@when('el usuario deja vacío el campo "contraseña"')
def step_impl(context):
    context.login_page.Login("juan@mail.com", "")

@when('el usuario llena el campo contraseña con caracteres random')
def step_impl(context):
    random_password = "".join(random.choices(string.ascii_letters + string.digits, k=8))
    context.login_page.Login("juan@mail.com", random_password)

@then('se redirige a la página de "Login exitoso"')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("success")
    )

    url_actual = context.driver.current_url
    assert "success" in url_actual, f"La URL {url_actual} no contiene 'success'"

@then('se muestra el mensaje de error "Rellene este campo"')
def step_impl(context):
    mensaje = context.login_page.get_password_error_message()
    assert "campo" in mensaje, f"mensaje: {mensaje}"

@then('se muestra el mensaje fail Login')
def step_impl(context):
    mensaje = context.login_page.get_password_error_message()
    assert "fail Login" in mensaje, f"Mensaje real: {mensaje}, ES UN BUG"