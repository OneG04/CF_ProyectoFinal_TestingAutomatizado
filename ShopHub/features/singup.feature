Feature: SingUp

  Como usuario no autentificado
  Quiero poder registrarme
  Para acceder a las funcionalidades de usuario registrado

  Scenario: SingUp exitoso
    Given el usuario ingresa a la web de Sing Up
    When el usuario ingresa credenciales válidas
    Then validar página success

  Scenario: Sign up con mail inválido
    Given el usuario ingresa a la web de Sing Up
    When el usuario no introduce el carácter "@" en el campo email
    Then se muestra el mensaje de error "incluye un signo @"

  Scenario: Sign up con campo vacío
    Given el usuario ingresa a la web de Sing Up
    When el usuario deja vacío el campo "password"
    Then se muestra el mensaje de error "Completa este campo"