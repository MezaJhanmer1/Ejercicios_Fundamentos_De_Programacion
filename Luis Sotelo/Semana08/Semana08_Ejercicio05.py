    #Ejercicio 5 – Búsqueda y Filtrado de Productos

inventario = [
    {"nombre": "Camiseta de Futbol", "categoria": "Ropa", "precio": 25.0},
    {"nombre": "Zapatillas", "categoria": "Calzado", "precio": 85.0},
    {"nombre": "Pantalón de Futbol", "categoria": "Ropa", "precio": 10.0}
]

def buscar_productos(lista, palabra):
    termino_limpio = palabra.lower()                    # Pasar la palabra de búsqueda a minúsculas
    
    productos_encontrados = []                          # Crear una lista vacia
    for producto in lista:                              # para producto en lista
        if termino_limpio in producto["nombre"].lower():      # Convertir el nombre del producto actual a minúsculas para comparar
            productos_encontrados.append(producto)            # Si la palabra buscada estaba dentro del nombre del producto se agrega a la lista

    precios = []
    for prod in productos_encontrados:      #Recorre los productos que encontramos antes, extrae sus precios uno a uno 
        precios.append(prod["precio"])      #si es verdadero agrega a la lista esos precios [25, 10]

    precios.sort()                           # Ordenamos esa lista de números de menor a mayor [10, 25]
    lista_ordenada = []                      # lista vacia para agregar los productos finales ya ordenados
    for precio_buscado in precios:          
        for prod in productos_encontrados:
            if prod["precio"] == precio_buscado:        #Si encuentra el producto que = precio ordenado actual, lo añade a lista_ordenada
                lista_ordenada.append(prod)             #si es verdadero agrega a la lista ya ordenada
                
    return lista_ordenada                   #retorna la lista ya ordenada

palabra_buscar = "FuTBol"
busqueda = buscar_productos(inventario, palabra_buscar)

print(f"--- RESULTADOS DE BÚSQUEDA PARA: '{palabra_buscar}' ---")
for prod in busqueda:
    print("Producto:", prod["nombre"], "| Precio:", prod["precio"])




#Qué hace aquí el for: Desarma la lista completa del inventario (los 3 productos).
#Paquete por paquete, Toma el primer diccionario (Camiseta), revisa su "nombre". Como tiene la palabra que buscamos,
#mete ese paquete entero en una caja nueva llamada productos_encontrados. Luego pasa al segundo producto (Zapatillas),
#lo desarma, ve que no coincide y lo deja pasar.

#Qué hace aquí el for: Ahora va a la caja donde están solo los 2 productos que encontramos y la vuelve a desarmar.
#Paquete por paquete, Abre el paquete de la Camiseta, mete la mano, saca solo el número de su "precio" (25.0) y lo guarda en una
#lista simple de números. Luego abre el siguiente paquete 
#Resultado: Nos deja una lista de números independientes: [25.0, 10.0], la cual ordenamos fácilmente con .sort() para 
#que quede como [10.0, 25.0].

#El primer for toma el primer precio ya ordenado (el 10.0).
#El segundo for vuelve a desarmar la lista de productos encontrados para buscar quién tiene ese precio. Encuentra las Medias (que valen 10.0) y mete ese paquete primero en la lista_ordenada.
#Luego, el primer for pasa al siguiente precio (25.0). El segundo for busca y encuentra la Camiseta, metiendo su paquete después.
#Resultado: Los paquetes de los diccionarios quedan perfectamente guardados en orden de menor a mayor.