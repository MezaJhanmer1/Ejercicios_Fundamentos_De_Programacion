# EJERCICIO 04 - DIVIDIR Y UNIR PALABRAS


# Guardamos varios colores en una sola cadena de texto.
colores = 'rojo,verde,azul,amarillo'


# Usamos .upper() para convertir todos los colores
# de minúsculas a MAYÚSCULAS.
mayus = colores.upper()


# Usamos .split(",") para separar el texto cada vez
# que encuentra una coma.
# El resultado se convierte en una lista.
lista_colores = mayus.split(",")


# Usamos .join() para unir nuevamente los elementos de la lista.
# En este caso, colocamos " | " entre cada color.
resultado_final = " | ".join(lista_colores)

print(resultado_final)