# EJERCICIO 05 - VALIDAR CORREO


# Creamos una función llamada "validar_dominio".
def validar_dominio(email):

    # .strip() elimina los espacios que están al inicio y al final.
    # .lower() convierte todo el correo a minúsculas.
    # Guardamos el resultado en la variable "email_limpio".
    email_limpio = email.strip().lower()


    # Verificamos si el símbolo "@" existe dentro del correo.
    # Si existe, continuamos con la validación.
    if "@" in email_limpio:

        # Usamos .split("@") para dividir el correo
        # cada vez que encuentra el símbolo "@".
        # Se convierte en:
        # ["juan.perez", "gmail.com"]
        partes = email_limpio.split("@")


        # [1] significa que estamos tomando el segundo elemento de lista
        # partes[1] = "gmail.com"
        dominio = partes[1]

        # Verificamos si el dominio contiene un punto ".".
        if "." in dominio:

            # Si el dominio tiene un punto,devolvemos el dominio (gmail.com)
            return dominio

    # Si no tiene "@" o el dominio no tiene ".",
    # devolvemos el mensaje de correo no válido.
    return "Email no válido"


print(validar_dominio("  Juan.PerEZ@GmaIl.com  "))

print(validar_dominio("  Juan_15_tlv@GmaIl.COM  "))

print(validar_dominio("juan.perEZ@gmail"))