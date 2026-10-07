# Definimos una función que recibe un texto y una lista de palabras prohibidas
def censurar(texto, palabras_prohibidas):

    # recorremos cada palabra prohibida de la lista
    for palabra in palabras_prohibidas:

         
        # reemplazamos esa palabra en el texto
        # "*" * len(palabra) crea tantos asteriscos como letras tenga la palabra
        # Ejemplo: "feas" (4 letras) → "****"
        texto = texto.replace(palabra, "*" * len(palabra))


    #  devolvemos el texto ya censurado
    return texto


# Texto original que queremos censurar
texto = "El examen fue dificil y el profesor lo jalo del curso."

# Lista de palabras que queremos ocultar
prohibidas = ["dificil", "jalo"]

# Mostramos el resultado de la función
print(censurar(texto, prohibidas))