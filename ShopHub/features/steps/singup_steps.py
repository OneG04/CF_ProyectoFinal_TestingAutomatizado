from behave import  given, when, then

from pages import singup_page

@given('el usuario ingresa a la web')
def step_impl(context):
    print('paso 1')

@when ('el usuario hace clic en el botón Sign up')
def step_impl(context):
    print('paso 1')

@when ('el usuario ingresa credenciales válidas')
def step_impl(context):
    print('paso 1')

@then ('validar página Login')
def step_impl(context):
    print('paso 1')