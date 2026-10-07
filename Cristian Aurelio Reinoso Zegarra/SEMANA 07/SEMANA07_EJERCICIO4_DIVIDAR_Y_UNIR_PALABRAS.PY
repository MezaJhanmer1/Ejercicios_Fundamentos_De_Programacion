# guardamos un texto con palabras separadas por comas
cadena = "rojo,verde,azul,amarillo"

#.split(",") corta el texto cada vez que encuentra una coma
# Resultado: una lista con 4 colores
# ["rojo", "verde", "azul", "amarillo"]
colores = cadena.split(",")

# recorremos la lista y ponemos cada color en MAYÚSCULAS
# con .upper(). El resultado se guarda en una lista nueva
# ["ROJO", "VERDE", "AZUL", "AMARILLO"]
colores_mayus = [color.upper() for color in colores]

# unimos los colores en un solo texto usando " | " como separador
# Resultado: "ROJO | VERDE | AZUL | AMARILLO"
resultado = " | ".join(colores_mayus)

 # mostramos el resultado en pantalla
print(resultado)