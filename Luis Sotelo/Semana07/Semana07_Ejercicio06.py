#Ejercicio 06 - Censurar palabras de texto

texto_inicial = "El user Pepito15 puso de contraseña Pepito322* en Steam"
palabras_prohibidas = ["Pepito15", "Pepito322*", "Steam"]           #lista para censurar


texto_censurado = texto_inicial         # variable para usar una copia del texto original


for palabra in palabras_prohibidas:     # Recorrer cada palabra de la lista de prohibidas
    
    largo = len(palabra)                # Medir la cantidad de la palabra prohibida (8, 10 y 5)
    asteriscos = "*" * largo            # multiplicar un carácter por un número lo repite esa cantidad de veces.
    texto_censurado = texto_censurado.replace(palabra, asteriscos)      #Reemplazar la palabra por los asteriscos en el texto
                                        #guarda el texto a reemplazar de "palabra" que es igual a "Pepito15" y reemplaza con asteriscos

print("Texto Inicial:")
print(texto_inicial)
print("Texto censurado:")
print(texto_censurado)