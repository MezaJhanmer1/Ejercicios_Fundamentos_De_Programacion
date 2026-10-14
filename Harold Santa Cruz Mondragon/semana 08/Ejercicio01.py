# Ejercicio 01 - Inventario usando arreglos paralelos

nombres = ["Camiseta ", "Medias", "Polo", "Pantalones"]     # Arreglo 1: nombres de productos
precios = [100.0, 25.0, 45.0, 150.0]                         # Arreglo 2: precios unitarios
cantidades = [5, 20, 15, 8]                                  # Arreglo 3: cantidades en stock

total_inventario = 0                 # Acumulador del valor total del inventario

print("--- INVENTARIO ---")

for i in range(4):                  # Iterar por cada posición de los arreglos
    
    nombre = nombres[i]             # Extraer el nombre del producto actual
    precio = precios[i]             # Extraer el precio del producto actual
    cantidad = cantidades[i]        # Extraer la cantidad del producto actual
    
    total_productos = precio * cantidad      # Calcular el valor de este producto en stock
    total_inventario += total_productos      # Acumular ese valor al total general
    
    print(f"Producto: {nombre} | Precio: S/.{precio:.2f} | Stock: {cantidad} unidades")

print("-----------------------------")
print(f"Precio Total del Inventario: S/.{total_inventario:.2f}")