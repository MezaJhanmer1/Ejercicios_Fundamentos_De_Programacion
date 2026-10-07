# EJERCICIO 03 - EXTRAER PALABRAS EXACTAS


# Guardamos una frase completa en la variable "texto".
texto = 'Análisis de Datos con Python'


# Utilizamos slicing [12:17] para extraer la palabra "Datos".
# El índice 12 indica dónde empieza la palabra "Datos".
# El índice 17 indica dónde termina el rango.

datos = texto[12:17]


# Utilizamos slicing [22:] para extraer "Python".
# El índice 22 indica dónde empieza la palabra y los : en la derecha es hasta el final de ese lado .

python = texto[22:]

print(f"Primera palabra extraída: {datos}")

print(f"Segunda palabra extraída: {python}")