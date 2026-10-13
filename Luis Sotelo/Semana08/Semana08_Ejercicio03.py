#Ejercicio03 – Búsqueda Simple en Lista de Emails

emails = ['ana@gmail.com', 'luis@outlook.com', 'mia@gmail.com', 'juan@yahoo.com']

contar_gmail = 0                                # Contar cuántos son de Gmail
for correo in emails:
    if "gmail" in correo:                       # si el texto "gmail" esta en correo
        contar_gmail = contar_gmail + 1         # se agrega al contador

emails_com = []                                 # Punto 2: Filtrar los que terminan en '.com'
for correo in emails:               
    if correo.endswith(".com"):                 #si correo termina en .com
        emails_com.append(correo)               #agrega a la lista vacia emails_com el correo

if "luis@outlook.com" in emails:                 #si el correo esta en emails, toma valor verdadero y muestra print
    lista_luis = "Sí está en la lista."
else:
    lista_luis = "No está en la lista."

print("1) Cantidad de emails que son de dominio Gmail:")
print(f'Existen {contar_gmail} correos Gmail.')
print("-" * 40)

print("2) Emails que terminan en '.com':")
print(emails_com)
print("-" * 40)

print("3) ¿Está 'luis@outlook.com' en la lista?")
print(lista_luis)