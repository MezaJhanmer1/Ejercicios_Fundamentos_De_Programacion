# ==========================================
# HISTORIAL DE NAVEGADOR - PILA (STACK)
# LIFO: Last In, First Out
# ==========================================

# Creamos una lista vacía.
# Esta lista será nuestra pila de páginas.
pila = []


# ==========================================
# FUNCIÓN PARA VISITAR UNA PÁGINA
# ==========================================

def visitar(url):

    # Agregamos la página al final de la pila.
    # append() funciona como PUSH.
    pila.append(url)

    # Mostramos la página que acabamos de visitar.
    print("Visitando:", url)

    # Mostramos cómo quedó la pila.
    print("Historial:", pila)


# ==========================================
# FUNCIÓN PARA RETROCEDER
# ==========================================

def retroceder():

    # Verificamos que exista una página anterior.
    if len(pila) > 1:

        # pop() elimina la última página visitada y la muestra.
        # Esta operación representa POP.
        pagina = pila.pop()

        # Mostramos qué página estamos dejando.
        print("Retrocediendo desde:", pagina)

        # [-1] obtiene el último elemento de la pila.
        # Ahora esa será nuestra página actual.
        print("Regresó a:", pila[-1])

        # Mostramos el historial después de retroceder.
        print("Historial:", pila)

    else:

        # Si solamente hay una página, no podemos retroceder.
        print("No hay una página anterior.")


# ==========================================
# FUNCIÓN PARA MOSTRAR LA PÁGINA ACTUAL
# ==========================================

def pagina_actual():

    # Verificamos que exista alguna página.
    if len(pila) > 0:

        # [-1] obtiene el último elemento.
        # No lo elimina, solamente lo consulta.
        print("Página actual:", pila[-1])

    else:

        print("No hay ninguna página abierta.")


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

while True:

    # Mostramos las opciones disponibles.
    print("\n===== HISTORIAL DEL NAVEGADOR =====")
    print("1. Visitar página")
    print("2. Retroceder")
    print("3. Ver página actual")
    print("4. Salir")

    # Pedimos al usuario que seleccione una opción.
    opcion = input("Ingrese una opción: ")


    # --------------------------------------
    # OPCIÓN 1: VISITAR
    # --------------------------------------

    if opcion == "1":

        # Pedimos al usuario el nombre o dirección
        # de la página que quiere visitar.
        url = input("Ingrese la página que desea visitar: ")

        # Llamamos a la función visitar().
        visitar(url)


    # --------------------------------------
    # OPCIÓN 2: RETROCEDER
    # --------------------------------------

    elif opcion == "2":

        # Llamamos a la función retroceder().
        retroceder()


    # --------------------------------------
    # OPCIÓN 3: PÁGINA ACTUAL
    # --------------------------------------

    elif opcion == "3":

        # Llamamos a la función pagina_actual().
        pagina_actual()


    # --------------------------------------
    # OPCIÓN 4: SALIR
    # --------------------------------------

    elif opcion == "4":

        print("Programa terminado.")

        # break termina el ciclo while.
        break


    # --------------------------------------
    # OPCIÓN INCORRECTA
    # --------------------------------------

    else:

        print("Opción incorrecta. Intente nuevamente.")