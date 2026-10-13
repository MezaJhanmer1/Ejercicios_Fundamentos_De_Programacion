# Ejercicio 01: Registro de productos con arreglos paralelos
# El programa muestra los productos, sus precios y sus cantidades.
# Al final, calcula el valor total de todo el inventario.

# Arreglo con los nombres de los productos.
nombres = ["Camiseta ", "Medias", "Polo", "Pantalones"]

# Arreglo con el precio de cada producto.
# La posición de cada precio corresponde al nombre en la misma posición.
precios = [100.0, 25.0, 45.0, 150.0]

# Arreglo con la cantidad disponible de cada producto.
# La posición de cada cantidad también corresponde al mismo producto.
cantidades = [5, 20, 15, 8]

# Inicializar el acumulador que guardará el valor total del inventario.
total_inventario = 0

# Mostrar el título del inventario.
print("--- INVENTARIO ---")

# Recorrer los cuatro productos usando sus índices: 0, 1, 2 y 3.
for i in range(4):

    # Obtener el nombre del producto ubicado en la posición actual.
    nombre = nombres[i]

    # Obtener el precio del producto ubicado en la misma posición.
    precio = precios[i]

    # Obtener la cantidad disponible del producto en esa posición.
    cantidad = cantidades[i]

    # Calcular el valor total de este producto: precio por cantidad.
    total_productos = precio * cantidad

    # Sumar el valor de este producto al total acumulado del inventario.
    total_inventario += total_productos

    # Mostrar el nombre, el precio con dos decimales y el stock disponible.
    print(f"Producto: {nombre} | Precio: S/.{precio:.2f} | Stock: {cantidad} unidades")

# Mostrar una línea para separar los productos del resultado final.
print("-----------------------------")

# Mostrar el valor total del inventario con dos decimales.
print(f"Precio Total del Inventario: S/.{total_inventario:.2f}")
