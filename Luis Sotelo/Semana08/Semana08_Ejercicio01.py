    #Ejercicio 01 - Registro de Productos con Arreglos Paralelos


nombres = ["Camiseta ", "Medias", "Polo", "Pantalones"]     # Tres arreglos paralelos
precios = [100.0, 25.0, 45.0, 150.0]
cantidades = [5, 20, 15, 8]

total_inventario = 0                 # Variable para acumular el valor total de inventario

print("--- INVENTARIO ---")

for i in range(4):                  # Recorrer los 4 elementos desde el índice de 0 a 3
    
    nombre = nombres[i]             # Obtener los datos del elemento en la posición actual, si i=0 es (Camiseta, 100 y 5)
    precio = precios[i]
    cantidad = cantidades[i]
    
    total_productos = precio * cantidad      # pide precio total del inventario
    total_inventario += total_productos      # Sumar total productos al total del inventario, sumale a lo q ya habia var1+var2+var3..
    
    print(f"Producto: {nombre} | Precio: S/.{precio:.2f} | Stock: {cantidad} unidades")

print("-----------------------------")
print(f"Precio Total del Inventario: S/.{total_inventario:.2f}")