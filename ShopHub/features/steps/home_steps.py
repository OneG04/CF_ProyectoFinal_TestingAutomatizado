from behave import  given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ShopHub.pages.home_page import HomePage

@given ('el usuario ingresa a la web')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.load()

@when ('El usuario en Home presiona el botón "Special deals"')
def step_impl(context):
    context.home_page.go_deals()

@then ('el usuario es redirigido a la página "Special Deals"')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("special-deals")
    )

    url_actual = context.driver.current_url
    assert "special-deals" in url_actual, f"La URL {url_actual} no contiene 'special-deals'"