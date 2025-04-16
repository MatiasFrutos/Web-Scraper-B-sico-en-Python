import requests
from bs4 import BeautifulSoup

def extraer_titulos(url):
    """Extrae todos los títulos (etiquetas <h1> a <h6>) de una página web."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción para códigos de error HTTP
        soup = BeautifulSoup(response.content, 'html.parser')
        titulos = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        return [titulo.get_text().strip() for titulo in titulos]
    except requests.exceptions.RequestException as e:
        print(f"Error al acceder a la URL: {e}")
        return []

def extraer_links(url):
    """Extrae todos los enlaces (etiquetas <a> con atributo href) de una página web."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)
        return [link['href'] for link in links]
    except requests.exceptions.RequestException as e:
        print(f"Error al acceder a la URL: {e}")
        return []

def main():
    """Función principal para ejecutar el web scraper."""
    url_objetivo = input("Ingrese la URL del sitio web que desea analizar: ")

    print("\n--- Títulos encontrados ---")
    titulos = extraer_titulos(url_objetivo)
    if titulos:
        for titulo in titulos:
            print(titulo)
    else:
        print("No se encontraron títulos.")

    print("\n--- Enlaces encontrados ---")
    links = extraer_links(url_objetivo)
    if links:
        for link in links:
            print(link)
    else:
        print("No se encontraron enlaces.")

if __name__ == "__main__":
    main()