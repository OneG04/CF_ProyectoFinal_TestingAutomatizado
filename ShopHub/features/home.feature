Feature: Home

  Como usuario
  Quiero poder revisar la web
  Para revisar productos o hacer compras

  Scenario: Ir a Special Deals
    Given el usuario ingresa a la web
    When El usuario en Home presiona el botón "Special deals"
    Then el usuario es redirigido a la página "Special Deals"