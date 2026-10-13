# Ejercicio 07: Extracción de datos de registros
# Separar los datos de cada persona y guardarlos en diccionarios.

# Lista con los datos de las personas.
registros = [
    'Andrea Salas -edad:25 -tel:987654321',
    'Tommy Solis -edad:30 -tel:912345678'
]

# Crear una lista vacía para guardar los datos separados.
lista_persona = []

# Recorrer cada registro.
for registro in registros:
    # Separar el nombre, la edad y el teléfono.
    partes = registro.split(" -")
    nombre = partes[0]

    # Extraer y convertir la edad a número entero.
    edad_texto = partes[1].replace("edad:", "")
    edad = int(edad_texto)

    # Extraer el número de teléfono.
    telefono = partes[2].replace("tel:", "")

    # Guardar los datos en un diccionario.
    diccionario_persona = {
        "nombre": nombre,
        "edad": edad,
        "telefono": telefono
    }

    # Agregar el diccionario a la lista.
    lista_persona.append(diccionario_persona)

# Mostrar la lista de personas.
print("--- LISTA DE DICCIONARIO ---")
print(lista_persona)
print("-" * 50)

# Mostrar los datos de cada persona por separado.
print("--- REPORTE (Desarmando la lista) ---")
for persona in lista_persona:
    print("Nombre:", persona["nombre"], "| Edad:", persona["edad"], "años | Teléfono:", persona["telefono"])
