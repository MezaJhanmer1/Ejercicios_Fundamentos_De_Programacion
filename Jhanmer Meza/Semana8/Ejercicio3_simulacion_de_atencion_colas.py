# Ejercicio 01 - Registro de Productos con Arreglos Paralelos

# Lista con los nombres de los productos
nombres = ["Camiseta ", "Medias", "Polo", "Pantalones"]

# Lista con los precios de cada producto
precios = [100.0, 25.0, 45.0, 150.0]

# Lista con las cantidades disponibles de cada producto
cantidades = [5, 20, 15, 8]

# Variable que acumula el valor total de todos los productos
total_inventario = 0

# Mostrar el título del inventario
print("--- INVENTARIO ---")

# Recorrer los 4 productos usando sus índices (del 0 al 3)
for i in range(4):

    # Obtener los datos segun la posicion del indice
    nombre = nombres[i]

    precio = precios[i]

    cantidad = cantidades[i]

    # Calcular el valor total de este producto:
   
    total_productos = precio * cantidad

    # Sumar el valor del producto al total del inventario
    
    total_inventario += total_productos

    # Mostrar el nombre, el precio y el stock del producto
    # :.2f muestra el precio con dos decimales
    print(f"Producto: {nombre} | Precio: S/.{precio:.2f} | Stock: {cantidad} unidades")

print("-----------------------------")

print(f"Precio Total del Inventario: S/.{total_inventario:.2f}")