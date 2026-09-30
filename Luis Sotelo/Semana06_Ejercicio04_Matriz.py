
matriz = [
    [3, 1, 6],
    [4, 5, 2],
    [9, 8, 7]
]

def ordenar_matriz(M):                      
    lista_simple = []                       
    for fila in M:                          #para fila en M, toma la 1era fila
        for numero in fila:                 #para num en fila, coge los numeros en la fila tomada
            lista_simple.append(numero)     #luego agrega esos numeros tomados en la lista simple, se repite con todas las filas.
    #ordenamiento burbuja para la matriz
    n = len(lista_simple)                   #n = cantidad de lista, seria 9
    for i in range(n):                      #para i en el rango de 9(va pasar desde el 0 al 8 en pasadas completas)
        for j in range(0, n - i - 1):       #recorre de izq a der los num
            if lista_simple[j] > lista_simple[j + 1]:           #si num actual > al num de la derecha, si es SI
                lista_simple[j], lista_simple[j + 1] = lista_simple[j + 1], lista_simple[j]    #cambia los num actual/derecha a derecha/actual

    #ya ordenados en lista, volver a matriz
    indice = 0                              #para comenzar desde 0
    for i in range(3):      #para i en rango 3 - 3 vueltas completas para Filas (0, 1, 2)
        for j in range(3):  #para j en rango 3 - 3 vueltas completas para Columnas (0, 1, 2)
            M[i][j] = lista_simple[indice]     #en M [fila][columna] = guarda el número que está en la pos. indice de la lista
            indice += 1                        #cuenta el num  y aumenta el contador y pasa al siguiente de la fila

print("Matriz antes del ordenamiento:")
for fila in matriz:
    print(fila)

ordenar_matriz(matriz)
print("Matriz después del ordenamiento:")
for fila in matriz:
    print(fila)






#ejemplo ordenamiento burbuja
# Cuando j = 0: Compara el índice 0 (3) con el índice 1 (1).
#  ¿3 > 1? Sí. ¡Se intercambian!
# La lista ahora va quedando: [1, 3, 6, 4, ...]

# Cuando j = 1: Compara el índice 1 (3) con el índice 2 (6).
# ¿3 > 6? No. No hace nada, se quedan igual.
# La lista sigue: [1, 3, 6, 4, ...]

#ejemplo volver a matriz
# Empezamos en la Fila i = 0 (Primera fila):
# Columna j = 0: Guarda en M[0][0] lo que hay en lista_plana[0] (el 1). El indice sube a 1.
# Columna j = 1: Guarda en M[0][1] lo que hay en lista_plana[1] (el 2). El indice sube a 2.
# Columna j = 2: Guarda en M[0][2] lo que hay en lista_plana[2] (el 3). El indice sube a 3.
# ¡Terminó la primera fila! La matriz va quedando así: [[1, 2, 3], ...]

#2. Pasamos a la Fila i = 1 (Segunda fila):
# Columna j = 0: Guarda en M[1][0] lo que hay en lista_plana[3] (el 4). El indice sube a 4.
# Columna j = 1: Guarda en M[1][1] lo que hay en lista_plana[4] (el 5). El indice sube a 5.
# Columna j = 2: Guarda en M[1][2] lo que hay en lista_plana[5] (el 6). El indice sube a 6.
# ¡Terminó la segunda fila! La matriz va así: [[1, 2, 3], [4, 5, 6], ...]
