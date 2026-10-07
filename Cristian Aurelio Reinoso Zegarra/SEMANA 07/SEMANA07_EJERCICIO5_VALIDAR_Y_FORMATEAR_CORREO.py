# Definimos una función llamada obtener_dominio
# Recibe un email y devuelve el dominio
def obtener_dominio(email):

    # limpiamos el email
    # .strip() quita espacios de los extremos
    # .lower() pone todo en minúsculas
    email = email.strip().lower()

    # revisamos que tenga "@" y "."
    # Si tiene los dos, seguimos. Si no, salta al final.
    if "@" in email and "." in email:

        # cortamos el email en dos partes usando el "@"
        # split("@", 1) corta solo en el primer "@"
        # usuario = lo de la izquierda
        # dominio = lo de la derecha
        usuario, dominio = email.split("@", 1)


        # revisamos que el dominio tenga un "."
        if "." in dominio:
            # Si sí tiene punto, devolvemos el dominio
            return dominio


    # si algo falló arriba, devolvemos este mensaje
    return "Correo inválido"



# Prueba 1: email con espacios y mayúsculas
# Se limpia, se corta y devuelve "ejemplo.com"
print(obtener_dominio("  USUARIO@Gmail.COM  "))  # ejemplo.com

# Prueba 2: email sin "@"
# No pasa la revisión, devuelve "Correo inválido"
print(obtener_dominio("correo.com"))     # Correo inválido
