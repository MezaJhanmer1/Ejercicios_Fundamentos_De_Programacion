# [PASO 1] Se importa la librería 're' (Regular Expressions).
# Nos permitirá buscar texto dentro de otros textos de forma inteligente (ignorando mayúsculas).
import re                                                    

# [PASO 2] Se crea la lista 'libros' con diccionarios. Cada diccionario es un libro.
libros = [
    {"titulo": "Python para Todos", "autor": "Carlos García", "año": 2020},
    {"titulo": "Aprende Python", "autor": "Ana Martínez", "año": 2022},
    {"titulo": "El camino del Programador", "autor": "Carlos García", "año": 2019},
    {"titulo": "Historias de Programación", "autor": "Luis Pérez", "año": 2025},
    {"titulo": "Guía Avanzada de Python", "autor": "Ana Martínez", "año": 2024}
]

# [PASO 3] Se define la función 'buscador'. Recibe el catálogo y la palabra a buscar (query).
def buscador(catalogo, query):                        
    
    # [PASO 4] Se crea la lista vacía donde se guardarán los libros que coincidan.
    resultados = []                                   
    
    # [PASO 5] Bucle: recorre cada libro del catálogo uno por uno.
    for libro in catalogo:                            
        
        # [PASO 6] Se inicializa el puntaje en 0 para este libro en particular.
        puntaje = 0                                   
        
        # [PASO 7] Buscamos la palabra en el TÍTULO usando re.search.
        # re.IGNORECASE hace que no importen las mayúsculas/minúsculas (ej. "PyThOn" = "python").
        # Si la encuentra, suma 2 puntos.
        # Ej: "Python para Todos" -> re.search("PyThOn", "Python para Todos", re.IGNORECASE) -> SÍ. puntaje = 0 + 2 = 2
        if re.search(query, libro["titulo"], re.IGNORECASE):       
            puntaje = puntaje + 2                               
        
        # [PASO 8] Buscamos la palabra en el AUTOR usando re.search.
        # Si la encuentra, suma 1 punto (menos peso que el título).
        # Ej: "Carlos García" no tiene "PyThOn", así que no suma. puntaje sigue en 2.
        if re.search(query, libro["autor"], re.IGNORECASE):        
            puntaje = puntaje + 1            
            
        # [PASO 9] Si el libro sumó al menos 1 punto, significa que coincidió en algo.
        if puntaje > 0:                          
            # [PASO 10] Se le inyecta una nueva clave "puntaje" al diccionario del libro.
            libro["puntaje"] = puntaje           
            # [PASO 11] Se guarda el diccionario completo del libro en la lista de resultados.
            resultados.append(libro)             


    # [PASO 12] Función interna para definir los criterios de ordenamiento.
    # Python la usará dentro de sorted() para saber cómo ordenar.
    def criterios_orden(item):                              
        # [PASO 13] Retorna una tupla con DOS criterios:
        # 1) -item["puntaje"]: El signo menos invierte el orden. En lugar de menor a mayor, será MAYOR a MENOR.
        # 2) item["año"]: Se deja normal para que vaya de MENOR (más antiguo) a MAYOR (más reciente).
        return (-item["puntaje"], item["año"])              
                                                            
    # [PASO 14] sorted() ordena la lista 'resultados' usando la función 'criterios_orden'.
    return sorted(resultados, key=criterios_orden)          


# ================= EJECUCIÓN PRINCIPAL =================

# [PASO 15] Se define la palabra a buscar.
busqueda = "PyThOn"                                         

# [PASO 16] Se llama a la función 'buscador' y el resultado se guarda en 'lista_resultados'.
# El resultado será una lista con los 3 libros que tienen "Python" en el título,
# ordenados primero por puntaje (todos tienen 2) y luego por año (2020, 2022, 2024).
lista_resultados = buscador(libros, busqueda)               

# [PASO 17] Se imprime el encabezado del reporte.
print("--- RESULTADOS DEL BUSCADOR ---")
print("Término buscado:", busqueda)
print("-" * 50)

# [PASO 18] Bucle final: enumerate nos da el índice (0, 1, 2) y el diccionario del libro.
for indice, libro in enumerate(lista_resultados):        
        
    # Iteración 1: indice=0 -> Imprime "1 ° Lugar - Puntos: 2 | Año: 2020" (Python para Todos)
    # Iteración 2: indice=1 -> Imprime "2 ° Lugar - Puntos: 2 | Año: 2022" (Aprende Python)
    # Iteración 3: indice=2 -> Imprime "3 ° Lugar - Puntos: 2 | Año: 2024" (Guía Avanzada de Python)
    print(indice + 1, "° Lugar - Puntos:", libro["puntaje"], "| Año:", libro["año"])
    print("    Título:", libro["titulo"])
    print("    Autor:", libro["autor"])
    print("-" * 30)