# Ejercicio 04: Lista de diccionarios de estudiantes
# El programa muestra los estudiantes y encuentra el promedio más alto.

# Lista de diccionarios con los datos de cada estudiante.
estudiantes = [
    {"nombre": "Carolina", "carrera": "Derecho", "promedio": 17.5},
    {"nombre": "Tatiana", "carrera": "Contabilidad", "promedio": 14.0},
    {"nombre": "Jose María", "carrera": "Medicina", "promedio": 19.2},
    {"nombre": "Luigi", "carrera": "Civil", "promedio": 12.8}
]

# Inicializar las variables para guardar al mejor estudiante.
mejor_estudiante = ""
promedio_mas_alto = 0.0

# Recorrer la lista para revisar cada estudiante.
for estudiante in estudiantes:
    # Comparar su promedio con la nota más alta guardada.
    if estudiante["promedio"] > promedio_mas_alto:
        # Actualizar el promedio más alto.
        promedio_mas_alto = estudiante["promedio"]
        # Guardar el nombre del estudiante con esa nota.
        mejor_estudiante = estudiante["nombre"]

# Mostrar el título de la lista.
print("--- ESTUDIANTES ---")

# Recorrer la lista para mostrar los datos de cada estudiante.
for estudiante in estudiantes:
    # Imprimir el nombre y el promedio.
    print(f"Estudiante: {estudiante['nombre']} | Promedio: {estudiante['promedio']}")

# Mostrar una línea separadora.
print("-" * 40)

# Mostrar al estudiante con el promedio más alto.
print("Estudiante con el promedio más alto:")
print(f"{mejor_estudiante} (Promedio: {promedio_mas_alto})")
