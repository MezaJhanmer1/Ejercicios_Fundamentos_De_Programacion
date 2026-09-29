# ==========================================
# SISTEMA DE GESTIÓN DE TURNOS BANCARIOS
# ESTRUCTURA DE DATOS: COLA (QUEUE - FIFO)
# ==========================================

# Importamos el contenedor lineal 'deque' desde el módulo collections.
# Optimiza el tiempo de ejecución en inserciones y extracciones en los extremos.
from collections import deque


# Inicializamos la cola vacía para almacenar las solicitudes de los clientes.
cola = deque()


# ==========================================
# a) REGISTRO DE TURNOS (ENQUEUE)
# ==========================================

# Función para registrar y agregar un nuevo cliente al final de la fila.
def tomar_turno(cliente):

    # Insertamos el nuevo cliente en la última posición (tope posterior) de la cola.
    # La operación append() simula la llegada al final de la fila.
    cola.append(cliente)

    # Confirmamos en pantalla la identidad del cliente recién ingresado.
    print("Cliente que tomó turno:", cliente)

    # Desplegamos el estado actualizado del contenedor de turnos.
    print("Cola actual:", list(cola))


# ==========================================
# b) ATENCIÓN AL CLIENTE (DEQUEUE)
# ==========================================

# Procesa al cliente en el frente de la cola aplicando la regla FIFO (First In, First Out).
def atender():

    # Evaluamos si existen elementos pendientes dentro del contenedor.
    if len(cola) > 0:

        # Removemos el elemento ubicado en el frente (inicio) de la cola.
        # Implementa el principio FIFO: el primero en llegar es el primero en ser atendido.
        cliente = cola.popleft()

        # Desplegamos la información del cliente que está siendo procesado.
        print("Atendiendo a:", cliente)

    else:

        # Manejamos el caso base en que no hay elementos registrados para procesar.
        print("No hay clientes esperando.")


# ==========================================
# c) CONSULTA DEL ESTADO DE LA COLA
# ==========================================

# Inspecciona y despliega el total de elementos y el contenido actual de la cola.
def mostrar_cola():

    # Consultamos la dimensión actual del contenedor (cantidad de elementos).
    print("Cantidad de clientes esperando:", len(cola))

    # Verificamos si la cola contiene al menos un registro.
    if len(cola) > 0:

        # Convertimos la estructura 'deque' a lista exclusivamente para facilitar su lectura en consola.
        print("Clientes en espera:", list(cola))

    else:

        # Notificamos cuando la estructura se encuentra completamente vacía.
        print("La cola está vacía.")


# ==========================================
# d) SIMULACIÓN DE OPERACIONES EN EL BANCO
# ==========================================

# Solicitamos el ingreso masivo inicial de 4 usuarios.
print("\n===== INGRESAN 4 CLIENTES =====")

for i in range(4):

    # Capturamos el identificador o nombre del cliente desde la consola.
    cliente = input("Ingrese el nombre del cliente: ")

    # Registramos el turno del cliente invocando la función de inserción.
    tomar_turno(cliente)


# Imprimimos la vista general del estado inicial de la cola.
print("\n===== COLA ACTUAL =====")
mostrar_cola()


# ==========================================
# PROCESAMIENTO DE LAS PRIMERAS ATENCIONES
# ==========================================

print("\n===== ATENDIENDO 2 CLIENTES =====")

# Procesamos al cliente ubicado en el frente de la cola (primer turno).
atender()

# Procesamos al siguiente cliente que quedó en el frente tras la primera extracción.
atender()


# Verificamos la secuencia de clientes restantes tras las dos extracciones.
print("\n===== COLA DESPUÉS DE ATENDER 2 =====")
mostrar_cola()


# ==========================================
# INSERCIÓN INTERMEDIA EN LA COLA
# ==========================================

print("\n===== ENTRA UN NUEVO CLIENTE =====")

# Capturamos los datos del cliente que llega de forma extemporánea.
cliente = input("Ingrese el nombre del nuevo cliente: ")

# Añadimos al cliente al final de la cola existente.
tomar_turno(cliente)


# Desplegamos la distribución de turnos tras la nueva incorporación.
print("\n===== COLA ACTUAL =====")
mostrar_cola()


# ==========================================
# VACIADO AUTOMÁTICO DE LA COLA
# ==========================================

print("\n===== ATENDIENDO A TODOS =====")

# Iteramos mientras el contenedor posea al menos un cliente en espera.
while len(cola) > 0:

    atender()


# ==========================================
# VERIFICACIÓN DEL ESTADO FINAL
# ==========================================

print("\n===== COLA FINAL =====")
mostrar_cola()