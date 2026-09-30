#Simula el sistema de turnos de un banco usando una Cola (Queue). Los clientes esperan en orden de
#llegada.


from collections import deque


cola_clientes = deque()

# Agregar clientes a la cola
cola_clientes.append("Cliente 1")
cola_clientes.append("Cliente 2")
cola_clientes.append("Cliente 3")

# Atender clientes
while cola_clientes:
    cliente = cola_clientes.popleft()
    print(f"Atendiendo a {cliente}")
#atencion de clientes
def atender_cliente():
    if cola_clientes:
        cliente = cola_clientes.popleft()
        print(f"Atendiendo a {cliente}")
    else:
        print("No hay clientes en la cola.")
#el estado de la cola
def mostrar_cola():
    if cola_clientes:
        print("Clientes en la cola:", list(cola_clientes))
    else:
        print("No hay clientes en la cola.")
#operacion en el banco
print("Bienvenido al sistema de atención al cliente del banco.")
for i in range(4):
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    cola_clientes.append(nombre_cliente)
    print(f"{nombre_cliente} ha sido agregado a la cola.")
#imprimimos la vista general inicial de la cola
print("Estado actual de la cola:")
mostrar_cola()
#atendemos a los clientes
atender_cliente()
atender_cliente()
#verificamos la secuencia de la cola
print("Estado actual de la cola después de atender a dos clientes:")
mostrar_cola()

#insercion intermedia en la cola
print("Agregando un cliente nuevo a la cola.")
tomar_turno = input("Ingrese el nombre del cliente: ")
tomar_turno=(cliente)
#vaciando automáticamente la cola
print("Vaciando la cola de clientes...")
while len(cola_clientes) > 0:
    atender_cliente()
#verificamos la cola
print("Estado final de la cola:")
mostrar_cola()
