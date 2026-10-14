# [PASO 1] Se crean las dos listas originales.
productos = ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Impresora']
ventas = [150, 300, 200, 80, 120]

 
# [PASO 2] Se crea la lista vacía.
lista = []

# [PASO 3] range(len(productos)) es range(5), así que 'i' tomará los valores: 0, 1, 2, 3, 4.
for i in range(len(productos)):
    lista.append({'producto': productos[i], 'ventas': ventas[i]})

# Estado de 'lista': [Laptop(150), Mouse(300), Teclado(200), Monitor(80), Impresora(120)]


# ================= ORDENAMIENTO MANUAL (BURBUJA) =================
# [PASO 4] Se crea una copia para no modificar 'lista' (la necesitamos sin ordenar al final).
lista_ordenada = lista.copy() 

# [PASO 5] Bucle EXTERNO: controla cuántas pasadas le damos a la lista.
# range(5) -> i toma los valores 0, 1, 2, 3, 4.
for i in range(len(lista_ordenada)):
    
    # [PASO 6] Bucle INTERNO: compara pares de vecinos.
    # len(lista_ordenada) - 1 - i: en la primera pasada compara 4 veces, luego 3, luego 2...
    for j in range(len(lista_ordenada) - 1 - i):
        
        # [PASO 7] Comparación: ¿Las ventas del actual son MENORES que las del siguiente?
        # (Usamos < para ordenar de MAYOR a MENOR).
        if lista_ordenada[j]['ventas'] < lista_ordenada[j+1]['ventas']:
            
            # [PASO 8] Intercambio (Swap) usando una variable temporal.
            # Ejemplo en la primera pasada (j=1): Mouse(300) vs Teclado(200). 300 < 200 es Falso, no hace nada.
            # Ejemplo en la primera pasada (j=3): Monitor(80) vs Impresora(120). 80 < 120 es Verdadero.
            # temporal = Monitor(80) -> lista_ordenada[3] = Impresora(120) -> lista_ordenada[4] = Monitor(80)
            temporal = lista_ordenada[j]
            lista_ordenada[j] = lista_ordenada[j+1]
            lista_ordenada[j+1] = temporal

# Al terminar todos los bucles, 'lista_ordenada' queda: [Mouse(300), Teclado(200), Laptop(150), Impresora(120), Monitor(80)]


# ================= IMPRIMIR RANKING =================
# [PASO 9] Se imprime el encabezado.
print("RANKING DE VENTAS")

# [PASO 10] enumerate(lista_ordenada, start=1) da el índice (i) y el elemento (item).
# Iteración 1: i=1, item=Mouse -> Imprime "1° Mouse: 300 ventas"
# Iteración 2: i=2, item=Teclado -> Imprime "2° Teclado: 200 ventas"
# ... y así hasta el 5°.
for i, item in enumerate(lista_ordenada, start=1):
    print(f"{i}° {item['producto']}: {item['ventas']} ventas")


# ================= PROMEDIO Y SOBRE LA MEDIA =================
# [PASO 11] Se inicializa el acumulador en 0.
total_ventas = 0

# [PASO 12] Se recorre 'lista' (la original, sin ordenar) para sumar las ventas.
for item in lista:
    total_ventas += item['ventas']

# [PASO 13] Se calcula el promedio. 850 / 5 = 170.0
promedio = total_ventas / len(lista)

# [PASO 14] Se imprime el promedio con 2 decimales. 
print(f"\nPromedio de ventas: {promedio:.2f}")

print("Productos sobre la media:")

# [PASO 15] Se recorre 'lista' de nuevo para ver quiénes superan el promedio (170.0).
for item in lista:
    if item['ventas'] > promedio:
        print(f" - {item['producto']} ({item['ventas']})")