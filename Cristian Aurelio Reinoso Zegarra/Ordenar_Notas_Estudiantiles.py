# 1. DEFINICIÓN DE LA LISTA INICIAL

notas = [85, 42, 93, 67, 28, 75]  # Define la lista original 


# 2. ORDENANMIENTO USANDO BUBBLE SORT

notas_burbuja = notas.copy()  # Crea una copia independiente para no modificar 'notas'
n = len(notas_burbuja)        # Obtiene el tamaño total de la lista (6)

for i in range(n):            # Bucle externo: controla el numero de pasadas generales
    for j in range(0, n - i - 1):  # Bucle interno: compara elementos adyacentes no ordenados
        if notas_burbuja[j] > notas_burbuja[j + 1]:  # Evalua si el de la izquierda es mayor
            # INTERCAMBIO MANUAL USANDO VARIABLE TEMPORAL:
            temp = notas_burbuja[j]                  # Guarda el valor actual en variable auxiliar
            notas_burbuja[j] = notas_burbuja[j + 1]  # Coloca el menor en la posición actual
            notas_burbuja[j + 1] = temp              # Coloca el mayor guardado en la posición derecha

print("a) Notas ordenadas con Bubble Sort:", notas_burbuja)  # Muestra el resultado final ordenado


# 3. ORDENAMIENTO USANDO SELECTION SORT 

notas_seleccion = notas.copy()  # Crea otra copia independiente de la lista original
n = len(notas_seleccion)        # Recalcula la longitud de la lista

for i in range(n - 1):          # Bucle externo: recorre la lista hasta la penúltima posición
    idx_min = i                 # Asume que el valor menor actual está en el índice 'i'
    for j in range(i + 1, n):   # Bucle interno: busca en el resto de la lista si hay otro menor
        if notas_seleccion[j] < notas_seleccion[idx_min]:  # Compara el elemento 'j' con el mínimo actual
            idx_min = j         # Si encuentra uno más pequeño, actualiza el índice del mínimo

    # INTERCAMBIO DEL ELEMENTO MÍNIMO ENCONTRADO A LA POSICIÓN ACTUAL 'i':
    temp = notas_seleccion[i]                      # Guarda el valor inicial en variable auxiliar
    notas_seleccion[i] = notas_seleccion[idx_min]  # Mueve el número menor a la posición 'i'
    notas_seleccion[idx_min] = temp                # Mueve el valor antiguo a donde estaba el menor

print("b) Notas ordenadas con Selection Sort:", notas_seleccion)  # Muestra la lista ordenada


# 4. MINIMO, MAXIMO Y PROMEDIO

nota_min = min(notas)               # Usa min() para extraer la nota mas baja
nota_max = max(notas)               # Usa max() para extraer la nota mas alta
suma_notas = sum(notas)             # Suma la totalidad de los valores contenidos en la lista
promedio = suma_notas / len(notas)  # Divide la suma total entre la cantidad de notas

print("c) Resultados finales:")
print("   Nota minima:", nota_min)       # 28
print("   Nota maxima:", nota_max)       # 93
print("   Promedio de notas:", promedio) # 65.0