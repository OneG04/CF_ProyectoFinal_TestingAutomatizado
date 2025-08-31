Feature: SingUp

  Como usuario no autentificado
  Quiero poder registrarme
  Para acceder a las funcionalidades de usuario registrado

  Scenario: SingUp exitoso
    Given el usuario ingresa a la web de Sing Up
    When el usuario ingresa credenciales válidas
    Then validar página Login