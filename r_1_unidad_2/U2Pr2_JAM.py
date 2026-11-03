import requests


def linea(simbolo="="):
  print(simbolo * 50)


def buscar_libro(titulo):
  url = f"https://openlibrary.org/search.json?q={titulo}"
  try:
    respuesta = requests.get(url)

    if respuesta.status_code != 200:
      print("Error en la solicitud")
      return None

    return respuesta.json()
  except requests.exceptions.RequestException:
    print("Error de conexión al realizar la solicitud.")
    return None


def main():
  linea("=")
  print("Práctica 1: OpenLibrary API")
  linea("=")

  titulo_ingresado = ""
  while not titulo_ingresado.strip():
    titulo_ingresado = input("Ingresa el título del libro a buscar: ").strip()

  datos = buscar_libro(titulo_ingresado)

  if datos and "docs" in datos:
    documentos = datos["docs"]
    print(f"\nSe encontraron {datos.get('numFound', 0)} resultados.\n")

    print("--- Listado de Documentos ---")
    for i, doc in enumerate(documentos[:10], start=1):
      titulo = doc.get("title", "Título no disponible")
      autores = ", ".join(doc.get("author_name", ["Autor desconocido"]))
      anios = doc.get("publish_year")
      anio = anios[0] if anios else "Año no disponible"
      key = doc.get("key", "")
      mas_info = f"https://openlibrary.org{key}" if key else "No disponible"

      print(f"{i}. Título: {titulo}")
      print(f"   Autor(es): {autores}")
      print(f"   Año de publicación: {anio}")
      print(f"   Más información: {mas_info}")
      linea("-")

    if documentos:
      print("\n")
      elegido = input("Introduce un título en especial de la lista anterior para consultar: ")
      print(f"Has seleccionado consultar sobre: {elegido}")


if __name__ == "__main__":
  main()