#Un profesor tiene las notas de 6 estudiantes en una lista desordenada:
notas =[85, 42, 93, 67, 28, 75]
#lista usando burbuja
def burbuja(notas):
    n = len(notas)
    for i in range(n):
        for j in range(0, n-i-1):
            if notas[j] > notas[j+1]:
                notas[j], notas[j+1] = notas[j+1], notas[j]
    return notas

# Ordenar las notas
notas_ordenadas = burbuja(notas)
print("Notas ordenadas:", notas_ordenadas)

#usando el metodo de seleccion sort
def seleccion(notas):
    n = len(notas)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if notas[j] < notas[min_idx]:
                min_idx = j
        notas[i], notas[min_idx] = notas[min_idx], notas[i]
    return notas

notas_ordenadas = seleccion(notas)
print("Notas ordenadas (selección):", notas_ordenadas)

#mostrando minimo , maximo y promedio
minimo = min(notas)
maximo = max(notas)
promedio = sum(notas) / len(notas)
print("Nota mínima:", minimo)
print("Nota máxima:", maximo)
print("Promedio de notas:", promedio)