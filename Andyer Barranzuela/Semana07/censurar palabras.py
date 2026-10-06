# ==========================================
# ENUNCIADO 6 - CENSURAR PALABRA EN UN TEXTO
# ==========================================

# Creamos una función para censurar palabras
def censurar_texto(texto, palabras_prohibidas):

    # Recorremos todas las palabras prohibidas
    for palabra in palabras_prohibidas:

        # Creamos una cantidad de asteriscos
        # igual al tamaño de la palabra
        asteriscos = "*" * len(palabra)

        # Reemplazamos la palabra por los asteriscos
        texto = texto.replace(palabra, asteriscos)

    # Retornamos el texto ya censurado
    return texto


# Creamos el texto que vamos a analizar
texto = "Python es divertido y aprender Python es interesante."

# Creamos una lista con las palabras que queremos censurar
palabras_prohibidas = ["Python", "divertido"]

# Llamamos a la función para censurar el texto
resultado = censurar_texto(texto, palabras_prohibidas)

# Mostramos el texto original
print("Texto original:")
print(texto)

# Dejamos una línea en blanco
print()

# Mostramos el texto después de censurar las palabras
print("Texto censurado:")
print(resultado)