Feature: SingUp

  Como usuario no autentificado
  Quiero poder registrarme
  Para acceder a las funcionalidades de usuario registrado

  Scenario: SingUp exitoso
    Given el usuario ingresa a la web
    When el usuario hace clic en el botón Sign up
    And el usuario ingresa credenciales válidas
    Then validar página Login