
# Orbidi Test

Este es un proyecto de ejemplo que demuestra el uso de los principios SOLID, así como el uso de repositories y el patrón Singleton.

## CI
Se implemento un flujo para CI para la validacion de pruebas unitarias , linter y formato del codigo para pririzar la calidad al momento de realizar el merge a la rama master

![Screenshot 2023-06-12 at 1 54 18 AM](https://github.com/SebastianNorenaMarquezMiso/orbidi/assets/78800255/490975a0-4ab9-4df2-b61f-eb78c6c46129)


![Screenshot 2023-06-12 at 1 41 46 AM](https://github.com/SebastianNorenaMarquezMiso/orbidi/assets/78800255/a3b9ebaf-a45d-4936-96fd-d30ed61c0ca3)

## Requisitos

- Python 3.8 o superior

## Instalación

1. Clona este repositorio:

git clone https://github.com/SebastianNorenaMarquezMiso/orbidi.git

2. Accede al directorio del proyecto:
cd orbidi

3. Añadir archivo .env.local con las siguientes variables
```
  HUBSPOT_API_KEY=
  HUBSPOT_BASE_URL=https://api.hubapi.com

  CLICKUP_BASE_URL=https://api.clickup.com
  CLICKUP_LIST_ID=
  CLICKUP_API_KEY=

  DB_HOST=
  DB_PORT=5432
  DB_USER=developer
  DB_PASS=
  DB_NAME=

  LOGGING_LEVEL=INFO
  HUBSPOT_STATUS_PENDING=pending
  HUBSPOT_STATUS_ADDED=added
```
4. instalar poetry:
brew install poetry

5. Instala las dependencias del proyecto utilizando `poetry`:

poetry install

## Ejecución

Para ejecutar el proyecto, asegúrate de tener las dependencias instaladas siguiendo los pasos anteriores. Luego, puedes ejecutar el siguiente comando:



poetry run python api/main.py

Esto iniciará la aplicación y estará disponible en `http://localhost:8000`.

## Unit Tests

El proyecto utiliza `pytest` para ejecutar las pruebas unitarias. Asegúrate de tener las dependencias de desarrollo instaladas siguiendo los pasos anteriores. Para ejecutar las pruebas, utiliza el siguiente comando:


poetry run pytest
Esto ejecutará todas las pruebas unitarias y mostrará los resultados.

## Dependencias

El proyecto utiliza las siguientes librerías y herramientas:

- FastAPI: Un framework web para crear APIs rápidas en Python.
- Pydantic: Una biblioteca para validación y serialización de datos.
- Poetry: Una herramienta para administrar dependencias y entornos virtuales de Python.
- Pytest: Un marco de pruebas para escribir y ejecutar pruebas unitarias en Python.

## Uso de Repositories

En este proyecto, se utiliza el patrón Repository para separar la lógica de acceso a datos de la lógica de negocio. Los repositories proporcionan una abstracción sobre el almacenamiento de datos y permiten intercambiar fácilmente implementaciones sin afectar otras partes del código.

El archivo `contact_repository.py` en el directorio `database/repositories` contiene la implementación del repository para la entidad "Contact". Proporciona métodos para crear, obtener, actualizar y eliminar contactos en el almacenamiento de datos.
## Uso de Singleton

El patrón Singleton se utiliza en el archivo `database.py` en el directorio `database` para asegurar que solo exista una única instancia de la base de datos en toda la aplicación. Esto garantiza que el acceso a la base de datos sea consistente y evita problemas de concurrencia.

## Principios SOLID

El proyecto sigue los principios SOLID para escribir código modular, extensible y mantenible. Estos principios incluyen:

- **Single Responsibility Principle (SRP)**: Cada clase tiene una única responsabilidad.
- **Open-Closed Principle (OCP)**: Las entidades deben estar abiertas para extensión pero cerradas para modificación.
- **Liskov Substitution Principle (LSP)**: Los objetos de un programa deben ser reemplazables por instancias de sus subtipos sin alterar la corrección del programa.
- **Interface Segregation Principle (ISP)**: Los clientes no deben verse obligados a depender de interfaces que no usan.
- **Dependency Inversion Principle (DIP)**: Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones.

- **Principio de Responsabilidad Única (SRP)**: Cada clase tiene una única responsabilidad. Se puede observar este principio en varios archivos, donde cada clase o función se ocupa de una tarea específica. Por ejemplo, el archivo clients/hubspot_client.py contiene la clase HubspotClient que se encarga de interactuar con la API de HubSpot.

- **Principio de Abierto/Cerrado (OCP)**: Las clases están abiertas para su extensión pero cerradas para su modificación. Esto se puede ver en la estructura del proyecto, donde se utilizan clases y funciones para encapsular comportamientos específicos y se pueden agregar nuevas clases o funciones sin modificar las existentes.

- **Principio de Sustitución de Liskov (LSP)**: Las clases derivadas pueden ser sustituidas por sus clases base sin afectar el comportamiento del programa. El diseño modular del proyecto permite la extensibilidad y la sustitución de componentes.

- **Principio de Segregación de Interfaz (ISP)**: Las interfaces deben ser específicas y no contener métodos innecesarios para las implementaciones. No se utilizan interfaces explícitas, pero las clases y funciones están diseñadas de manera cohesiva y específica para sus propósitos, lo que refleja un enfoque de segregación de funcionalidad.

- **Principio de Inversión de Dependencia (DIP)**: Los módulos de alto nivel no deben depender de módulos de bajo nivel, sino de abstracciones. En el proyecto, se utilizan inyecciones de dependencia para proporcionar dependencias a través de la inicialización de clases. Por ejemplo, en el archivo database/repositories/contact_repository.py, se inyecta una instancia de Session en el constructor de ContactRepository, permitiendo que la clase dependa de la abstracción en lugar de una implementación concreta.
