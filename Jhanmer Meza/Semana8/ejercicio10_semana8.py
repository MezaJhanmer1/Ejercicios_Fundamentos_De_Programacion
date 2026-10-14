import re  # Importa la librería para trabajar con expresiones regulares.

# Texto que vamos a analizar.
parrafo = "Python es divertido, muy divertido. El código en Python es limpio y Python es genial."

# TAREA 1: Extraer todas las palabras del texto.
palabras = re.findall(r"[a-zA-ZáéíóúÁÉÍÓÚñÑ']+", parrafo)
# Busca todas las palabras, incluyendo letras con tilde, ñ y apóstrofes.
# Devuelve una lista con las palabras encontradas.

frecuencias = {}  # Diccionario vacío para contar las palabras.

for p in palabras:  # Recorre cada palabra extraída.
    p_min = p.lower()  # Convierte la palabra a minúsculas.
    frecuencias[p_min] = frecuencias.get(p_min, 0) + 1
    # Si la palabra existe, aumenta su contador en uno.
    # Si no existe, comienza a contarla desde uno.

# Función que define cómo se ordenarán las palabras.
def criterios_orden(palabra):
    return (-frecuencias[palabra], palabra)
    # Primero ordena por frecuencia de mayor a menor.
    # Si hay empate, ordena alfabéticamente de A a Z.

palabras_ordenadas = sorted(frecuencias, key=criterios_orden)
# Ordena las palabras del diccionario según los criterios anteriores.

top_5 = palabras_ordenadas[:5]
# Usa slicing [:5] para obtener las primeras cinco palabras ordenadas.

palabras_unicas = []  # Lista vacía para guardar palabras que aparecen una vez.

for p in palabras_ordenadas:
    if frecuencias[p] == 1:  # Comprueba si la palabra aparece una sola vez.
        palabras_unicas.append(p)  # Agrega la palabra a la lista.

palabras_unicas.sort()  # Ordena las palabras únicas alfabéticamente.

# Mostrar el ranking de las cinco palabras más frecuentes.
print("           ANALIZADOR DE TEXTO           ")
print(" " * 50)
print("1 y 4) TOP 5 DE PALABRAS MÁS FRECUENTES:")

for indice, p in enumerate(top_5):
    # enumerate() obtiene la posición y la palabra.
    print(indice + 1, "° Lugar - Palabra:", p,
          "| Aparece:", frecuencias[p], "veces")

print("-" * 50)

# Mostrar las palabras que aparecen una sola vez.
print("4) PALABRAS ÚNICAS ORDENADAS ALFABÉTICAMENTE:")
print(palabras_unicas)
print(" " * 50)