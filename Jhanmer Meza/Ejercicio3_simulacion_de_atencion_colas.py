# ==========================================
# SISTEMA DE TURNOS DE UN BANCO
# COLA (QUEUE) - FIFO
# ==========================================

# Importamos deque desde collections.
# deque nos permite trabajar fácilmente con una cola.
from collections import deque


# Creamos una cola vacía.
cola = deque()


# ==========================================
# a) TOMAR TURNO
# ==========================================

def tomar_turno(cliente):

    # Agregamos el cliente al FINAL de la cola.
    # append() agrega un elemento al final.
    cola.append(cliente)

    # Mostramos el cliente que acaba de entrar.
    print("Cliente que tomó turno:", cliente)

    # Mostramos cómo quedó la cola.
    print("Cola actual:", list(cola))


# ==========================================
# b) ATENDER
# ==========================================

def atender():

    # Verificamos si hay clientes esperando.
    if len(cola) > 0:

        # popleft() elimina el PRIMER elemento
        # de la cola.
        #
        # Esto representa FIFO:
        # Primero en entrar, primero en salir.
        cliente = cola.popleft()

        # Mostramos el cliente que está siendo atendido.
        print("Atendiendo a:", cliente)

    else:

        # Si no hay clientes, mostramos este mensaje.
        print("No hay clientes esperando.")


# ==========================================
# c) MOSTRAR COLA
# ==========================================

def mostrar_cola():

    # len() nos indica cuántos clientes
    # están esperando.
    print("Cantidad de clientes esperando:", len(cola))

    # Verificamos si hay clientes.
    if len(cola) > 0:

        # Convertimos la cola en lista solamente
        # para mostrarla de una manera más sencilla.
        print("Clientes en espera:", list(cola))

    else:

        print("La cola está vacía.")


# ==========================================
# d) SIMULACIÓN
# ==========================================

# Pedimos que ingresen 4 clientes.
print("\n===== INGRESAN 4 CLIENTES =====")

for i in range(4):

    # Pedimos el nombre del cliente.
    cliente = input("Ingrese el nombre del cliente: ")

    # El cliente toma su turno.
    tomar_turno(cliente)


# Mostramos la cola.
print("\n===== COLA ACTUAL =====")
mostrar_cola()


# ==========================================
# ATENDER A 2 CLIENTES
# ==========================================

print("\n===== ATENDIENDO 2 CLIENTES =====")

# Atendemos al primer cliente.
atender()

# Atendemos al segundo cliente.
atender()


# Mostramos cómo quedó la cola.
print("\n===== COLA DESPUÉS DE ATENDER 2 =====")
mostrar_cola()


# ==========================================
# ENTRA UN CLIENTE MÁS
# ==========================================

print("\n===== ENTRA UN NUEVO CLIENTE =====")

# Pedimos el nombre del nuevo cliente.
cliente = input("Ingrese el nombre del nuevo cliente: ")

# Agregamos el nuevo cliente al final.
tomar_turno(cliente)


# Mostramos la cola nuevamente.
print("\n===== COLA ACTUAL =====")
mostrar_cola()


# ==========================================
# ATENDER A TODOS LOS CLIENTES RESTANTES
# ==========================================

print("\n===== ATENDIENDO A TODOS =====")

# Mientras haya clientes en la cola,
# seguimos atendiendo.
while len(cola) > 0:

    atender()


# ==========================================
# MOSTRAR COLA FINAL
# ==========================================

print("\n===== COLA FINAL =====")
mostrar_cola()