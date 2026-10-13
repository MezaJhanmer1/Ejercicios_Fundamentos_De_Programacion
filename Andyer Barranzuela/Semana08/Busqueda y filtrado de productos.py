# Ejercicio 05: Búsqueda y filtrado de productos
# El programa busca productos por nombre y los ordena por precio.

# Lista de productos con su nombre, categoría y precio.
inventario = [
    {"nombre": "Camiseta de Futbol", "categoria": "Ropa", "precio": 25.0},
    {"nombre": "Zapatillas", "categoria": "Calzado", "precio": 85.0},
    {"nombre": "Pantalón de Futbol", "categoria": "Ropa", "precio": 10.0}
]

# Buscar productos que contengan una palabra y ordenarlos por precio.
def buscar_productos(lista, palabra):
    # Convertir la palabra buscada a minúsculas.
    termino_limpio = palabra.lower()

    # Crear una lista vacía para los productos encontrados.
    productos_encontrados = []

    # Revisar cada producto de la lista.
    for producto in lista:
        # Comparar el nombre sin distinguir mayúsculas y minúsculas.
        if termino_limpio in producto["nombre"].lower():
            # Guardar el producto que coincide con la búsqueda.
            productos_encontrados.append(producto)

    # Crear una lista para guardar los precios encontrados.
    precios = []
    for prod in productos_encontrados:
        # Agregar el precio a la lista.
        precios.append(prod["precio"])

    # Ordenar los precios de menor a mayor.
    precios.sort()

    # Crear una lista vacía para los productos ordenados.
    lista_ordenada = []
    for precio_buscado in precios:
        # Buscar el producto que tenga el precio actual.
        for prod in productos_encontrados:
            if prod["precio"] == precio_buscado:
                # Agregar el producto a la lista ordenada.
                lista_ordenada.append(prod)

    # Devolver los productos ordenados por precio.
    return lista_ordenada

# Indicar la palabra que se desea buscar.
palabra_buscar = "FuTBol"

# Ejecutar la búsqueda en el inventario.
busqueda = buscar_productos(inventario, palabra_buscar)

# Mostrar el título de los resultados.
print(f"--- RESULTADOS DE BÚSQUEDA PARA: '{palabra_buscar}' ---")

# Mostrar el nombre y el precio de cada producto encontrado.
for prod in busqueda:
    print("Producto:", prod["nombre"], "| Precio:", prod["precio"])
