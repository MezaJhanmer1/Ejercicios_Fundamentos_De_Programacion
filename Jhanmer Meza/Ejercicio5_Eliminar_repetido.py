# ==========================================================
# FUNCIÓN PARA ELIMINAR UNA REPETICIÓN DE UNA FRUTA
# ==========================================================

def eliminar_repeticion(lista, eliminar_fruta, cual_eliminar):

    # Creamos una lista vacía.
    # Aquí vamos a guardar las frutas que queremos conservar.
    lista_limpia = []

    # Creamos un contador para saber
    # cuántas veces aparece la fruta que buscamos.
    contador_apariciones = 0

    # Recorremos una por una todas las frutas de la lista.
    for fruta in lista:

        # Comprobamos si la fruta actual
        # es igual a la fruta que queremos eliminar.
        if fruta == eliminar_fruta:

            # Si encontramos la fruta,
            # aumentamos el contador en 1.
            contador_apariciones += 1

            # Comprobamos si esta es la aparición
            # que queremos eliminar.
            if contador_apariciones == cual_eliminar:

                # Mostramos un mensaje indicando
                # qué aparición estamos eliminando.
                print(f"Eliminando la aparición #{cual_eliminar} "
                      f"de {eliminar_fruta}")

                # "continue" hace que no guardemos
                # esta fruta en la lista nueva.
                # Luego pasa directamente a la siguiente fruta.
                continue

        # Si la fruta no fue eliminada,
        # la agregamos a la lista limpia.
        lista_limpia.append(fruta)

    # Al terminar el recorrido,
    # devolvemos la lista sin el duplicado.
    return lista_limpia


# ==========================================================
# LISTA ORIGINAL DE FRUTAS
# ==========================================================

# Creamos una lista de frutas.
# La manzana aparece dos veces.
frutas = [
    "plátano",
    "manzana",
    "naranja",
    "pera",
    "manzana",
    "uva"
]


# ==========================================================
# FRUTA QUE QUEREMOS BUSCAR
# ==========================================================

# Guardamos el nombre de la fruta que está repetida.
fruta_repetida = "manzana"


# ==========================================================
# LLAMAMOS A LA FUNCIÓN
# ==========================================================

# Enviamos tres datos a la función:
#
# 1. frutas → la lista donde vamos a buscar.
# 2. fruta_repetida → la fruta que queremos buscar.
# 3. cual_eliminar=2 → queremos eliminar la segunda
#    aparición de la manzana.
resultado = eliminar_repeticion(
    frutas,
    fruta_repetida,
    cual_eliminar=2
)


# ==========================================================
# MOSTRAMOS LOS RESULTADOS
# ==========================================================

# Mostramos la lista original.
print("\nLista original:")
print(frutas)

# Mostramos la lista después de eliminar
# la segunda manzana.
print("\nLista final:")
print(resultado)










