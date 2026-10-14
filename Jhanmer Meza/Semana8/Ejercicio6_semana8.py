# Ejercicio 6 – Combinación de Arreglos y Ordenamiento

# Arreglos paralelos: cada producto corresponde a sus ventas en la misma posición.
productos = ["Laptop", "Mouse", "Teclado", "Monitor"]
ventas = [45, 120, 85, 30]

lista_productos = []  # Lista vacía para guardar productos y ventas en diccionarios.

for i in range(4):  # Recorre los índices del 0 al 3.
    producto_dicc = {"nombre": productos[i], "ventas": ventas[i]}
    # Combina el nombre y las ventas de cada producto en un diccionario.
    lista_productos.append(producto_dicc)  # Agrega el diccionario a la lista.

lista_ventas_ordenadas = []  # Lista para guardar únicamente las ventas.

for prod in lista_productos:
    lista_ventas_ordenadas.append(prod["ventas"])
    # Extrae las ventas de cada producto y las agrega a la lista.

lista_ventas_ordenadas.sort()  # Ordena las ventas de menor a mayor.
lista_ventas_ordenadas.reverse()  # Invierte el orden para obtener de mayor a menor.

orden_productos = []  # Lista donde guardaremos los productos ordenados.

for venta_buscada in lista_ventas_ordenadas:
    for prod in lista_productos:  # Busca el producto que tiene esas ventas.
        if prod["ventas"] == venta_buscada and prod not in orden_productos:
            # Comprueba que las ventas coincidan y que el producto no esté repetido.
            orden_productos.append(prod)  # Agrega el producto a la lista ordenada.

suma_total_ventas = 0  # Acumulador que comienza en cero.

for prod in lista_productos:
    suma_total_ventas = suma_total_ventas + prod["ventas"]
    # Suma las ventas de todos los productos.

promedio_ventas = suma_total_ventas / 4  # Calcula el promedio de ventas.

productos_sobre_media = []  # Lista para guardar productos que superan el promedio.

for prod in lista_productos:
    if prod["ventas"] > promedio_ventas:
        # Comprueba si las ventas superan el promedio.
        productos_sobre_media.append(prod["nombre"])  # Guarda el nombre del producto.

# Mostrar el ranking de productos según sus ventas.
print("1 y 2) ORDEN DE VENTAS (De mayor a menor):")
posicion = 1  # El ranking comienza en el primer lugar.

for prod in orden_productos:
    print(posicion, "° Lugar - Producto:", prod["nombre"], "| Ventas:", prod["ventas"])
    posicion = posicion + 1  # Avanza a la siguiente posición del ranking.

print("-" * 45)

# Mostrar el promedio y los productos que lo superan.
print("3) REPORTE DE MEDIA Y PROMEDIO:")
print("El promedio de ventas es:", promedio_ventas)
print("Productos que superan la media:", productos_sobre_media)