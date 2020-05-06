# RPAForm

Instrucciones de instalación:

- pip install -r requirements.txt
- Entrar a https://selenium-python.readthedocs.io/installation.html y descargar los drivers de Chrome necesarios.


Teclas para selenium:
- https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.keys

Para inicializar el programa hay dos opciones:
- Ejecutar main.py
- Ejecutar app/login.py para crear sesión en chrome y loguearse y Ejecutar app/create.py para crear un reporte

Para configurar:
- Por el momento, para configurar las colas se tiene el archivo app/extra/request.json, donde se ecuentra el nombre del dashboard que se quiere crear y el de las respectivas colas (queues)

Por el momento las otras funcionalidades están en prueba, procurar no usarlas.
