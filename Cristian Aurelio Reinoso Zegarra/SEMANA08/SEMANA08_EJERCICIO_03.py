# Se crea la lista en la memoria con 4 correos.
emails = ['ana@gmail.com', 'luis@outlook.com', 'mia@gmail.com', 'juan@yahoo.com']

# 1) Contar emails de Gmail
# Se inicializa una variable contadora en 0.
contador_gmail = 0

# Bucle for: recorre la lista elemento por elemento.
for email in emails:
    if '@gmail.com' in email:
        contador_gmail += 1

#Se imprime el resultado final del contador.
#IMPRIME EN PANTALLA: 1) Emails de Gmail: 2
print(f"1) Emails de Gmail: {contador_gmail}")




# 2) Mostrar solo los que terminan en '.com'
# Se imprime un encabezado en pantalla.
print("2) Emails que terminan en '.com':")

# Bucle for: recorre la lista de nuevo.
for email in emails:
    if email.endswith('.com'):
        print(" -", email)




# 3) Verificar si 'luis@outlook.com' está en la lista

#Condicional if-else. 
# Python revisa toda la lista. 'luis@outlook.com' SÍ existe (posición 2).
# Como la condición es True, se ejecuta el bloque if y se guarda el texto en 'lista_luis'.
if 'luis@outlook.com' in emails:
    lista_luis = "Sí, luis@outlook.com está en la lista"
else:
    lista_luis = "No está en la lista"

#Se imprime la pregunta.
print("3) ¿Está 'luis@outlook.com' en la lista?")

# Se imprime la variable 'lista_luis' que guardamos en el paso 7.
print(lista_luis)



# 1) Emails de Gmail: 2
# 2) Emails que terminan en '.com':
#  - ana@gmail.com
#  - luis@outlook.com
#  - mia@gmail.com
#  - juan@yahoo.com
# 3) ¿Está 'luis@outlook.com' en la lista?
# Sí, luis@outlook.com está en la lista