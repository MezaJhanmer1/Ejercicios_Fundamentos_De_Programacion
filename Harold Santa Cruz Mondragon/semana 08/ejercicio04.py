# Ejercicio 04 – Lista de diccionarios de estudiantes

estudiantes = [
    {"nombre": "Carolina", "carrera": "Derecho", "promedio": 17.5},
    {"nombre": "Tatiana", "carrera": "Contabilidad", "promedio": 14.0},
    {"nombre": "Jose María", "carrera": "Medicina", "promedio": 19.2},
    {"nombre": "Luigi", "carrera": "Civil", "promedio": 12.8}
]

mejor_estudiante = ""               # Guardará el nombre del estudiante con mayor promedio
promedio_mas_alto = 0.0             # Guardará el promedio más alto encontrado

# Recorremos la lista de diccionarios para encontrar al mejor estudiante
for estudiante in estudiantes:
    if estudiante["promedio"] > promedio_mas_alto:      # ¿El promedio actual supera al registrado?
        promedio_mas_alto = estudiante["promedio"]      # Actualizamos el promedio más alto
        mejor_estudiante = estudiante["nombre"]         # Guardamos el nombre del estudiante

print("--- ESTUDIANTES ---")
# Recorremos cada diccionario y mostramos sus datos con acceso por clave
for estudiante in estudiantes:
    print(f"Estudiante: {estudiante['nombre']} | Promedio: {estudiante['promedio']}")

print("-" * 40)
print("Estudiante con el promedio más alto:")
print(f"{mejor_estudiante} (Promedio: {promedio_mas_alto})")