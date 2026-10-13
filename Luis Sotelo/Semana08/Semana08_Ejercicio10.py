
import re                                        #  Importamos la librería de expresiones regulares

parrafo = "Python es divertido, muy divertido. El código en Python es limpio y Python es genial."

# TAREA 1: Extraer todas las palabras usando regex (letras y apóstrofes)
palabras = re.findall(r"[a-zA-ZáéíóúÁÉÍÓÚñÑ']+", parrafo)   # busca en el texto  las partes que coincidan con parrafo y termina en ., o space
                                                            # Guarda una lista limpia de palabras sueltas en la var palabras

frecuencias = {}                                # crear un diccionario vacío
for p in palabras:                              # desarmar la lista de palabras usando la var p y
    p_min = p.lower()                           # pasar la palabra a minúsculas
    
    frecuencias[p_min] = frecuencias.get(p_min, 0) + 1      # Si ya existe le suma 1, si no, lo inicia en 1
                                                            # Busca en el dicc si ya esta palabra. Si es V dame el # de veces que aparecio
                                                            # si es la 1era vez devuelve un 0

def criterios_orden(palabra):
    return (-frecuencias[palabra], palabra)                 # invierte el sentido para ese dato al tener "-frecuencias" de mayor a menor
                                                            # Ordena por su texto de la A a la Z para desempates

palabras_ordenadas = sorted(frecuencias, key=criterios_orden)    #toma "palabras" del dicc "frecuencias" y las ordena con esa funcion

top_5 = palabras_ordenadas[:5]                              # usa slicing para tomar los 1eros 5 elementos de la lista que ya está ordenada

palabras_unicas = []                                        # Crea una lista vacía
for p in palabras_ordenadas:
    if frecuencias[p] == 1:                                 # El conteo de esta palabra es igual a 1?
        palabras_unicas.append(p)                           # apareció una sola vez en todo el texto, por lo que la agrega a la lista

palabras_unicas.sort()                                      # Ordenar las palabras únicas alfabéticamente


print("           ANALIZADOR DE TEXTO           ")
print(" " * 50)
print("1 y 4) TOP 5 DE PALABRAS MÁS FRECUENTES:")
for indice, p in enumerate(top_5):                          # # Desarma la lista final ya ordenada. enumerate nos da el num fila en indice (0, 1...)
    print(indice + 1, "° Lugar - Palabra:", p, "| Aparece:", frecuencias[p], "veces")

print("-" * 50)

print("4) PALABRAS ÚNICAS ORDENADAS ALFABÉTICAMENTE:")
print(palabras_unicas)
print(" " * 50)
