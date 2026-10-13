#Ejercicio 6 –Combinación de Arreglos y Ordenamiento

productos = ["Laptop", "Mouse", "Teclado", "Monitor"]       # Arreglos paralelos 
ventas = [45, 120, 85, 30]

lista_productos = []                                         #lista vacia para guardar los diccionarios
for i in range(4):                                           # para i en rango del 0 al 3
    producto_dicc = {"nombre": productos[i], "ventas": ventas[i]}   #producto_dicc toma productos y ventas
    lista_productos.append(producto_dicc)                           #agrega ambos datos y tenemos una lista ordenada

lista_ventas_ordenadas = []                                 #lista vacia para guardar la nueva lista ordenada
for prod in lista_productos:                                #para prod en lista_ productos [ laptop, 45] y asi recorre la nueva lista.
    lista_ventas_ordenadas.append(prod["ventas"])           #agrega solo los datos de ventas: [45, 120 ,85, 30]

lista_ventas_ordenadas.sort()                               #Ordena los números de menor a mayor
lista_ventas_ordenadas.reverse()                            # Queda de mayor a menor [120,85,45,30]

orden_productos = []
for venta_buscada in lista_ventas_ordenadas:
    for prod in lista_productos:                            #para prod en lista_productos, toma el num mas alto.
        
        if prod["ventas"] == venta_buscada and prod not in orden_productos:   #si el num alto es igual a venta_buscada y prod no esta en orden_productos
            orden_productos.append(prod)                    #agrega la nueva lista ordenada.. [producto] + [ventas]

suma_total_ventas = 0
for prod in lista_productos:                
    suma_total_ventas = suma_total_ventas + prod["ventas"]              #Desarma la lista de productos y va sumando todas las ventas 
promedio_ventas = suma_total_ventas / 4

productos_sobre_media = []                                  # Filtrar cuáles productos están sobre la media (sobre el promedio)
for prod in lista_productos:
    if prod["ventas"] > promedio_ventas:                    # Si las ventas del producto actual son mayores a 70
        productos_sobre_media.append(prod["nombre"])        # agrega el nombre


print("1 y 2) ORDEN DE VENTAS (De mayor a menor):")
posicion = 1                                                #variable para acumular q comienza en 1
for prod in orden_productos:
    print(posicion, "° Lugar - Producto:", prod["nombre"], "| Ventas:", prod["ventas"])
    posicion = posicion + 1                                 #variable q recorre la lista y pasa a 2 y 3 + el print

print("-" * 45)
print("3) REPORTE DE MEDIA Y PROMEDIO:")
print("El promedio de ventas es:", promedio_ventas)
print("Productos que superan la media:", productos_sobre_media)