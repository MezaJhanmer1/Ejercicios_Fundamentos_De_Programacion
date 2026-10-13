# Ejercicio 06: Combinación de arreglos y ordenamiento
# Ordena los productos por ventas y calcula el promedio.

# Listas paralelas de productos y ventas.
productos = ["Laptop", "Mouse", "Teclado", "Monitor"]
ventas = [45, 120, 85, 30]

# Crear una lista para combinar productos y ventas.
lista_productos = []
for i in range(4):
    # Guardar el nombre y las ventas en un diccionario.
    producto_dicc = {"nombre": productos[i], "ventas": ventas[i]}
    lista_productos.append(producto_dicc)  # Agregar el diccionario a la lista.

# Crear una lista con las ventas.
lista_ventas_ordenadas = []
for prod in lista_productos:
    lista_ventas_ordenadas.append(prod["ventas"])  # Agregar las ventas.

# Ordenar las ventas de mayor a menor.
lista_ventas_ordenadas.sort()
lista_ventas_ordenadas.reverse()

# Crear una lista para los productos ordenados.
orden_productos = []
for venta_buscada in lista_ventas_ordenadas:
    for prod in lista_productos:
        # Agregar el producto que coincide, sin repetirlo.
        if prod["ventas"] == venta_buscada and prod not in orden_productos:
            orden_productos.append(prod)

# Sumar las ventas de todos los productos.
suma_total_ventas = 0
for prod in lista_productos:
    suma_total_ventas = suma_total_ventas + prod["ventas"]

# Calcular el promedio de ventas.
promedio_ventas = suma_total_ventas / 4

# Buscar productos que superan el promedio.
productos_sobre_media = []
for prod in lista_productos:
    if prod["ventas"] > promedio_ventas:
        productos_sobre_media.append(prod["nombre"])  # Guardar el nombre.

# Mostrar los productos ordenados por ventas.
print("1 y 2) ORDEN DE VENTAS (De mayor a menor):")
posicion = 1
for prod in orden_productos:
    print(posicion, "° Lugar - Producto:", prod["nombre"], "| Ventas:", prod["ventas"])
    posicion = posicion + 1  # Avanzar a la siguiente posición.

# Mostrar el promedio y los productos que lo superan.
print("-" * 45)
print("3) REPORTE DE MEDIA Y PROMEDIO:")
print("El promedio de ventas es:", promedio_ventas)
print("Productos que superan la media:", productos_sobre_media)
