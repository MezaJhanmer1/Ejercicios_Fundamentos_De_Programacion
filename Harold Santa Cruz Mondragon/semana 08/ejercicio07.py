# Ejercicio 07 – Extracción de datos desde registros de texto

registros = [
    'Andrea Salas -edad:25 -tel:987654321',                   # Registros con la información mezclada en un solo string
    'Tommy Solis -edad:30 -tel:912345678'
]

lista_persona = []                                          # Lista vacía donde se guardarán los diccionarios resultantes

for registro in registros:                                  # Recorre cada registro de la lista original
    partes = registro.split(" -")                           # Divide el string en 3 partes: [nombre, edad, teléfono]
    nombre = partes[0]                                      # La posición 0 corresponde al nombre

    edad_texto = partes[1].replace("edad:", "")             # En la posición 1 viene "edad:25"; el replace quita "edad:" y deja solo "25"
    edad = int(edad_texto)                                  # Convierte el texto "25" a número entero
    telefono = partes[2].replace("tel:", "")                # En la posición 2 viene "tel:987654321"; el replace quita "tel:" y deja solo el número

    diccionario_persona = {                                 # Empaqueta las 3 variables extraídas en un diccionario
        "nombre": nombre,
        "edad": edad,
        "telefono": telefono
    }

    lista_persona.append(diccionario_persona)               # Agrega el diccionario a la lista final y repite con el siguiente registro

print("--- LISTA DE DICCIONARIO ---")
print(lista_persona)
print("-" * 50)

print("--- REPORTE (Desarmando la lista) ---")
for persona in lista_persona:                               # Recorre cada diccionario y muestra sus datos con acceso por clave
    print("Nombre:", persona["nombre"], "| Edad:", persona["edad"], "años | Teléfono:", persona["telefono"])