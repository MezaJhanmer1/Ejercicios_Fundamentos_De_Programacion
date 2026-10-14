# [PASO 1] Se crea una lista llamada 'estudiantes'. 
# Cada elemento de la lista es un Diccionario con 3 claves: 'nombre', 'carrera' y 'promedio'.
estudiantes = [
    {'nombre': 'Ana', 'carrera': 'Ingeniería', 'promedio': 17.5},
    {'nombre': 'Luis', 'carrera': 'Medicina', 'promedio': 15.0},
    {'nombre': 'Mía', 'carrera': 'Derecho', 'promedio': 18.2},
    {'nombre': 'Juan', 'carrera': 'Arquitectura', 'promedio': 16.8}
]

# [PASO 2] Se imprime un título en pantalla.
# >>> IMPRIME: Lista de estudiantes:
print("Lista de estudiantes:")

# [PASO 3] Bucle for: recorre la lista elemento por elemento (diccionario por diccionario).
# En cada vuelta, la variable 'estudiante' toma el valor de un diccionario distinto.
for estudiante in estudiantes:
    print(f"{estudiante['nombre']}: {estudiante['promedio']}")


# ================= ENCONTRAR EL MEJOR PROMEDIO =================

# [PASO 4] Inicialización: Se supone que el primer estudiante de la lista es el mejor.
# La variable 'mejor' guarda el diccionario COMPLETO de Ana.
# Estado de 'mejor': {'nombre': 'Ana', 'promedio': 17.5, ...}
mejor = estudiantes[0]  # suponemos el primero

# [PASO 5] Bucle for: vuelve a recorrer toda la lista para comparar promedios.
for estudiante in estudiantes:
    if estudiante['promedio'] > mejor['promedio']:
        mejor = estudiante

# [PASO 6] Se imprime el resultado final. 
# '\n' al inicio genera un salto de línea en blanco para separar visualmente.
# Se accede a las claves 'nombre' y 'promedio' del diccionario que quedó guardado en 'mejor'.
# >>> IMPRIME EN PANTALLA: El estudiante con el promedio más alto es: Mía (18.2)
print(f"\nEl estudiante con el promedio más alto es: {mejor['nombre']} ({mejor['promedio']})")


#Lista de estudiantes:
#Ana: 17.5
#Luis: 15.0
#Mía: 18.2
#Juan: 16.8

#El estudiante con el promedio más alto es: Mía (18.2)