from statistics import mean

notas_originales = [85, 42, 93, 67, 28, 75]

def ordenamiento_burbuja(valores):
    lista = valores.copy()
    n = len(lista)
    for pasada in range(n - 1):
        hubo_cambio = False
        for i in range(n - 1 - pasada):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                hubo_cambio = True
        if not hubo_cambio:
            break
    return lista

def ordenamiento_seleccion(valores):
    lista = valores.copy()
    n = len(lista)
    for i in range(n - 1):
        pos_min = i
        for j in range(i + 1, n):
            if lista[j] < lista[pos_min]:
                pos_min = j
        if pos_min != i:
            lista[i], lista[pos_min] = lista[pos_min], lista[i]
    return lista

def resumen_estadistico(valores):
    return {
        "minima": min(valores),
        "maxima": max(valores),
        "promedio": mean(valores)
    }

def main():
    print("Calificaciones originales:", notas_originales)

    orden_burbuja = ordenamiento_burbuja(notas_originales)
    print("Bubble Sort:", orden_burbuja)

    orden_seleccion = ordenamiento_seleccion(notas_originales)
    print("Selection Sort:", orden_seleccion)

    stats = resumen_estadistico(notas_originales)
    print("\nResumen:")
    print(f"  Mínima: {stats['minima']}")
    print(f"  Máxima: {stats['maxima']}")
    print(f"  Promedio: {stats['promedio']:.2f}")

if __name__ == "__main__":
    main()