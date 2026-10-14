# Ejercicio 4 – Lista de Diccionarios de Estudiantes

# Lista que contiene diccionarios con los datos de cada estudiante
estudiantes = [
    {"nombre": "Carolina", "carrera": "Derecho", "promedio": 17.5},
    {"nombre": "Tatiana", "carrera": "Contabilidad", "promedio": 14.0},
    {"nombre": "Jose María", "carrera": "Medicina", "promedio": 19.2},
    {"nombre": "Luigi", "carrera": "Civil", "promedio": 12.8}
]

# Variables para guardar al estudiante con el promedio más alto
mejor_estudiante = ""
promedio_mas_alto = 0.0

# Recorremos la lista para encontrar el promedio más alto
for estudiante in estudiantes:
    # Comparamos el promedio actual con el promedio más alto guardado
    if estudiante["promedio"] > promedio_mas_alto:
        promedio_mas_alto = estudiante["promedio"]  # Actualiza la nota más alta
        mejor_estudiante = estudiante["nombre"]  # Guarda el nombre del estudiante

# Mostrar los datos de todos los estudiantes
print("--- ESTUDIANTES ---")
for estudiante in estudiantes:
    # Accedemos al nombre y al promedio usando las claves del diccionario
    print(f"Estudiante: {estudiante['nombre']} | Promedio: {estudiante['promedio']}")

print("-" * 40)

print("Estudiante con el promedio más alto:")
print(f"{mejor_estudiante} (Promedio: {promedio_mas_alto})")