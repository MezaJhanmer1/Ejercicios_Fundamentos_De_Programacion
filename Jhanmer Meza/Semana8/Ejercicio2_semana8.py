#Ejercicio02 – Ordenamiento Alfanumérico de Nombres

nombres = ['Carlos', 'ana', 'Beatriz', 'david', 'Elena']  # Lista original

lista_alfabetica = nombres[:]  # Copia la lista original usando slicing [:].

lista_alfabetica.sort(key=str.lower)
# sort() ordena la lista original de esta variable alfabéticamente,
# ignorando mayúsculas y minúsculas. Modifica la lista directamente.

lista_descendente = sorted(nombres, key=str.lower, reverse=True)
# sorted() crea una nueva lista ordenada de forma descendente (Z a A).
# reverse=True invierte el orden alfabético y no modifica la lista original.

print("1) Lista original sin modificar:")
print(nombres)

print("2) Lista ordenada alfabéticamente (con sort):")
print(lista_alfabetica)

print("3) Nueva lista en orden descendente (con sorted):")
print(lista_descendente)