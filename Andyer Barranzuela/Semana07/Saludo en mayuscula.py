# Solicitar al usuario que ingrese sus nombres
nombre = input("Por favor, ingresa tus nombres: ")

# Solicitar al usuario que ingrese sus apellidos
apellido = input("Por favor, ingresa tus apellidos: ")

# Convertir los nombres y apellidos a mayúsculas
# Luego, unirlos dejando un espacio entre ambos
nombre_mayusculas = nombre.upper() + " " + apellido.upper()

# Mostrar un saludo personalizado utilizando el nombre completo
print(f"¡Hola, {nombre_mayusculas}! Bienvenido al curso.")