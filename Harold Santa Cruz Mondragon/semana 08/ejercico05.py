# Ejercicio 05 – Búsqueda y filtrado de productos

inventario = [
    {"nombre": "Camiseta de Futbol", "categoria": "Ropa", "precio": 25.0},
    {"nombre": "Zapatillas", "categoria": "Calzado", "precio": 85.0},
    {"nombre": "Pantalón de Futbol", "categoria": "Ropa", "precio": 10.0}
]

def buscar_productos(lista, palabra):
    termino_limpio = palabra.lower()                    # Normaliza la palabra buscada a minúsculas
    
    # Paso 1: Filtrar los productos cuyo nombre contenga la palabra buscada
    productos_encontrados = []
    for producto in lista:
        if termino_limpio in producto["nombre"].lower():    # Compara ignorando mayúsculas/minúsculas
            productos_encontrados.append(producto)          # Guarda el diccionario completo si coincide

    # Paso 2: Extraer solo los precios de los productos encontrados
    precios = []
    for prod in productos_encontrados:
        precios.append(prod["precio"])      # Se obtiene una lista simple de números: [25.0, 10.0]

    # Paso 3: Ordenar los precios de menor a mayor
    precios.sort()                          # Queda como [10.0, 25.0]

    # Paso 4: Reconstruir la lista de productos en el orden de los precios ordenados
    lista_ordenada = []
    for precio_buscado in precios:          # Recorre los precios ya ordenados
        for prod in productos_encontrados:
            if prod["precio"] == precio_buscado:        # Busca el producto que coincide con ese precio
                lista_ordenada.append(prod)             # Lo agrega en el orden correcto

    return lista_ordenada                   # Devuelve la lista final ordenada por precio

palabra_buscar = "FuTBol"
busqueda = buscar_productos(inventario, palabra_buscar)

print(f"--- RESULTADOS DE BÚSQUEDA PARA: '{palabra_buscar}' ---")
for prod in busqueda:
    print("Producto:", prod["nombre"], "| Precio:", prod["precio"])