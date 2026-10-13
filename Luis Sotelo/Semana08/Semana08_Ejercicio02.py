#Ejercicio02 – Ordenamiento Alfanumérico de Nombres

nombres = ['Carlos', 'ana', 'Beatriz', 'david', 'Elena']        # Lista original

lista_alfabetica = nombres[:]               # el parametro[:] (slicing) toma todo de la var NOMBRES y duplica en una nueva variable.
lista_alfabetica.sort(key=str.lower)        # aplica sort a la lista_alfab.. para ignorar mayus..
lista_descendente = sorted(nombres, key=str.lower, reverse=True)        # Paso 3: Crear la lista ordenada en orden descendente


print("1) Lista original sin modificar:")
print(nombres)

print("2) Lista ordenada alfabéticamente (con sort):")
print(lista_alfabetica)

print("3) Nueva lista en orden descendente (con sorted):")
print(lista_descendente)