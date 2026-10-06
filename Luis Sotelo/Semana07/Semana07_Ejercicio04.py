#Ejercicio 04 - Dividir y Unir palabras

colores = 'rojo,verde,azul,amarillo'

mayus = colores.upper()         # Queda: 'ROJO,VERDE,AZUL,AMARILLO'

lista_colores = mayus.split(",")  # Separamos por comas

resultado_final = " | ".join(lista_colores)     # Unimos con ' | '

print(resultado_final)