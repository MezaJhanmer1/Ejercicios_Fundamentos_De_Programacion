# Lista de notas de los estudiantes
notas = [85, 42, 93, 67, 28, 75]


# ==========================================================
# BUBBLE SORT
# ==========================================================

def bubble_sort(lista):

    # Guardamos la cantidad de elementos de la lista
    n = len(lista)

    # Recorremos la lista varias veces
    for i in range(n):

        # Esta variable nos indica si hubo algún intercambio
        intercambio = False

        # Comparamos los elementos que están juntos
        # n-i-1 evita revisar los elementos que ya están ordenados
        for j in range(0, n-i-1):

            # Si el elemento de la izquierda es mayor
            # que el elemento de la derecha
            if lista[j] > lista[j+1]:

                # Intercambiamos las posiciones
                lista[j], lista[j+1] = lista[j+1], lista[j]

                # Indicamos que hubo un intercambio
                intercambio = True

        # Si no hubo ningún intercambio,
        # significa que la lista ya está ordenada
        if not intercambio:
            break


# Llamamos a la función para ordenar las notas
bubble_sort(notas)

# Mostramos las notas ordenadas
print(f"Estas son las notas ordenadas con Bubble Sort: {notas}")


# ==========================================================
# SELECTION SORT
# ==========================================================

# Creamos otra lista porque vamos a utilizar
# Selection Sort por separado
notas2 = [85, 42, 93, 67, 28, 75]


def selection_sort(lista):

    # Guardamos la cantidad de elementos
    n = len(lista)

    # Recorremos la lista hasta el penúltimo elemento
    for i in range(n - 1):

        # Suponemos que el elemento de la posición i
        # es el menor de la parte que falta ordenar
        idx_min = i

        # Buscamos un elemento menor hacia adelante
        for j in range(i + 1, n):

            # Si encontramos un elemento menor
            if lista[j] < lista[idx_min]:

                # Guardamos la posición del nuevo menor
                idx_min = j

        # Si encontramos un elemento menor,
        # lo intercambiamos con el elemento actual
        if idx_min != i:
            lista[i], lista[idx_min] = lista[idx_min], lista[i]


# Llamamos a la función Selection Sort
selection_sort(notas2)

# Mostramos las notas ordenadas
print(f"Estas son las notas ordenadas con Selection Sort: {notas2}")


# ==========================================================
# MÍNIMA, MÁXIMA Y PROMEDIO
# ==========================================================

# min() busca la nota más pequeña de la lista
minima = min(notas)

# max() busca la nota más grande de la lista
maxima = max(notas)

# sum() suma todas las notas
# len() obtiene la cantidad de notas
# Dividimos la suma entre la cantidad para obtener el promedio
promedio = sum(notas) / len(notas)


# Mostramos los resultados
print("Resultados:")

print(f"Nota mínima: {minima}")

print(f"Nota máxima: {maxima}")

print(f"Promedio: {promedio}")