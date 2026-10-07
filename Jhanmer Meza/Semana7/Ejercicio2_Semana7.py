# EJERCICIO 2 - LIMPIAR Y CONTAR

# Guardamos un texto en la variable "texto".
# El texto tiene espacios al inicio y al final.
texto = ' Python es divertido '


# Usamos .strip() para eliminar los espacios
# que se encuentran al inicio y al final del texto.
limpiar = texto.strip()


# Usamos len() para contar la cantidad de caracteres
# que tiene el texto después de eliminar los espacios.
total_caracteres = len(limpiar)


# Mostramos el texto ya limpio.
# Las comillas simples nos permiten ver claramente el contenido.
print(f"Texto limpio: '{limpiar}'")


# Mostramos la cantidad total de caracteres del texto limpio.
print(f"Número de caracteres: {total_caracteres}")