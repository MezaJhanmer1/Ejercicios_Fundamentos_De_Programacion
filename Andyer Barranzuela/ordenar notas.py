# Lista de calificaciones de los alumnos
notas = [85, 42, 93, 67, 28, 75]


# ==========================================================
# BUBBLE SORT
# ==========================================================

def bubble_sort(lista):

    # Obtenemos la longitud total de la lista
    n = len(lista)

    # Iteramos sobre la lista para realizar los pases necesarios
    for i in range(n):

        # Bandera para verificar si ocurrió algún cambio en esta iteración
        intercambio = False

        # Comparamos pares adyacentes hasta la sección no ordenada
        # Descartamos los últimos i elementos que ya están en su lugar correcto
        for j in range(0, n-i-1):

            # Evaluamos si el elemento actual supera al siguiente
            if lista[j] > lista[j+1]:

                # Reorganizamos los dos valores en la lista
                lista[j], lista[j+1] = lista[j+1], lista[j]

                # Registramos que se realizó al menos una permuta
                intercambio = True

        # Si no se realizaron cambios, la lista se encuentra totalmente ordenada
        if not intercambio:
            break


# Ejecutamos el algoritmo Bubble Sort sobre la lista original
bubble_sort(notas)

# Imprimimos el resultado final del ordenamiento
print(f"Estas son las notas ordenadas con Bubble Sort: {notas}")


# ==========================================================
# SELECTION SORT
# ==========================================================

# Definimos una copia limpia de las calificaciones para el segundo algoritmo
notas2 = [85, 42, 93, 67, 28, 75]


def selection_sort(lista):

    # Determinamos el número total de elementos
    n = len(lista)

    # Avanzamos posición por posición a través del arreglo
    for i in range(n - 1):

        # Establecemos el índice actual como la ubicación del valor mínimo tentativo
        idx_min = i

        # Exploramos el resto de la lista para buscar un valor inferior
        for j in range(i + 1, n):

            # Detectamos si existe un valor menor al mínimo registrado
            if lista[j] < lista[idx_min]:

                # Actualizamos la posición del elemento más pequeño hallado
                idx_min = j

        # Colocamos el valor mínimo encontrado en la posición i correspondiente
        if idx_min != i:
            lista[i], lista[idx_min] = lista[idx_min], lista[i]


# Aplicamos Selection Sort a la lista secundaria
selection_sort(notas2)

# Imprimimos la lista procesada por Selection Sort
print(f"Estas son las notas ordenadas con Selection Sort: {notas2}")


# ==========================================================
# MÍNIMA, MÁXIMA Y PROMEDIO
# ==========================================================

# Extraemos el valor más bajo presente en el conjunto
minima = min(notas)

# Extraemos el valor más alto del conjunto
maxima = max(notas)

# Calculamos la media aritmética dividiendo la suma total entre el número de elementos
promedio = sum(notas) / len(notas)


# Presentamos el desglose de métricas calculadas
print("Resultados:")

print(f"Nota mínima: {minima}")

print(f"Nota máxima: {maxima}")

print(f"Promedio: {promedio}")