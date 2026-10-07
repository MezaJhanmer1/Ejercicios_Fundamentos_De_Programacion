# PASO 1: guardamos un texto con espacios de sobra al inicio y al final
cadena = "  Python es divertido  "

# PASO 2: .strip() quita esos espacios de los extremos
# El resultado se guarda en "limpia". "cadena" no cambia.
limpia = cadena.strip()

# PASO 3: mostramos el texto limpio entre comillas
# para ver que ya no hay espacios de sobra
print(f"Cadena limpia: '{limpia}'")

# PASO 4: len() cuenta los caracteres del texto limpio
# "Python es divertido" tiene 20 caracteres
print(f"Cantidad de caracteres: {len(limpia)}")