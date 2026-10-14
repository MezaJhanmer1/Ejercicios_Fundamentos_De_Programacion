# [PASO 1] Se crea la lista principal 'reporte_materias'.
# Es una lista que contiene diccionarios. Cada diccionario tiene una materia,
# una lista de alumnos y una lista de notas paralela (mismo orden).
reporte_materias = [
    {
        "materia": "Matemáticas",
        "alumnos": ["Ana", "Pedro", "Luis", "María"],
        "notas": [18.0, 12.5, 14.0, 19.5]
    },
    {
        "materia": "Fundamentos de Programación",
        "alumnos": ["Cristian", "Hans", "Luiggi", "Mariana"],
        "notas": [05.0, 16.5, 11.0, 13.0]
    }
]

# [PASO 2] Bucle externo: recorre cada materia (cada diccionario).
# Iteración 1: item = Diccionario de Matemáticas
# Iteración 2: item = Diccionario de Fundamentos de Programación
for item in reporte_materias:                                   
    
    # [PASO 3] Se inicializa el acumulador de notas en 0 para esta materia.
    suma_notas = 0                                              
    
    # [PASO 4] Bucle interno: recorre la lista de notas de la materia actual.
    # Iteración 1 (Matemáticas): nota=18.0 -> suma_notas = 18.0
    # Iteración 2 (Matemáticas): nota=12.5 -> suma_notas = 30.5
    # Iteración 3 (Matemáticas): nota=14.0 -> suma_notas = 44.5
    # Iteración 4 (Matemáticas): nota=19.5 -> suma_notas = 64.0
    for nota in item["notas"]:                                  
        suma_notas = suma_notas + nota                          
    
    # [PASO 5] Se calcula el promedio (64.0 / 4 = 16.0) y se guarda en el diccionario.
    # Se crea una nueva clave "promedio" dentro del diccionario de la materia.
    item["promedio"] = suma_notas / len(item["notas"])          
    
    
    # [PASO 6] Se inicializan las variables para encontrar al mejor alumno.
    # Se usa 0.0 y "" como valores base (inferiores a cualquier nota/nombre real).
    nota_maxima = 0.0                                           
    mejor_alumno = ""                                           
    
    # [PASO 7] Bucle con range: recorre los índices 0, 1, 2, 3.
    # Esto permite acceder al mismo tiempo a 'notas' y 'alumnos' usando el mismo índice 'i'.
    for i in range(len(item["notas"])):                         
        
        # [PASO 8] Comparación: ¿La nota actual en la posición 'i' es mayor que la máxima?
        # Iteración 1 (i=0): 18.0 > 0.0? SÍ -> nota_maxima=18.0, mejor_alumno="Ana"
        # Iteración 2 (i=1): 12.5 > 18.0? NO.
        # Iteración 3 (i=2): 14.0 > 18.0? NO.
        # Iteración 4 (i=3): 19.5 > 18.0? SÍ -> nota_maxima=19.5, mejor_alumno="María"
        if item["notas"][i] > nota_maxima:                      
            nota_maxima = item["notas"][i]                      
            mejor_alumno = item["alumnos"][i]                   
            
    # [PASO 9] Se guardan los resultados del mejor alumno en el diccionario de la materia.
    item["mejor_estudiante"] = mejor_alumno  
    item["nota_maxima"] = nota_maxima        

# ================= ORDENAMIENTO MANUAL POR PROMEDIO =================

# [PASO 10] Se crea una lista vacía para extraer solo los promedios.
lista_promedios = []                                            

# [PASO 11] Se recorre la lista de materias y se extrae el promedio de cada una.
# Matemáticas: 16.0 | Fundamentos: 11.375
for item in reporte_materias:                                   
    lista_promedios.append(item["promedio"])                    

# [PASO 12] Se ordenan los promedios de menor a mayor: [11.375, 16.0]
lista_promedios.sort()                                          

# [PASO 13] Se invierte la lista para que quede de mayor a menor: [16.0, 11.375]
lista_promedios.reverse()                                       

# [PASO 14] Se crea una lista vacía para el reporte final ordenado.
reporte_ordenado = []                                           

# [PASO 15] Bucle externo: recorre los promedios ordenados (16.0, luego 11.375).
for prom_buscado in lista_promedios:                            
    
    # [PASO 16] Bucle interno: busca en las materias cuál tiene ese promedio exacto.
    for item in reporte_materias:                               
        
        # [PASO 17] Condición doble: 
        # 1) ¿El promedio de la materia coincide con el buscado?
        # 2) ¿La materia NO está ya en la lista ordenada? (Evita duplicados si hay promedios iguales).
        if item["promedio"] == prom_buscado and item not in reporte_ordenado:       
            
            # [PASO 18] Se agrega el diccionario completo de la materia a la lista ordenada.
            reporte_ordenado.append(item)                       
            # Al terminar, 'reporte_ordenado' tendrá primero Matemáticas (16.0) y luego Fundamentos (11.375).

# ================= IMPRESIÓN DEL REPORTE FINAL =================

print("       REPORTE GENERAL DE RENDIMIENTO             ")

# [PASO 19] enumerate nos da el índice (0, 1) y el diccionario de la materia.
# Se usa 'indice + 1' para que el ranking empiece en 1° y no en 0°.
for indice, item in enumerate(reporte_ordenado):        
        
    # Iteración 1 (Matemáticas):
    print(indice + 1, "° - Materia:", item["materia"])
    print("    Promedio General:", item["promedio"])
    print("    Mejor Estudiante:", item["mejor_estudiante"], "(Nota:", item["nota_maxima"], ")")
    print("-" * 50)



#           REPORTE GENERAL DE RENDIMIENTO             
#1 ° - Materia: Matemáticas
#    Promedio General: 16.0
#    Mejor Estudiante: María (Nota: 19.5 )
#--------------------------------------------------
#2 ° - Materia: Fundamentos de Programación
#    Promedio General: 11.375
#    Mejor Estudiante: Hans (Nota: 16.5 )
#--------------------------------------------------