# ==========================================
# ENUNCIADO 4 - DIVIDIR Y UNIR PALABRAS
# ==========================================

# Creamos la cadena con los colores separados por comas
cadena = "rojo,verde,azul,amarillo"

# split(",") divide la cadena cada vez que encuentra una coma
colores = cadena.split(",")

# Creamos una lista vacía para guardar los colores en mayúsculas
colores_mayusculas = []

# Recorremos cada color de la lista
for color in colores:

    # Convertimos cada color a mayúsculas
    color_mayuscula = color.upper()

    # Agregamos el color convertido a la nueva lista
    colores_mayusculas.append(color_mayuscula)

# join() une todos los colores utilizando " | " como separador
resultado = " | ".join(colores_mayusculas)

# Mostramos el resultado final
print(resultado)