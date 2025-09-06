from behave import  given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ShopHub.pages.singup_page import SingupPage


@given('el usuario ingresa a la web de Sing Up')
def step_impl(context):
    context.singup_page = SingupPage(context.driver)
    context.singup_page.load()

@when ('el usuario ingresa credenciales válidas')
def step_impl(context):
    context.singup_page.formulario("Juan", "Gomez", "juan@mail.com", "123", "123456")

@when ('el usuario no introduce el carácter "@" en el campo email')
def step_imp(context):
    context.singup_page.formulario("Juan", "Gomez", "juanmail", "123", "123aa456")

@when ('el usuario deja vacío el campo "password"')
def step_imp(context):
    context.singup_page.formulario("Juan", "Gomez", "juan@mail.com", "123", "")

@then ('validar página success')
def step_impl(context):
    # Espera hasta que la URL contenga "success"
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("success")
    )

    url_actual = context.driver.current_url
    assert "success" in url_actual, f"La URL {url_actual} no contiene 'success'"

@then ('se muestra el mensaje de error "incluye un signo @"')
def step_impl(context):
    mensaje = context.singup_page.get_email_error_message()
    assert "@" in mensaje, f"El mensaje mostrado fue: {mensaje}"

@then ('se muestra el mensaje de error "Completa este campo"')
def step_impl(context):
    mensaje = context.singup_page.get_password_error_message()
    #print("MENSAJE REAL:", mensaje)
    assert "campo" in mensaje, f"mensaje: {mensaje}"


