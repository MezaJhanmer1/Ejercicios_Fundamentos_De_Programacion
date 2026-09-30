
# 1. IMPORTAR LA LIBRERÍA DE COLAS
# Importamos 'deque' de la librería 'collections'.
# Esto nos da una cola real y eficiente para agregar y quitar elementos.
from collections import deque

# 2. CREACIÓN DE LA COLA
# Creamos una cola vacía usando deque(). 
# A diferencia de una lista normal, deque está optimizada para sacar el primer elemento rápidamente.
cola_banco = deque()

# 3. FUNCIONES DEL SISTEMA (Puntos a, b y c del enunciado)

# a) Función para que un cliente tome turno
def tomar_turno(cliente):
    # .append() significa "agregar al final". 
    # Toma el nombre del 'cliente' y lo pone al final de la cola.
    cola_banco.append(cliente) 
    # Imprime un mensaje avisando que el cliente se unió a la fila.
    print(f"-> {cliente} ha tomado un turno.")

# b) Función para atender al primer cliente de la cola
def atender():
    # len() cuenta cuántos elementos hay en la cola. 
    # Si hay más de 0 (es decir, si hay gente en la fila), entra al 'if'.
    if len(cola_banco) > 0:
        # .popleft() saca al PRIMER elemento de la cola (el de la izquierda). 
        # ¡Esto es lo que hace que sea una Cola FIFO (First In, First Out)!
        cliente_atendido = cola_banco.popleft() 
        # Imprime el mensaje de que ese cliente está siendo atendido.
        print(f"<- Atendiendo a: {cliente_atendido}")
    else:
        # Si la cola estaba vacía (len = 0), entra aquí y avisa que no hay nadie.
        print("No hay clientes en la fila para atender.")

# c) Función para mostrar cuántos esperan y sus nombres
def mostrar_cola():
    # Imprime cuántos clientes hay en total en la fila usando len()
    print(f"   [Clientes esperando: {len(cola_banco)}]")
    # Imprime la cola completa. Usamos list() para convertir el deque a una lista normal y que se vea más bonito.
    print(f"   [Fila actual: {list(cola_banco)}]")


# --- 4. SIMULACIÓN PASO A PASO (Punto d del enunciado) ---

# Imprime un título en pantalla
print("--- INICIO DE LA SIMULACIÓN ---")

# PASO 1: Pedir al usuario los nombres de los 4 clientes
print("\n1. Entran 4 clientes:")
# 'for i in range(4)' crea un bucle que se repetirá 4 veces (i será 0, 1, 2 y 3)
for i in range(4):
    # input() detiene el programa y pide al usuario que escriba un nombre.
    nombre = input(f"Ingresa el nombre del cliente {i+1}: ")
    # Llama a la función 'tomar_turno' y le pasa el nombre que el usuario escribió.
    tomar_turno(nombre)

# Al terminar el bucle de 4, muestra cómo quedó la fila
mostrar_cola() 

# PASO 2: Atender a los 2 primeros
print("\n2. Se atienden 2 clientes:")
# Llama a la función 'atender()'. Saca al primer cliente de la fila.
atender() 
# Llama a la función 'atender()' otra vez. Saca al segundo cliente de la fila.
atender() 
# Muestra la fila actual (ahora deberían quedar solo 2 clientes).
mostrar_cola() 

# PASO 3: Pedir el nombre del 5to cliente
print("\n3. Entra 1 cliente más:")
# Pide al usuario que escriba el nombre del quinto cliente.
nombre = input("Ingresa el nombre del cliente 5: ")
# Agrega a este nuevo cliente al final de la cola.
tomar_turno(nombre)
# Muestra la fila (deberían haber 3 clientes ahora).
mostrar_cola()

# PASO 4: Atender a todos los que quedan en la fila
print("\n4. Se atienden todos:")
# 'while len(cola_banco) > 0' significa: "Mientras la cola tenga más de 0 elementos, repite esto".
# El bucle se repetirá automáticamente hasta que la cola quede vacía.
while len(cola_banco) > 0:
    # Llama a la función 'atender()'. Saca al primero de la fila.
    atender()

# Cuando el bucle 'while' termina (porque ya no hay nadie), muestra la fila. Debería estar vacía [].
mostrar_cola() 
# Imprime el mensaje de finalización del programa.
print("\n--- FIN DE LA SIMULACIÓN ---")