
# Inicializamos una estructura de datos tipo lista.
# Servirá para almacenar la secuencia de enlaces web.
pila = []


# ==========================================
# FUNCIÓN PARA VISITAR UNA PÁGINA
# ==========================================

# Añadimos una función para visitar y registrar una nueva URL en el historial.
def visitar(url):

    # Insertamos el nuevo sitio al final del arreglo.
    # Añadimos la URL ingresada al final de la pila.
    pila.append(url)

    # Imprimimos la URL recién agregada.
    print("Visitando:", url)

    # Imprimimos el estado actualizado del contenedor (variable pila).
    print("Historial:", pila)


# ==========================================
# FUNCIÓN PARA RETROCEDER
# ==========================================

# Función para regresar a la página web anterior en el historial.
def retroceder():

    # # Comprobamos que existan más de dos páginas en el historial.
    if len(pila) > 1:

        # pop() remueve el elemento superior y devuelve su valor.
        # Corresponde a la operación POP.
        pagina = pila.pop()

        # Notificamos desde qué dirección se está saliendo.
        print("Retrocediendo desde:", pagina)

        # Desplegamos la página que queda activa en el historial.
        print("Regresó a:", pila[-1])

        # Mostramos cómo queda el historial.
        print("Historial:", pila)

    else:

        # Si queda un solo elemento o ninguno, se impide la extracción.
        print("No hay una página anterior.")


# ==========================================
# FUNCIÓN PARA MOSTRAR LA PÁGINA ACTUAL
# ==========================================

# Muestra la página actual en la que se encuentra el usuario.
def pagina_actual():

    # Validamos que el historial contenga al menos un registro.
    if len(pila) > 0:

        # El índice [-1] accede al ultimo elemento de la lista.
        # Realiza la consulta sin modificar la lista.
        print("Página actual:", pila[-1])

    else:

        print("No hay ninguna página abierta.")


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

while True:

    # Desplegamos el menú principal con los comandos de la aplicación.
    print("\n===== HISTORIAL DEL NAVEGADOR =====")
    print("1. Visitar página")
    print("2. Retroceder")
    print("3. Ver página actual")
    print("4. Salir")

    # Solicitamos la selección del menú mediante consola.
    opcion = input("Ingrese una opción: ")


    # --------------------------------------
    # OPCIÓN 1: VISITAR
    # --------------------------------------

    if opcion == "1":

        # Capturamos la URL o el dominio que
        # el usuario desea registrar.
        url = input("Ingrese la página que desea visitar: ")

        # Invocamos la rutina visitar().
        visitar(url)


    # --------------------------------------
    # OPCIÓN 2: RETROCEDER
    # --------------------------------------

    elif opcion == "2":

        # Ejecutamos la rutina retroceder().
        retroceder()


    # --------------------------------------
    # OPCIÓN 3: PÁGINA ACTUAL
    # --------------------------------------

    elif opcion == "3":

        # Invocamos la rutina pagina_actual().
        pagina_actual()


    # --------------------------------------
    # OPCIÓN 4: SALIR
    # --------------------------------------

    elif opcion == "4":

        print("Programa terminado.")

        # Interrumpimos la ejecución continua del bucle.
        break


    # --------------------------------------
    # OPCIÓN INCORRECTA
    # --------------------------------------

    else:

        print("Opción incorrecta. Intente nuevamente.")