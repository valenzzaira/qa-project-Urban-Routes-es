# Automatización de Pruebas de Urban Routes con Selenium

Este proyecto automatiza las pruebas de la aplicación web "Urban Routes", utilizando Selenium con Python. El objetivo es asegurar la funcionalidad y la experiencia del usuario al interactuar con la plataforma.

## Descripción del Proyecto

El proyecto consiste en un conjunto de pruebas automatizadas que simulan el flujo de un usuario al utilizar "Urban Routes". Las pruebas cubren escenarios como la interacción con elementos de la interfaz de usuario, la verificación de funcionalidades específicas y la validación de la respuesta del sistema.

## Tecnologías y Técnicas Utilizadas

* **Selenium:** Se utiliza para automatizar la interacción con el navegador web, simulando las acciones del usuario en "Urban Routes".
* **Python:** El lenguaje de programación utilizado para escribir las pruebas, aprovechando su sintaxis clara y sus amplias bibliotecas.
* **PyCharm:** Entorno de Desarrollo Integrado (IDE) utilizado para escribir, depurar y gestionar el proyecto, facilitando el desarrollo con sus herramientas de asistencia y gestión de proyectos.
* **Localizadores:** Se emplean diversos tipos de localizadores para identificar elementos en la página web:
    * ID
    * XPath
    * CSS Selectors
    * Name
* **Interacción con Entradas y Botones:** Las pruebas interactúan con campos de texto, botones, sliders y otros elementos de la interfaz de usuario de "Urban Routes".
* **Esperas Explícitas:** Se implementan esperas explícitas para asegurar que los elementos estén presentes e interactivos antes de realizar acciones, mejorando la robustez de las pruebas.
* **Chrome:** Las pruebas fueron ejecutadas en el navegador Google Chrome.

## Casos de Prueba

Las pruebas cubren diversos escenarios de uso de "Urban Routes", incluyendo:

1.  **Verificación de la funcionalidad de sliders:** Verifica que los sliders funcionen correctamente y cambien de estado al interactuar con ellos.
2.  **Interacción con campos de texto:** Verifica que los campos de texto acepten entradas válidas y manejen entradas inválidas correctamente.
3.  **Pruebas de botones:** Verifica que los botones realicen las acciones esperadas al ser presionados.
4.  **Validación de mensajes y alertas:** Verifica que la aplicación muestre mensajes y alertas correctos en diferentes situaciones.

## Requisitos

* Python 3.x
* Selenium
* ChromeDriver (para pruebas en Chrome)
* PyCharm (opcional, pero recomendado)

## Instalación

1.  Clona el repositorio:

    ```bash
    git clone [https://github.com/dserodio?tab=repositories](https://github.com/dserodio?tab=repositories)
    ```

2.  Crea un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv venv
    ```

3.  Activa el entorno virtual:

    * En Windows: `venv\Scripts\activate`
    * En macOS y Linux: `source venv/bin/activate`

4.  Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Ejecución de las Pruebas

1.  Asegúrate de tener el ChromeDriver instalado y configurado en el PATH.
2.  Ejecuta las pruebas desde la línea de comandos:

    ```bash
    python -m unittest discover
    ```

    O, si estás usando PyCharm, puedes ejecutar las pruebas directamente desde el IDE.

## Estructura del Proyecto
