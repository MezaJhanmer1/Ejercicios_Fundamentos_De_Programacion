# ==========================================================
# EJERCICIO 06 - CENSURAR PALABRAS DE TEXTO
# ==========================================================


# Guardamos el texto original en una variable.
texto_inicial = "El user Pepito15 puso de contraseña Pepito322* en Steam"


# Creamos una lista con las palabras que queremos censurar.
palabras_prohibidas = ["Pepito15", "Pepito322*", "Steam"]


# Al inicio contiene el mismo texto original.
texto_censurado = texto_inicial


# Recorremos una por una las palabras de la lista.
for palabra in palabras_prohibidas:

    # len() nos permite saber cuántos caracteres tiene la palabra
  
    largo = len(palabra)

    # Multiplicamos "*" por la cantidad de caracteres.
    asteriscos = "*" * largo

    # replace() busca la palabra dentro del texto
    # y la reemplaza por los asteriscos.
    texto_censurado = texto_censurado.replace(palabra, asteriscos)


# Mostramos el texto original sin modificar.
print("Texto Inicial:")
print(texto_inicial)


# Mostramos el texto después de realizar la censura.
print("Texto censurado:")
print(texto_censurado)