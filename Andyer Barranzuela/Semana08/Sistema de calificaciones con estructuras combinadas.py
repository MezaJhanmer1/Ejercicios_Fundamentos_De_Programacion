# Ejercicio 08: Sistema de calificaciones
# Calcular promedios y encontrar al mejor estudiante de cada materia.

# Datos de las materias, alumnos y sus notas.
reporte_materias = [
    {
        "materia": "Matemáticas",
        "alumnos": ["Ana", "Pedro", "Luis", "María"],
        "notas": [18.0, 12.5, 14.0, 19.5]
    },
    {
        "materia": "Fundamentos de Programación",
        "alumnos": ["Cristian", "Hans", "Luiggi", "Mariana"],
        "notas": [5.0, 16.5, 11.0, 13.0]
    }
]

# Recorrer cada materia para calcular sus resultados.
for item in reporte_materias:
    suma_notas = 0  # Inicializar la suma de notas.
    for nota in item["notas"]:
        suma_notas = suma_notas + nota  # Acumular las notas.

    # Calcular y guardar el promedio de la materia.
    item["promedio"] = suma_notas / len(item["notas"])

    # Inicializar los datos del mejor estudiante.
    nota_maxima = 0.0
    mejor_alumno = ""

    # Comparar las notas y ubicar al alumno con la nota más alta.
    for i in range(len(item["notas"])):
        if item["notas"][i] > nota_maxima:
            nota_maxima = item["notas"][i]
            mejor_alumno = item["alumnos"][i]

    # Guardar el mejor alumno y su nota en el diccionario.
    item["mejor_estudiante"] = mejor_alumno
    item["nota_maxima"] = nota_maxima

# Crear una lista con los promedios de las materias.
lista_promedios = []
for item in reporte_materias:
    lista_promedios.append(item["promedio"])

# Ordenar los promedios de mayor a menor.
lista_promedios.sort()
lista_promedios.reverse()

# Crear una lista para guardar las materias ordenadas.
reporte_ordenado = []
for prom_buscado in lista_promedios:
    for item in reporte_materias:
        # Agregar la materia correspondiente sin repetirla.
        if item["promedio"] == prom_buscado and item not in reporte_ordenado:
            reporte_ordenado.append(item)

# Mostrar el reporte general ordenado por promedio.
print("       REPORTE GENERAL DE RENDIMIENTO             ")
for indice, item in enumerate(reporte_ordenado):
    print(indice + 1, "° - Materia:", item["materia"])
    print("    Promedio General:", item["promedio"])
    print("    Mejor Estudiante:", item["mejor_estudiante"], "(Nota:", item["nota_maxima"], ")")
    print("-" * 50)
