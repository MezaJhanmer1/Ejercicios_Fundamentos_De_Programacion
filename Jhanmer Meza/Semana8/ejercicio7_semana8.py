# Ejercicio 07 – Extracción de Datos de Texto

# Lista original con los datos de las personas mezclados en un texto
registros = [
    'Andrea Salas -edad:25 -tel:987654321',
    'Tommy Solis -edad:30 -tel:912345678'
]

lista_persona = []  # Lista vacía para guardar los datos organizados.

for registro in registros:  # Recorre cada registro de la lista.
    partes = registro.split(" -")
    # Divide el texto usando " -" como separador y crea una lista con 3 partes.

    nombre = partes[0]  # Extrae el nombre, que está en la primera posición.

    edad_texto = partes[1].replace("edad:", "")
    # Elimina "edad:" y deja solamente el número como texto.
    edad = int(edad_texto)  # Convierte la edad de texto a número entero.

    telefono = partes[2].replace("tel:", "")
    # Elimina "tel:" y deja solamente el número de teléfono.

    diccionario_persona = {
        "nombre": nombre,
        "edad": edad,
        "telefono": telefono
    }
    # Organiza los datos extraídos en un diccionario.

    lista_persona.append(diccionario_persona)
    # Agrega el diccionario a la lista. Se repite con cada registro.

# Mostrar la lista con los datos organizados
print("--- LISTA DE DICCIONARIO ---")
print(lista_persona)
print("-" * 50)

# Recorrer la lista para mostrar los datos de forma más clara
print("--- REPORTE (Desarmando la lista) ---")
for persona in lista_persona:
    print("Nombre:", persona["nombre"], "| Edad:", persona["edad"],
          "años | Teléfono:", persona["telefono"])