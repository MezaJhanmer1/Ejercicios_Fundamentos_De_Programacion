
# Ejercicio 03 – Búsqueda Simple en Lista de Emails

# Lista original que contiene los correos electrónicos
emails = ['ana@gmail.com', 'luis@outlook.com', 'mia@gmail.com', 'juan@yahoo.com']

# Punto 1: Contar cuántos correos pertenecen a Gmail
contar_gmail = 0  # El contador comienza en cero.

for correo in emails:  # Recorre cada correo de la lista.
    if "gmail" in correo:  # Verifica si el correo contiene la palabra "gmail".
        contar_gmail = contar_gmail + 1  # Aumenta el contador en uno si la condición se cumple.

# Punto 2: Filtrar los correos que terminan en ".com"
emails_com = []  # Lista vacía donde guardaremos los correos encontrados.

for correo in emails:  # Recorre nuevamente todos los correos.
    if correo.endswith(".com"):  # Comprueba si el correo termina en ".com".
        emails_com.append(correo)  # Agrega el correo a la nueva lista.

# Punto 3: Verificar si un correo específico está en la lista
if "luis@outlook.com" in emails:  # Comprueba si el correo existe en la lista.
    lista_luis = "Sí está en la lista."  # Se ejecuta si el correo fue encontrado.
else:
    lista_luis = "No está en la lista."  # Se ejecuta si el correo no fue encontrado.


print("1) Cantidad de emails que son de dominio Gmail:")
print(f'Existen {contar_gmail} correos Gmail.')
print("-" * 40)  # Imprime una línea de 40 guiones como separador.


print(emails_com)
print("-" * 40)

print("3) ¿Está 'luis@outlook.com' en la lista?")
print(lista_luis)