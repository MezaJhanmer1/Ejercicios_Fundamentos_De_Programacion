
# ESTRUCTURA DE DATOS: PILA (STACK - LIFO)

# Se crea una lista vacía para simular la pila del navegador.
# En una pila (LIFO - Last In, First Out), el último elemento en entrar es el
# primero en salir.
pila_navegador = []



# FUNCIONES DEL NAVEGADOR


# a) Función para visitar una página (Operación PUSH)
def visitar(url):
    # .append() agrega la nueva URL al final de la pila.
    # Esto simula entrar a una página nueva.
    pila_navegador.append(url)
    
    # Mostramos un mensaje indicando qué página se visitó.
    print("Visitaste:", url)
    
    # Mostramos cómo queda el historial completo después de visitar.
    print("Historial actual:", pila_navegador)


# b) Función para retroceder una página (Operación POP)
def retroceder():
    # Estructura condicional: verifica si la pila contiene al menos un elemento.
    if len(pila_navegador) > 0:
        # .pop() elimina y retorna el ÚLTIMO elemento de la lista (cima de la pila).
        pagina_cerrada = pila_navegador.pop()
        
        # Evalúa si aún quedan páginas en la pila tras eliminar la última.
        if len(pila_navegador) > 0:
            # pila_navegador[-1] accede al nuevo último elemento sin eliminarlo.
            print("Retrocediste desde", pagina_cerrada, "ahora estás en:", pila_navegador[-1])
        else:
            # Notifica que la pila quedó totalmente vacía tras hacer el pop().
            print("Retrocediste desde", pagina_cerrada, "pero ya no hay páginas atrás.")
    else:
        # Manejo de error/excepción: si la lista ya estaba vacía desde el inicio.
        print("No hay paginas para retroceder.")


# c) Función para ver la página actual (Operación PEEK)
def pagina_actual():
    # Verifica si existen elementos dentro de la pila.
    if len(pila_navegador) > 0:
        # Muestra la cima de la pila mediante el índice negativo [-1].
        print("Pagina actual:", pila_navegador[-1])
    else:
        # Caso en que no haya elementos registrados en la lista.
        print("No hay ninguna pagina abierta.")




# BUCLE PRINCIPAL 

# Bucle infinito que mantiene el programa activo hasta que el usuario decida salir.
while True:
    # Despliegue del menú de opciones en pantalla.
    print("\n---- MENÚ ----")
    print("1. Visitar una pagina")
    print("2. Retroceder")
    print("3. Ver pagina actual")
    print("4. Salir")
    
    # Solicitud de entrada de datos por teclado al usuario.
    opcion = input("Elige una opcion (1-4): ")
    
    # Control de flujo para la Opción 1: Visitar
    if opcion == "1":
        # Captura la cadena de texto con la URL ingresada.
        url_ingresada = input("Ingresa la URL de la pagina: ")
        # Llama a la función visitar pasando la cadena como argumento.
        visitar(url_ingresada)
        
    # Control de flujo para la Opción 2: Retroceder
    elif opcion == "2":
        # Executa la desapilación (pop) de la página actual.
        retroceder()
        
    # Control de flujo para la Opción 3: Consultar estado
    elif opcion == "3":
        # Inspecciona la cima de la pila (peek).
        pagina_actual()
        
    # Control de flujo para la Opción 4: Salir
    elif opcion == "4":
        print("Navegador cerrado.")
        # La instrucción 'break' interrumpe la ejecución del bucle 'while True'.
        break
        
    # Manejo de entradas inválidas por el usuario.
    else:
        print("Opcion incorrecta. Por favor, elige un numero del 1 al 4.")