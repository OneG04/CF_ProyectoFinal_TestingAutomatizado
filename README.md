#Proyecto final

CREADO POR:
- JUAN GOMEZ GRANDEZ | Código facilito username : JuanGOne
- Diana Laura Vazquez sandoval | Código facilito username : DIANALAU08
#####Descripción del proyecto 

###### 
Este proyecto implementa la automatización de pruebas para ShopHub, una aplicación web de comercio electrónico que permite a los usuarios registrarse, iniciar sesión, explorar categorías, gestionar un carrito de compras y realizar compras en línea. La solución combina pruebas de UI con Selenium y Behave siguiendo el patrón Page Object Model (POM), junto con pruebas de API utilizando pytest y requests, garantizando la validación integral tanto de la experiencia de usuario como de la lógica de negocio en el backend relacionados a un Aeropuerto. 

CASOS DE PRUEBA : https://docs.google.com/spreadsheets/d/1iEEbj6Jirm-cFQkf_3fS-h5TVdDVNIXv/edit?usp=sharing&ouid=103493380885471903635&rtpof=true&sd=true

#### Instrucciones de instalación 

El repositorio se encuentra alojado en un repositorio  GitHub, pueden acceder al enlace para clonarlo.
https://github.com/OneG04/CF_ProyectoFinal_TestingAutomatizado.git 

Estructura del proyecto

ProyectoFinal/
│── .venv/                        # Entorno virtual
│── .env                          # Variables de entorno (credenciales, URLs, etc.)
│── behave.ini                    # Configuración de Behave
│── requirements.txt              # Dependencias del proyecto
│── README.md                     # Documentación

│── API/                          # Pruebas de API con pytest
│   ├── tests/
│   │   ├── airports/
│   │   │   ├── __init__.py
│   │   │   ├── conftest.py
│   │   │   └── test_airports.py
│   │   ├── bookings/
│   │   │   ├── __init__.py
│   │   │   ├── conftest.py
│   │   │   └── test_bookings.py
│   │   ├── flights/
│   │   │   ├── __init__.py
│   │   │   ├── conftest.py
│   │   │   └── test_flight.py
│   │   ├── payments/
│   │   │   ├── __init__.py
│   │   │   ├── conftest.py
│   │   │   └── test_payments.py
│   │   ├── users/
│   │   │   ├── __init__.py
│   │   │   ├── conftest.py
│   │   │   └── test_users.py
│   │   └── __init__.py
│   │
│   └── utils/
│       ├── api_helpers.py        # Funciones auxiliares para requests
│       ├── fixture_utils.py      # Fixtures reutilizables
│       └── settings.py           # Configuración (URLs base, headers, etc.)

│── ShopHub/                      # Pruebas de UI con Selenium + Behave
│   ├── features/                 # Archivos .feature (BDD - Gherkin)
│   │   ├── cart.feature
│   │   ├── checkout.feature
│   │   ├── login.feature
│   │   ├── signup.feature
│   │   └── steps/                # Implementación de steps
│   │       ├── cart_steps.py
│   │       ├── checkout_steps.py
│   │       ├── login_steps.py
│   │       └── signup_steps.py
│   │
│   ├── pages/                    # Page Objects (POM)
│   │   ├── base_page.py
│   │   ├── cart_page.py
│   │   ├── category_page.py
│   │   ├── checkout_page.py
│   │   ├── login_page.py
│   │   └── signup_page.py
│   │
│   ├── utils/                    # Utilidades para UI
│   │   └── driver_factory.py
│   │
│   └── conftest.py               # Hooks y configuración para Selenium/Behave


ShopHub Automation Testing

Automatización de pruebas end-to-end para la aplicación ShopHub, una plataforma de comercio electrónico.
Este proyecto cubre los principales flujos de usuario:

Registro de usuario (SignUp)
Inicio de sesión (Login)
Navegación por categorías
Agregar productos al carrito
Eliminar productos del carrito
Proceso de checkout (compra)

Las pruebas están implementadas con Python, Selenium y Behave (Cucumber style) siguiendo el patrón Page Object Model (POM) para una mejor mantenibilidad.

Tecnologías / Paquetes utilizados

Selenium → Automatización de navegador
Behave → Framework BDD (similar a Cucumber)
Cucumber → Sintaxis Gherkin para features
webdriver-manager → Descarga y gestión automática de drivers (ChromeDriver, etc.)
python-dotenv → Manejo de variables de entorno
Faker → Generación de datos de prueba (emails, nombres, etc.)
pytest → Ejecutor alternativo de pruebas

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


###End