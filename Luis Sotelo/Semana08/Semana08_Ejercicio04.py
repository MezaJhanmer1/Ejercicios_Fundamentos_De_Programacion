#Ejercicio 4 –Lista de Diccionario de Estudiantes

estudiantes = [
    {"nombre": "Carolina", "carrera": "Derecho", "promedio": 17.5},
    {"nombre": "Tatiana", "carrera": "Contabilidad", "promedio": 14.0},
    {"nombre": "Jose María", "carrera": "Medicina", "promedio": 19.2},
    {"nombre": "Luigi", "carrera": "Civil", "promedio": 12.8}
]

mejor_estudiante = ""               #variables vacias para tomar al mejor
promedio_mas_alto = 0.0
                                                            #el for para desarmar la lista diccionario y tomar valor por valor para el print
for estudiante in estudiantes:                              # para estudiantes en lista de estudiantes , recorrer uno por uno la lista
    if estudiante["promedio"] > promedio_mas_alto:          # Si el diccionario de promedio de estudiante actual > al que teníamos guardado:
        promedio_mas_alto = estudiante["promedio"]  # Actualizamos la nota más alta
        mejor_estudiante = estudiante["nombre"]     # Guarda su nombre

print("--- ESTUDIANTES ---")                                 # como es un diccionario hay que especificar para sacar los datos
for estudiante in estudiantes:                               # para estudiantes en lista de estudiantes , recorrer uno por uno la lista        
    print(f"Estudiante: {estudiante['nombre']} | Promedio: {estudiante['promedio']}")

print("-" * 40)
print("Estudiante con el promedio más alto:")
print(f"{mejor_estudiante} (Promedio: {promedio_mas_alto})")