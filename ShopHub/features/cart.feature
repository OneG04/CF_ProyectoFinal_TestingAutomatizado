Feature: cart

  Como usuario
  Quiero poder seleccionar objetos
  Para acceder para poder comprarles

  Scenario: Remover objetos del carro
    Given el usuario ingresa a la web categorias
    When el usuario selecciona objeto
    And el usuario va al carro de compras
    And el usuario hace clic en el ícono de borrar
    Then el usuario es redirigido a la página de carro vacío

  Scenario: Continuar comprando
    Given el usuario ingresa a la web categorias
    When el usuario selecciona objeto
    And el usuario va al carro de compras
    And el usuario hace clic en el botón "Continues to shopping"
    Then el usuario es redirigido a la página de inicio

  #BUG REPORTED
  Scenario: Checkout con pago exitoso
    Given el usuario ingresa a la web categorias
    When el usuario selecciona objeto
    And el usuario va al carro de compras
    And el usuario entra a Checkout
    And el usuario llena los campos
    Then Mostrar mensaje compra exitosa

  Scenario: Checkout con campo vacio
    Given el usuario ingresa a la web categorias
    When el usuario selecciona objeto
    And el usuario va al carro de compras
    And el usuario entra a Checkout
    And el usuario dejar vacío campo obligatorio "Phone"
    Then Mostrar mensaje de campo obligatorio