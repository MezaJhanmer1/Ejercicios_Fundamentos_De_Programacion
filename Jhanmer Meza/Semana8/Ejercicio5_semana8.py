# Ejercicio 5 – Búsqueda y Filtrado de Productos

# Lista de productos con su nombre, categoría y precio
inventario = [
    {"nombre": "Camiseta de Futbol", "categoria": "Ropa", "precio": 25.0},
    {"nombre": "Zapatillas", "categoria": "Calzado", "precio": 85.0},
    {"nombre": "Pantalón de Futbol", "categoria": "Ropa", "precio": 10.0}
]

# Función que busca productos por una palabra y los ordena por precio
def buscar_productos(lista, palabra):
    termino_limpio = palabra.lower()
    # Convierte la palabra buscada a minúsculas para ignorar mayúsculas.

    productos_encontrados = []  # Lista vacía para guardar los productos encontrados.

    for producto in lista:  # Recorre todos los productos del inventario.
        if termino_limpio in producto["nombre"].lower():
            # Comprueba si la palabra aparece en el nombre del producto.
            productos_encontrados.append(producto)
            # Agrega el producto si coincide con la búsqueda.

    precios = []
    for prod in productos_encontrados:
        precios.append(prod["precio"])
        # Guarda los precios de los productos encontrados.

    precios.sort()
    # Ordena los precios de menor a mayor.

    lista_ordenada = []  # Lista vacía para guardar los productos ordenados.

    for precio_buscado in precios:
        for prod in productos_encontrados:
            if prod["precio"] == precio_buscado:
                # Busca el producto que tiene el precio actual.
                lista_ordenada.append(prod)
                # Agrega el producto a la lista ordenada.

    return lista_ordenada
    # Devuelve los productos encontrados y ordenados por precio.

# Palabra que queremos buscar en los nombres de los productos
palabra_buscar = "FuTBol"

# Llamamos a la función y guardamos el resultado
busqueda = buscar_productos(inventario, palabra_buscar)

# Mostrar los productos encontrados y sus precios
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