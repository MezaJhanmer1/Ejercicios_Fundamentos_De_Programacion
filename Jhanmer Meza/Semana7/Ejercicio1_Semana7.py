# Pedimos al usuario que ingrese sus nombres.
# Lo que escriba se guarda en la variable "nombre".
nombre = input("Por favor, ingresa tus nombres: ")

# Pedimos al usuario que ingrese sus apellidos.
# Lo que escriba se guarda en la variable "apellido".
apellido = input("Por favor, ingresa tus apellidos: ")


# Convertimos los nombres y apellidos a MAYÚSCULAS usando .upper()
# Luego unimos el nombre y el apellido con un espacio entre ellos.
nombre_mayusculas = nombre.upper() + " " + apellido.upper()


# Mostramos un saludo personalizado.
# La letra f permite colocar el contenido de una variable
# directamente dentro del texto usando {nombre_mayusculas}.
print(f"¡Hola, {nombre_mayusculas}! Bienvenido al curso.")