# Ejercicio 03: Búsqueda simple en una lista de emails
# El programa cuenta los correos Gmail, filtra los que terminan en .com
# y verifica si un correo específico se encuentra en la lista.

# Lista con los correos electrónicos.
emails = ['ana@gmail.com', 'luis@outlook.com', 'mia@gmail.com', 'juan@yahoo.com']

# Inicializar el contador de correos Gmail en cero.
contar_gmail = 0

# Recorrer cada correo de la lista.
for correo in emails:
    # Verificar si el correo contiene la palabra "gmail".
    if "gmail" in correo:
        # Aumentar el contador cuando sea un correo Gmail.
        contar_gmail = contar_gmail + 1

# Crear una lista vacía para guardar los correos que terminan en .com.
emails_com = []

# Recorrer nuevamente la lista de correos.
for correo in emails:
    # Comprobar si el correo termina con ".com".
    if correo.endswith(".com"):
        # Agregar el correo a la lista filtrada.
        emails_com.append(correo)

# Comprobar si el correo de Luis está dentro de la lista original.
if "luis@outlook.com" in emails:
    # Guardar el mensaje si el correo sí existe.
    lista_luis = "Sí está en la lista."
else:
    # Guardar el mensaje si el correo no existe.
    lista_luis = "No está en la lista."

# Mostrar el título y la cantidad de correos Gmail encontrados.
print("1) Cantidad de emails que son de dominio Gmail:")
print(f'Existen {contar_gmail} correos Gmail.')
print("-" * 40)  # Imprimir una línea separadora.

# Mostrar los correos que terminan en .com.
print("2) Emails que terminan en '.com':")
print(emails_com)
print("-" * 40)  # Imprimir una línea separadora.

# Mostrar el resultado de la búsqueda del correo de Luis.
print("3) ¿Está 'luis@outlook.com' en la lista?")
print(lista_luis)
