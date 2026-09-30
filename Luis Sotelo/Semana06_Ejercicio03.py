

cola_banco = []


def tomar_turno(cliente):
    cola_banco.append(cliente)		#Agregar un cliente al final de la cola
    print(f"🎫 {cliente} tomó un turno y entró a la cola.")
    mostrar_cola()

def atender():
    if len(cola_banco) > 0:	#Atender al 1er cliente de la cola (sale de la posición 0)
        cliente_atendido = cola_banco.pop(0) 	# El 0 borra y devuelve al primero
        print(f"🔔 Atendiendo a: {cliente_atendido}")
        mostrar_cola()
    else:
        print("⚠️ No hay clientes en la cola para atender.\n")

def mostrar_cola():		#Mostrar el estado actual de la cola
    print(f"Esperando: {len(cola_banco)} clientes -> Lista: {cola_banco}\n")


print("--- 1. Entran 4 clientes ---")
tomar_turno("Ana")
tomar_turno("Pedro")
tomar_turno("Carlos")
tomar_turno("Diana")

print("--- 2. Se atienden 2 clientes ---")
atender()
atender()

print("--- 3. Entra 1 cliente más ---")
tomar_turno("Eduardo")

print("--- 4. Se atienden a todos los que quedan ---")
atender()
atender()
atender()