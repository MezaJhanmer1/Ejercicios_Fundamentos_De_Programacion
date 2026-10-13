    #Ejercicio 07 – Extracción con Expresiones Regulares

registros = [
    'Andrea Salas -edad:25 -tel:987654321',                   # Lista original con la información mezclada
    'Tommy Solis -edad:30 -tel:912345678'
]

lista_persona = []                                          #crear la lista vacia

for registro in registros:                                  # Para registro en lista registros, desarmamos la lista  
    partes = registro.split(" -")                           # divide el string y retorna en 3 partes [ nombre, edad, tel].
    nombre = partes[0]                                      # toma el indice 0 (nombre) y lo guarda en la variable nombre
    
    edad_texto = partes[1].replace("edad:", "")      # indice 1: "edad:25", el replace quita "edad:" y la borra y pone "" para dejar solo el texto 25
    edad = int(edad_texto)                           # el texto: 25 lo convertimos a número entero
    telefono = partes[2].replace("tel:", "")         # indice 2: "tel:", el replace quita "tel:" y la borra y pone "" para dejar solo el numero

    diccionario_persona = {                          # Toma las 3 variables q acabamos de extraer(nombre, edad, telefono) 
        "nombre": nombre,                            # y las empaqueta dentro de un diccionario
        "edad": edad,
        "telefono": telefono
    }
    
    lista_persona.append(diccionario_persona)       # toma el diccionario y lo mete a lista_persona, se repite con el otro dato

print("--- LISTA DE DICCIONARIO ---")
print(lista_persona)
print("-" * 50)

print("--- REPORTE (Desarmando la lista) ---")
for persona in lista_persona:
    print("Nombre:", persona["nombre"], "| Edad:", persona["edad"], "años | Teléfono:", persona["telefono"])