from behave import  given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from ShopHub.pages.categoryMC_page import CategoryMC
from ShopHub.pages.cart_page import CartPage
from ShopHub.pages.checkout_page import Checkout

@given('el usuario ingresa a la web categorias')
def step_impl(context):
    context.categoryMC_page = CategoryMC(context.driver)
    context.categoryMC_page.loadMC()

@when('el usuario selecciona objeto')
def step_impl(context):
    context.categoryMC_page.pagemc()

@when('el usuario va al carro de compras')
def step_impl(context):
    context.categoryMC_page.gocart()
    context.cart_page = CartPage(context.driver)
    context.cart_page.waitCart()

@when('el usuario hace clic en el ícono de borrar')
def step_impl(context):
    context.cart_page.deleteObj()

@when('el usuario hace clic en el botón "Continues to shopping"')
def step_impl(context):
    context.cart_page.continueshop()

@when('el usuario entra a Checkout')
def step_impl(context):
    context.cart_page.checkout()
    context.checkout_page = Checkout(context.driver)

@when('el usuario dejar vacío campo obligatorio "Phone"')
def step_impl(context):
    context.checkout_page.customerInfo("Juan", "Gomez", "juan@mail.com", "", "jr lima 222", "Lima", "54214", "Peru")

@when('el usuario llena los campos')
def step_impl(context):
    context.checkout_page.customerInfo("Juan", "Gomez", "juan@mail.com", "979883331", "jr lima 222", "Lima", "54214", "Peru")

@then('el usuario es redirigido a la página de carro vacío')
def step_impl(context):
    context.cart_page.emptyCart()

@then ('el usuario es redirigido a la página de inicio')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_to_be("https://shophub-commerce.vercel.app/")
    )
    assert context.driver.current_url == "https://shophub-commerce.vercel.app/"

@then('Mostrar mensaje de campo obligatorio')
def step_impl(context):
    mensaje = context.checkout_page.get_phone_error_message()
    assert "campo" in mensaje, f"mensaje: {mensaje}"

@then('Mostrar mensaje compra exitosa')
def step_impl(context):
    WebDriverWait(context.driver, 3).until(
        EC.url_contains("success")
    )

    url_actual = context.driver.current_url
    assert "success" in url_actual, f"La URL {url_actual} no contiene 'success', ES UN BUG"