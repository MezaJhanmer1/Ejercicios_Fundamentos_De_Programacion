# Ejercicio 03 – Búsqueda simple en una lista de emails

emails = ['ana@gmail.com', 'luis@outlook.com', 'mia@gmail.com', 'juan@yahoo.com']  # Lista de correos

# 1) Contar cuántos correos son de Gmail
contar_gmail = 0
for correo in emails:
    if "gmail" in correo:          # ¿El correo contiene "gmail"?
        contar_gmail += 1          # Sí: sumamos 1 al contador

# 2) Filtrar los correos que terminan en ".com"
emails_com = []
for correo in emails:
    if correo.endswith(".com"):    # ¿El correo termina en ".com"?
        emails_com.append(correo)  # Sí: lo agregamos a la lista

# 3) Comprobar si "luis@outlook.com" está en la lista original
if "luis@outlook.com" in emails:
    lista_luis = "Sí está en la lista."
else:
    lista_luis = "No está en la lista."

# Mostrar resultados
print("1) Cantidad de emails que son de dominio Gmail:")
print(f'Existen {contar_gmail} correos Gmail.')
print("-" * 40)

print("2) Emails que terminan en '.com':")
print(emails_com)
print("-" * 40)

print("3) ¿Está 'luis@outlook.com' en la lista?")
print(lista_luis)