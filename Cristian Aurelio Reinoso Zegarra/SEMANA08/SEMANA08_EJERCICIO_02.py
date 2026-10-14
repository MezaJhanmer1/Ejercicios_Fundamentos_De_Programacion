# Inicializa la lista original con 5 nombres. 
# Nota que hay mayúsculas y minúsculas mezcladas a propósito.
nombres = ['Carlos', 'ana', 'Beatriz', 'david', 'Elena']


# 1) Imprimir sin modificar
# Muestra la lista tal cual se creó. No se ha ordenado nada aún.
# Salida esperada: ['Carlos', 'ana', 'Beatriz', 'david', 'Elena']
print("1) Lista original:", nombres)

# 2) Ordenar alfabéticamente ignorando mayúsculas con sort()
# .sort() modifica la lista original EN SU LUGAR (no crea una nueva lista).
# key=str.lower convierte temporalmente todo a minúsculas para comparar de forma justa (a, b, c...).
# La variable 'nombres' ahora queda modificada en orden ascendente.
nombres.sort(key=str.lower)
# Salida esperada: ['ana', 'Beatriz', 'Carlos', 'david', 'Elena']
print("2) Orden alfabetico (con sort):", nombres)

# 3) Crear una nueva lista ordenada en orden descendente con sorted()
# sorted() crea una NUEVA lista (no modifica la variable 'nombres' original).
# key=str.lower ignora mayúsculas/minúsculas para que el orden alfabético sea real.
# reverse=True invierte el resultado para que vaya de la Z a la A.
descendente = sorted(nombres, key=str.lower, reverse=True)
# Salida esperada: ['Elena', 'david', 'Carlos', 'Beatriz', 'ana']
print("3) Orden descendente (con sorted):", descendente)


#1) Lista original: ['Carlos', 'ana', 'Beatriz', 'david', 'Elena']
#2) Orden alfabetico (con sort): ['ana', 'Beatriz', 'Carlos', 'david', 'Elena']
#3) Orden descendente (con sorted): ['Elena', 'david', 'Carlos', 'Beatriz', 'ana'