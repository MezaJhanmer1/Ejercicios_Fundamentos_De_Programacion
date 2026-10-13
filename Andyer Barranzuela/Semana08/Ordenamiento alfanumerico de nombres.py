# Ordenamiento alfanumérico de nombres

# Lista original de nombres.
nombres = ['Carlos', 'ana', 'Beatriz', 'david', 'Elena']

# Copiar la lista original.
lista_alfabetica = nombres[:]

# Ordenar de A a Z ignorando mayúsculas.
lista_alfabetica.sort(key=str.lower)

# Crear una lista ordenada de Z a A.
lista_descendente = sorted(nombres, key=str.lower, reverse=True)

# Mostrar la lista original.
print("1) Lista original sin modificar:")
print(nombres)

# Mostrar la lista ordenada de A a Z.
print("2) Lista ordenada alfabéticamente (con sort):")
print(lista_alfabetica)

# Mostrar la lista ordenada de Z a A.
print("3) Nueva lista en orden descendente (con sorted):")
print(lista_descendente)
