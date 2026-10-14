# [PASO 1] Se importa la librería 're' para usar expresiones regulares.
import re                                        

# [PASO 2] Se define el texto que vamos a analizar.
parrafo = "Python es divertido, muy divertido. El código en Python es limpio y Python es genial."

# [PASO 3] TAREA 1: Extraer todas las palabras usando regex.
# La expresión r"[a-zA-ZáéíóúÁÉÍÓÚñÑ']+" busca secuencias de letras (mayúsculas, minúsculas, con tildes, ñ) y apóstrofes.
# Esto ignora automáticamente los espacios, comas, puntos y cualquier otro signo de puntuación.
# Resultado en 'palabras': ['Python', 'es', 'divertido', 'muy', 'divertido', 'El', 'código', 'en', 'Python', 'es', 'limpio', 'y', 'Python', 'es', 'genial']
palabras = re.findall(r"[a-zA-ZáéíóúÁÉÍÓÚñÑ']+", parrafo)   

# [PASO 4] Se crea un diccionario vacío para guardar cuántas veces aparece cada palabra.
frecuencias = {}                                

# [PASO 5] Bucle: recorre cada palabra extraída en el paso 3.
for p in palabras:                              
    
    # [PASO 6] Se convierte la palabra a minúsculas para que "Python" y "python" cuenten como la misma.
    # Iteración 1: p = 'Python' -> p_min = 'python'
    # Iteración 2: p = 'es' -> p_min = 'es'
    # Iteración 3: p = 'divertido' -> p_min = 'divertido'
    p_min = p.lower()                           
    
    # [PASO 7] Se actualiza el diccionario de frecuencias.
    # .get(p_min, 0) busca el valor actual. Si no existe, devuelve 0.
    # Luego se le suma 1.
    # Iteración 1: 'python' no existe -> 0 + 1 = 1
    # Iteración 2: 'es' no existe -> 0 + 1 = 1
    # Iteración 3: 'divertido' no existe -> 0 + 1 = 1
    # Iteración 4: 'muy' no existe -> 0 + 1 = 1
    # Iteración 5: 'divertido' YA existe (vale 1) -> 1 + 1 = 2
    frecuencias[p_min] = frecuencias.get(p_min, 0) + 1      

# [PASO 8] Función de ordenamiento personalizada.
def criterios_orden(palabra):
    # [PASO 9] Retorna una tupla con DOS criterios:
    # 1) -frecuencias[palabra]: El signo menos invierte el orden. Mayor frecuencia primero.
    # 2) palabra: Si hay empate en frecuencia, ordena alfabéticamente (A-Z).
    return (-frecuencias[palabra], palabra)                 

# [PASO 10] Se ordenan las palabras del diccionario usando la función anterior.
# sorted() toma las claves (las palabras) del diccionario 'frecuencias' y las ordena.
palabras_ordenadas = sorted(frecuencias, key=criterios_orden)    

# [PASO 11] Se toman los primeros 5 elementos de la lista ya ordenada.
# Slicing [:5] toma desde el índice 0 hasta el 4.
top_5 = palabras_ordenadas[:5]                              

# [PASO 12] Se crea una lista vacía para las palabras que aparecen una sola vez.
palabras_unicas = []                                        

# [PASO 13] Bucle: recorre todas las palabras ordenadas.
for p in palabras_ordenadas:
    
    # [PASO 14] Si el conteo de esta palabra es exactamente 1...
    if frecuencias[p] == 1:                                 
        # [PASO 15] ...la agregamos a la lista de palabras únicas.
        palabras_unicas.append(p)                           

# [PASO 16] Se ordena la lista de palabras únicas alfabéticamente (A-Z).
palabras_unicas.sort()                                      


# ================= IMPRESIÓN DE RESULTADOS =================

print("           ANALIZADOR DE TEXTO           ")
print(" " * 50)

print("1 y 4) TOP 5 DE PALABRAS MÁS FRECUENTES:")
# [PASO 17] enumerate nos da el índice (0, 1, 2...) y la palabra.
for indice, p in enumerate(top_5):                          
    
    # Iteración 1: indice=0 -> Imprime "1 ° Lugar - Palabra: divertido | Aparece: 2 veces"
    # Iteración 2: indice=1 -> Imprime "2 ° Lugar - Palabra: es | Aparece: 2 veces"
    # Iteración 3: indice=2 -> Imprime "3 ° Lugar - Palabra: python | Aparece: 2 veces"
    # (El orden entre 'divertido', 'es' y 'python' se define alfabéticamente por el segundo criterio, ya que los 3 tienen frecuencia 2)
    print(indice + 1, "° Lugar - Palabra:", p, "| Aparece:", frecuencias[p], "veces")

print("-" * 50)

print("4) PALABRAS ÚNICAS ORDENADAS ALFABÉTICAMENTE:")
# [PASO 18] Se imprime la lista de palabras que aparecieron solo 1 vez.
print(palabras_unicas)
print(" " * 50)