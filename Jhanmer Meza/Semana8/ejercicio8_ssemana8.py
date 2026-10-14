# Ejercicio08 Sistema de Calificaciones con Estructuras Combinadas

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


for item in reporte_materias:                                   # para item en reporte_materias, se desarma la lista
    suma_notas = 0                                              # se genera un acumulador desde 0
    for nota in item["notas"]:                                  # para nota en item diccionario notas, desarma y toma los numeros
        suma_notas = suma_notas + nota                          # suma  toda las notas [18.0 + 12.5 + 14.0 + 19.5]
    item["promedio"] = suma_notas / len(item["notas"])          # el 64/4 es 16 se Guarda el promedio y se crea el item promedio en el diccionario
    
    
    nota_maxima = 0.0                                           # Inicializa las variables básicas para el promedio
    mejor_alumno = ""                                           # Inicializa las variables básicas para el mejor alumno
                                                                # Ciclo for basado en range (0, 1, 2, 3) para poder recorrer al mismo tiempo los dos arreglos paralelos
    for i in range(len(item["notas"])):                         # para i en range cantidad, busca item dicc notas  , recorre alumno y notas..
        if item["notas"][i] > nota_maxima:                      # nota actual > la nota_maxima
            nota_maxima = item["notas"][i]                      # actualiza nota
            mejor_alumno = item["alumnos"][i]                   # guarda alumno que está en esa misma posición i
            
    item["mejor_estudiante"] = mejor_alumno  # se agrega item tal como promedio y se Guarda el mejor alumno directo en el diccionario
    item["nota_maxima"] = nota_maxima        # se agrega item tal como promedio y se Guarda el mejor alumno directo en el diccionario

lista_promedios = []                                            # se agrega lista vacia
for item in reporte_materias:                                   # para item en reporte_materias
    lista_promedios.append(item["promedio"])                    # se agrega el nuevo item promedio

lista_promedios.sort()                                          # ordena de menor a mayor
lista_promedios.reverse()                                       # le da vuelta y Queda de mayor a menor 

reporte_ordenado = []                                           # se agrega lista vacia
for prom_buscado in lista_promedios:                            # toma el promedio mas alto buscado
    for item in reporte_materias:                               # desarma la lista de materias buscuando cual tiene ese promedio
        if item["promedio"] == prom_buscado and item not in reporte_ordenado:       #Exige que ambas condiciones y..
            reporte_ordenado.append(item)                       # que esta materia NO esté ya guardada dentro de la lista reporte_ordenado
                                                                #Encuentra el diccionario de Matemáticas y lo cuelga primero en la nueva lista


print("       REPORTE GENERAL DE RENDIMIENTO             ")

for indice, item in enumerate(reporte_ordenado):        # Desarma la lista final ya ordenada. enumerate nos da el num fila en indice (0, 1...) 
                                                        # y el diccionario de la materia en la variable materia.
    print(indice + 1, "° - Materia:", item["materia"])
    print("    Promedio General:", item["promedio"])
    print("    Mejor Estudiante:", item["mejor_estudiante"], "(Nota:", item["nota_maxima"], ")")
    print("-" * 50)