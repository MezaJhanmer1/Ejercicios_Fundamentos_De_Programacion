# Ejercicio 09 – Extracción con Expresiones Regulares

import re  # Importa la librería para trabajar con expresiones regulares.

# Lista de diccionarios con la información de los libros.
libros = [
    {"titulo": "Python para Todos", "autor": "Carlos García", "año": 2020},
    {"titulo": "Aprende Python", "autor": "Ana Martínez", "año": 2022},
    {"titulo": "El camino del Programador", "autor": "Carlos García", "año": 2019},
    {"titulo": "Historias de Programación", "autor": "Luis Pérez", "año": 2025},
    {"titulo": "Guía Avanzada de Python", "autor": "Ana Martínez", "año": 2024}
]

# Función que busca libros y los ordena según su puntaje y año.
def buscador(catalogo, query):
    resultados = []  # Lista vacía para guardar los libros encontrados.

    for libro in catalogo:  # Recorre cada libro del catálogo.
        puntaje = 0  # Reinicia el puntaje para cada libro.

        if re.search(query, libro["titulo"], re.IGNORECASE):
            # Busca el término en el título, ignorando mayúsculas y minúsculas.
            puntaje = puntaje + 2  # Suma 2 puntos si coincide con el título.

        if re.search(query, libro["autor"], re.IGNORECASE):
            # Busca el término en el nombre del autor.
            puntaje = puntaje + 1  # Suma 1 punto si coincide con el autor.

        if puntaje > 0:
            # Si el libro coincide con la búsqueda, guarda su puntaje.
            libro["puntaje"] = puntaje
            resultados.append(libro)  # Agrega el libro a los resultados.

    # Define los criterios para ordenar los libros encontrados.
    def criterios_orden(item):
        return (-item["puntaje"], item["año"])
        # Primero ordena por mayor puntaje y, en caso de empate,
        # por año de menor a mayor (del más antiguo al más reciente).

    return sorted(resultados, key=criterios_orden)
    # Devuelve una nueva lista ordenada sin reorganizar la lista resultados.

# Palabra que se utilizará para probar la búsqueda.
busqueda = "PyThOn"

# Ejecuta la función y guarda los libros encontrados y ordenados.
lista_resultados = buscador(libros, busqueda)

# Mostrar el término buscado.
print("--- RESULTADOS DEL BUSCADOR ---")
print("Término buscado:", busqueda)
print("-" * 50)

# Mostrar los resultados con su posición, puntaje, año, título y autor.
for indice, libro in enumerate(lista_resultados):
    print(indice + 1, "° Lugar - Puntos:", libro["puntaje"],
          "| Año:", libro["año"])
    print("    Título:", libro["titulo"])
    print("    Autor:", libro["autor"])
    print("-" * 30)