Feature: Login

  Como usuario no autentificado
  Quiero poder hacer Login
  Para acceder a las funcionalidades de usuario registrado

  Scenario: Login exitoso
    Given el usuario ingresa a la web Login
    When el usuario llena los campos obligatorios
    Then se redirige a la página de "Login exitoso"