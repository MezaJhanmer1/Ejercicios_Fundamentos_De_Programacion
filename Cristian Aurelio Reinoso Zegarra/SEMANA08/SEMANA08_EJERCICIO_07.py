# [PASO 1] Se crea la lista original con dos strings (cada uno es un registro).
registros = [
    'Andrea Salas -edad:25 -tel:987654321',                   
    'Tommy Solis -edad:30 -tel:912345678'
]

# [PASO 2] Se crea una lista vacía donde guardaremos los diccionarios finales.
lista_persona = []                                          

# [PASO 3] Bucle externo: recorre la lista de registros uno por uno.
# Iteración 1: registro = 'Andrea Salas -edad:25 -tel:987654321'
# Iteración 2: registro = 'Tommy Solis -edad:30 -tel:912345678'
for registro in registros:                                  
    
    # [PASO 4] .split(" -") divide el string usando " -" como separador.
    # Iteración 1: partes = ['Andrea Salas', 'edad:25', 'tel:987654321']
    # Iteración 2: partes = ['Tommy Solis', 'edad:30', 'tel:912345678']
    partes = registro.split(" -")                           
    
    # [PASO 5] Se extrae el nombre (posición 0 de la lista 'partes').
    # Iteración 1: nombre = 'Andrea Salas'
    # Iteración 2: nombre = 'Tommy Solis'
    nombre = partes[0]                                      
    
    # [PASO 6] Se extrae la edad. 
    # partes[1] es 'edad:25'. El .replace("edad:", "") borra ese texto y deja solo '25'.
    # Iteración 1: edad_texto = '25'
    # Iteración 2: edad_texto = '30'
    edad_texto = partes[1].replace("edad:", "")      
    
    # [PASO 7] Se convierte el texto a número entero con int() para poder hacer cálculos luego.
    # Iteración 1: edad = 25 (entero)
    # Iteración 2: edad = 30 (entero)
    edad = int(edad_texto)                           
    
    # [PASO 8] Se extrae el teléfono.
    # partes[2] es 'tel:987654321'. El .replace("tel:", "") borra ese texto y deja solo '987654321'.
    # Nota: se deja como string (texto) porque los teléfonos no se usan para sumar/restar.
    # Iteración 1: telefono = '987654321'
    # Iteración 2: telefono = '912345678'
    telefono = partes[2].replace("tel:", "")         

    # [PASO 9] Se crea un diccionario con las 3 variables extraídas.
    # Iteración 1: diccionario_persona = {'nombre': 'Andrea Salas', 'edad': 25, 'telefono': '987654321'}
    # Iteración 2: diccionario_persona = {'nombre': 'Tommy Solis', 'edad': 30, 'telefono': '912345678'}
    diccionario_persona = {                          
        "nombre": nombre,                            
        "edad": edad,
        "telefono": telefono
    }
    
    # [PASO 10] Se agrega el diccionario a la lista 'lista_persona'.
    # Al final del bucle, 'lista_persona' tendrá 2 diccionarios dentro.
    lista_persona.append(diccionario_persona)       

# [PASO 11] Se imprime la lista completa de diccionarios.
print("--- LISTA DE DICCIONARIO ---")
# >>> IMPRIME: [{'nombre': 'Andrea Salas', 'edad': 25, 'telefono': '987654321'}, {'nombre': 'Tommy Solis', 'edad': 30, 'telefono': '912345678'}]
print(lista_persona)
print("-" * 50) # Imprime 50 guiones como separador visual

# [PASO 12] Se imprime un encabezado para el reporte final.
print("--- REPORTE (Desarmando la lista) ---")

# [PASO 13] Bucle final: recorre 'lista_persona' para mostrar los datos de forma legible.
# Iteración 1: persona = {'nombre': 'Andrea Salas', 'edad': 25, ...} -> Imprime "Nombre: Andrea Salas | Edad: 25 años | Teléfono: 987654321"
# Iteración 2: persona = {'nombre': 'Tommy Solis', 'edad': 30, ...} -> Imprime "Nombre: Tommy Solis | Edad: 30 años | Teléfono: 912345678"
for persona in lista_persona:
    print("Nombre:", persona["nombre"], "| Edad:", persona["edad"], "años | Teléfono:", persona["telefono"])