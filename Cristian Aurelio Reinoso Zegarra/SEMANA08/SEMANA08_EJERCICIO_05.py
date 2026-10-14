# [PASO 1] Se crea la lista 'inventario' con 3 diccionarios (productos).
inventario = [
    {"nombre": "Camiseta de Futbol", "categoria": "Ropa", "precio": 25.0},
    {"nombre": "Zapatillas", "categoria": "Calzado", "precio": 85.0},
    {"nombre": "Pantalón de Futbol", "categoria": "Ropa", "precio": 10.0}
]

# [PASO 2] Se define la función 'buscar_productos'. 
# Python guarda estas instrucciones en memoria, pero NO las ejecuta todavía.
def buscar_productos(lista, palabra):
    # [PASO 3] 'palabra' llega como "FuTBol". .lower() la convierte a "futbol".
    termino_limpio = palabra.lower()                    
    

    # [PASO 4] Se crea una lista vacía para guardar los productos que coincidan.
    productos_encontrados = []                          
    
    # [PASO 5] Primer bucle: Recorre el inventario buscando la palabra "futbol".
    # Iteración 1: producto = Camiseta. "futbol" está en "camiseta de futbol"? SÍ. Se agrega.
    # Iteración 2: producto = Zapatillas. "futbol" está en "zapatillas"? NO. Se ignora.
    # Iteración 3: producto = Pantalón. "futbol" está en "pantalón de futbol"? SÍ. Se agrega.
    # Estado de 'productos_encontrados' al final del bucle: [Camiseta, Pantalón]
    for producto in lista:                              
        if termino_limpio in producto["nombre"].lower():      
            productos_encontrados.append(producto)            

    # [PASO 6] Se crea una lista vacía para guardar solo los precios.
    precios = []
    
    # [PASO 7] Segundo bucle: Recorre los productos encontrados (Camiseta y Pantalón).
    # Iteración 1: prod = Camiseta -> precios.append(25.0)
    # Iteración 2: prod = Pantalón -> precios.append(10.0)
    # Estado de 'precios' al final del bucle: [25.0, 10.0]
    for prod in productos_encontrados:      
        precios.append(prod["precio"])      

    # [PASO 8] .sort() ordena la lista de precios de menor a mayor.
    # Estado de 'precios' ahora: [10.0, 25.0]
    precios.sort()                           
    
    # [PASO 9] Se crea una lista vacía para los productos finales ordenados.
    lista_ordenada = []                      
    
    # [PASO 10] Tercer y Cuarto bucle (Bucles anidados). 
    # El primer bucle recorre los precios ordenados, el segundo busca qué producto tiene ese precio.
    
    # Iteración Externa 1: precio_buscado = 10.0
    #   Iteración Interna 1: prod = Camiseta (25.0). 25.0 == 10.0? NO.
    #   Iteración Interna 2: prod = Pantalón (10.0). 10.0 == 10.0? SÍ. Se agrega Pantalón a lista_ordenada.
    # Iteración Externa 2: precio_buscado = 25.0
    #   Iteración Interna 1: prod = Camiseta (25.0). 25.0 == 25.0? SÍ. Se agrega Camiseta a lista_ordenada.
    #   Iteración Interna 2: prod = Pantalón (10.0). 10.0 == 25.0? NO.
    # Estado de 'lista_ordenada' al final: [Pantalón, Camiseta]
    for precio_buscado in precios:          
        for prod in productos_encontrados:
            if prod["precio"] == precio_buscado:        
                lista_ordenada.append(prod)             
                
    # [PASO 11] La función devuelve la lista ordenada al código principal.
    return lista_ordenada                   


# [PASO 12] Ejecución principal. Se define la palabra a buscar.
palabra_buscar = "FuTBol"

# [PASO 13] Se llama a la función. El resultado que devuelve se guarda en 'busqueda'.
# 'busqueda' ahora contiene: [{'nombre': 'Pantalón de Futbol', 'precio': 10.0}, {'nombre': 'Camiseta de Futbol', 'precio': 25.0}]
busqueda = buscar_productos(inventario, palabra_buscar)

# [PASO 14] Se imprime el encabezado.
print(f"--- RESULTADOS DE BÚSQUEDA PARA: '{palabra_buscar}' ---")

# [PASO 15] Bucle final: Recorre 'busqueda' e imprime cada producto en orden de precio.
# Iteración 1: Imprime Pantalón de Futbol | Precio: 10.0
# Iteración 2: Imprime Camiseta de Futbol | Precio: 25.0
for prod in busqueda:
    print("Producto:", prod["nombre"], "| Precio:", prod["precio"])