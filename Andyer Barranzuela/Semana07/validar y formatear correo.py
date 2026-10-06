# ==========================================
# ENUNCIADO 5 - VALIDAR Y FORMATEAR CORREO
# ==========================================

# Creamos una función para validar el correo
def validar_correo(email):

    # strip() elimina espacios al inicio y al final
    # lower() convierte todo el correo a minúsculas
    email = email.strip().lower()

    # Verificamos que el correo contenga @ y .
    if "@" in email and "." in email:

        # split("@") divide el correo en dos partes
        # Ejemplo: usuario@gmail.com
        # Resultado: ["usuario", "gmail.com"]
        dominio = email.split("@")[1]

        # Retornamos solamente el dominio
        return dominio

    # Si no contiene @ o ., retornamos None
    else:
        return None


# Pedimos al usuario que ingrese su correo
correo = input("Ingrese su correo electrónico: ")

# Llamamos a la función para validar el correo
dominio = validar_correo(correo)

# Comprobamos si la función encontró un dominio
if dominio:

    # Mostramos que el correo es válido
    print("Correo válido")

    # Mostramos el dominio obtenido
    print("Dominio:", dominio)

else:

    # Mostramos que el correo no es válido
    print("Correo no válido")