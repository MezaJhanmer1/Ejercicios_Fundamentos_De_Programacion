# Ejercicio 02 – Ordenamiento alfanumérico de nombres

nombres = ['Carlos', 'ana', 'Beatriz', 'david', 'Elena']        # Lista original de nombres

lista_alfabetica = nombres[:]               # Copia la lista original usando slicing para no modificarla
lista_alfabetica.sort(key=str.lower)        # Ordena la copia alfabéticamente ignorando mayúsculas/minúsculas
lista_descendente = sorted(nombres, key=str.lower, reverse=True)  # Crea una nueva lista ordenada de forma descendente

print("1) Lista original sin modificar:")
print(nombres)

print("2) Lista ordenada alfabéticamente (con sort):")
print(lista_alfabetica)

print("3) Nueva lista en orden descendente (con sorted):")
print(lista_descendente)