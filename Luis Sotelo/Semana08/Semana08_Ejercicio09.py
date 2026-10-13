# Ejercicio09 Extracción con Expresiones Regulares

import re                                                    # 1. Importamos la librería de expresiones regulares

libros = [
    {"titulo": "Python para Todos", "autor": "Carlos García", "año": 2020},
    {"titulo": "Aprende Python", "autor": "Ana Martínez", "año": 2022},
    {"titulo": "El camino del Programador", "autor": "Carlos García", "año": 2019},
    {"titulo": "Historias de Programación", "autor": "Luis Pérez", "año": 2025},
    {"titulo": "Guía Avanzada de Python", "autor": "Ana Martínez", "año": 2024}
]

def buscador(catalogo, query):                        # Def función buscador parametros catálogo y query
    resultados = []                                   # crea la lista vacía para ir metiendo los libros que coincidan.
    
    for libro in catalogo:                            # desarmar la lista del catálogo paquete por paquete
        puntaje = 0                                   # inicializa una variable puntaje en 0 para cada libro nuevo que empieza a revisar..
        
                                            # si el texto del query está dentro del título del libro
        if re.search(query, libro["titulo"], re.IGNORECASE):       # re.search busca la palabra usando re.IGNORECASE para ignorar mayús y minus
            puntaje = puntaje + 2                               # Si lo encuentra, le suma 2 puntos a la libreta de este libro
                                            # si el texto del query está dentro del autor del libro suma 2 puntos
        if re.search(query, libro["autor"], re.IGNORECASE):        # re.search busca la palabra usando re.IGNORECASE
            puntaje = puntaje + 1            # si el texto del query está dentro del autor del libro suma 1 punto
            
        if puntaje > 0:                          # Si sumó puntos o coincide en esos 2, le inyectamos la llave 'puntaje' y lo guardamos
            libro["puntaje"] = puntaje           # en la var libro crea nueva "puntaje" al diccionario de este libro para recordar su valor
            resultados.append(libro)             # guarda el paquete completo dentro de la lista de resultados


    def criterios_orden(item):                              #def funcion con parametro item
        return (-item["puntaje"], item["año"])              # invierte el sentido para ese dato al tener "-item"
                                                            # y el año normal para que vaya de MENOR (más antiguo) a mayor.
    return sorted(resultados, key=criterios_orden)          # sorted() ordena de golpe usando el -item puntaje e item año


busqueda = "PyThOn"                                         # crea la var para la prueba
lista_resultados = buscador(libros, busqueda)               # la lista de libros encontrados y ordenados se guarda en lista_resultados

print("--- RESULTADOS DEL BUSCADOR ---")
print("Término buscado:", busqueda)
print("-" * 50)

for indice, libro in enumerate(lista_resultados):        # Desarma la lista final ya ordenada. enumerate nos da el num fila en indice (0, 1...) 
    print(indice + 1, "° Lugar - Puntos:", libro["puntaje"], "| Año:", libro["año"])
    print("    Título:", libro["titulo"])
    print("    Autor:", libro["autor"])
    print("-" * 30)