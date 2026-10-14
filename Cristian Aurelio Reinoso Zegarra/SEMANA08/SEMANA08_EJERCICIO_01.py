#Mostrar el título del programa
print("Registro de Productos")


#Declarar las listas con los datos de los productos
#   - nombres:    nombre de cada producto
#   - precios:    precio unitario en soles
#   - cantidades: stock disponible
# Las tres listas están alineadas por posición (índice 0, 1, 2, 3)
nombres    = ["Laptop", "Mouse", "Teclado", "Monitor"]
precios    = [2500.00, 45.50, 120.00, 800.00]
cantidades = [5, 40, 15, 8]


#Inicializar el acumulador del total del inventario
# Se empieza en 0 y se irá sumando el subtotal de cada producto
total_inventario = 0


#Recorrer los productos con un for + range
#   - range(4) genera los índices 0, 1, 2, 3 (uno por producto)
for i in range(4):

    # Mostrar los datos del producto en formato de tabla
    #   - {nombres[i]:<10}  -> alinea el nombre a la izquierda (10 espacios)
    #   - {precios[i]:>8.2f} -> alinea el precio a la derecha, 2 decimales
    #   - {cantidades[i]:>3} -> alinea el stock a la derecha (3 espacios)
    print(f"{nombres[i]:<10} | Precio: S/ {precios[i]:>8.2f} | Stock: {cantidades[i]:>3}")

    # Calcular el subtotal (precio * cantidad)
    # y acumularlo en total_inventario
    total_inventario += precios[i] * cantidades[i]


 
#Mostrar el resultado final del inventario
#   - \n agrega una línea en blanco antes del mensaje
#   - :.2f muestra el total con 2 decimales
print(f"\nPrecio total del inventario: S/ {total_inventario:.2f}")


#Registro de Productos
#Laptop     | Precio: S/  2500.00 | Stock:   5
#Mouse      | Precio: S/    45.50 | Stock:  40
#Teclado    | Precio: S/   120.00 | Stock:  15
#Monitor    | Precio: S/   800.00 | Stock:   8

#Precio total del inventario: S/ 22520.00