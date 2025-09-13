#Proyecto final
#####Descripción del proyecto 

###### 
En este proyecto se requiere realizar las pruebas para una página web ShopHub, 	relacionada a comprás en línea, donde se analizan las funciones más relevantes del los distintos flujos que se requieren al realizar una compra, desde registrate como usuario en la página hasta poder lograr registar un pago, con articulos seleccionados,  se utilizó en su mayoría el marco de trabajo BEHAVE, con sintaxis Guerkin, de esta manera es más comprensible al leer lo que se realiza en cada test. Además de la página Web, se nos proporcionó una archivo swager, de una API, con todos los endpoints relacionados a un Aeropuerto, para ello se utilizó Selenium, para poder realizar las peticiones, ya sean de tipo POST, o GET, según fuera el caso, y lo que quisiera probar. 

#### Instrucciones de instalación 

El repositorio se encuentra alojado en un repositorio  GitHub, pueden acceder al enlace para clonarlo.
https://github.com/OneG04/CF_ProyectoFinal_TestingAutomatizado.git 

####Instrucciones de uso
Para la parte de las API, se muestran algunos ejemplos de los enpoint que se utilizaron 

**USERS**

POST /users

{
  "email": "user@example.com",
  "password": "string",
  "full_name": "string",
  "role": "passenger"
}

200 "message": "Successful response"
401 "message": "Validation Error" 

**AIRPORTS**

POST /airports

{
  "iata_code": "THD",
  "city": "string",
  "country": "string"
}

200 "message": "Successful response"
401 "message": "Validation Error" 

**FLIGHTS** 

POST /flights
{
  "origin": "EVY",
  "destination": "FDV",
  "departure_time": "2025-09-12T02:28:16.930Z",
  "arrival_time": "2025-09-12T02:28:16.930Z",
  "base_price": 0,
  "aircraft_id": "string"
}

200 "message": "Successful response"
401 "message": "Validation Error" 


**BOOKINGS** 

POST /bookings 
{
  "flight_id": "string",
  "passengers": [
    {
      "full_name": "string",
      "passport": "string",
      "seat": "string"
    }
  ]
}

200 "message": "Successful response"
401 "message": "Validation Error" 

**PAYMENTS** 

POST/payments 

{
  "booking_id": "string",
  "amount": 0,
  "payment_method": "string"
}

200 "message": "Successful response"
401 "message": "Validation Error" 

#### Tecnologías utilizadas 

**Lenguaje de Programación**

Se utilizó principalmente Python como base, para nuestro código de pruebas. 
Dentro de sus librerias se instalo lo siguiente: 
1. pytest
1. pip
1. request

En el código que se desarrolló para antes de las pruebas se utilizó @pytest.fixture para la preparación de los datos y su configuración, dentro de la carpeta *conftest.py*

Dentro de la misma capeta se trabajó con toda la información de la API, como su URL y en general la configuración. 

Métodos empleados para las peticiones de las pruebas API 

- POST
- GET
- DELETE

**Framework y Bibliotecas **

**Selenium** fue una herramienta que se utilizó como Framework para la automatización de las pruebas, con el uso de POM, dando lógica y funcionalidad a los datos que teniamos, en este caso los ENDPOINTS

**Behave** otro framework para escribir pruebas automatizadas con Gherkin, donde su sixtaxis se reduce a:
- Given
- When 
- Then













###End
