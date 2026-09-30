# ==========================================================
# MATRIZ ORIGINAL
# ==========================================================

matriz = [
    [3, 1, 6],
    [4, 5, 2],
    [9, 8, 7]
]


# ==========================================================
# FUNCIÓN PARA ORDENAR LA MATRIZ
# ==========================================================

def ordenar_matriz(M):

    # Creamos una lista vacía.
    # Aquí vamos a guardar todos los números de la matriz
    # para poder ordenarlos más fácilmente.
    lista_simple = []

    # Recorremos cada fila de la matriz
    for fila in M:

        # Recorremos cada número que existe dentro de la fila
        for numero in fila:

            # Agregamos cada número a la lista simple
            lista_simple.append(numero)


    # ======================================================
    # ORDENAMIENTO BURBUJA
    # ======================================================

    # len() nos indica cuántos elementos tiene la lista.
    # En este caso hay 9 números.
    n = len(lista_simple)

    # Este ciclo controla las pasadas que realizará
    # el algoritmo de ordenamiento.
    for i in range(n):

        # Este ciclo compara los números de dos en dos.
        # n - i - 1 hace que en cada pasada se reduzca
        # la cantidad de comparaciones.
        for j in range(0, n - i - 1):

            # Comparamos el número actual con el siguiente.
            # Si el actual es mayor que el de la derecha,
            # significa que están en el orden incorrecto.
            if lista_simple[j] > lista_simple[j + 1]:

                # Intercambiamos las posiciones.
                # El número mayor pasa a la derecha
                # y el menor pasa a la izquierda.
                lista_simple[j], lista_simple[j + 1] = \
                    lista_simple[j + 1], lista_simple[j]


    # ======================================================
    # VOLVER A CONVERTIR LA LISTA EN MATRIZ
    # ======================================================

    # Creamos un índice que empieza en 0.
    # Este nos permitirá recorrer la lista ordenada.
    indice = 0

    # Recorremos las 3 filas de la matriz.
    for i in range(3):

        # Recorremos las 3 columnas de cada fila.
        for j in range(3):

            # Colocamos el número ordenado de la lista
            # dentro de la posición correspondiente
            # de la matriz.
            M[i][j] = lista_simple[indice]

            # Aumentamos el índice para tomar
            # el siguiente número de la lista.
            indice += 1


# ==========================================================
# MOSTRAR MATRIZ ANTES DEL ORDENAMIENTO
# ==========================================================

print("Matriz antes del ordenamiento:")

# Recorremos cada fila y la mostramos.
for fila in matriz:
    print(fila)


# ==========================================================
# LLAMAR A LA FUNCIÓN
# ==========================================================

# Enviamos la matriz a la función para que
# todos sus números sean ordenados.
ordenar_matriz(matriz)


# ==========================================================
# MOSTRAR MATRIZ DESPUÉS DEL ORDENAMIENTO
# ==========================================================

print("Matriz después del ordenamiento:")

# Mostramos nuevamente cada fila.
for fila in matriz:
    print(fila)