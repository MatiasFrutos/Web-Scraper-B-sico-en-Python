# Web Scraper Básico en Python

Este es un script básico en Python que utiliza las librerías `requests` y `Beautiful Soup` para extraer información de una página web. Actualmente, el script puede extraer todos los títulos (de `<h1>` a `<h6>`) y todos los enlaces (`<a>` con atributo `href`) de la URL proporcionada por el usuario.

**¡Importante!** Utiliza este script de manera ética y respetando los términos de servicio y el archivo `robots.txt` de los sitios web.

## Cómo Utilizar

1.  Asegúrate de tener Python instalado en tu sistema.
2.  Instala las librerías necesarias: `pip install requests beautifulsoup4`
3.  Clona este repositorio o descarga el archivo `web_scraper.py`.
4.  Abre tu terminal o símbolo del sistema y navega al directorio donde guardaste el archivo.
5.  Ejecuta el script con el comando: `python web_scraper.py`
6.  Ingresa la URL del sitio web que deseas analizar cuando se te solicite.
7.  El script mostrará los títulos y enlaces encontrados en la consola.

## Tecnologías Utilizadas

* Python
* requests
* Beautiful Soup 4

## Posibles Mejoras Futuras

* Permitir al usuario especificar qué tipo de información extraer (ej: texto de párrafos, imágenes).
* Implementar la extracción de datos más específicos basados en selectores CSS o XPath.
* Guardar los resultados en un archivo (ej: CSV, JSON).
* Manejar la paginación en sitios web.
* Implementar un mecanismo para respetar el `robots.txt`.
* Agregar una interfaz de usuario (GUI).

## Autor

MatiasFrutos
