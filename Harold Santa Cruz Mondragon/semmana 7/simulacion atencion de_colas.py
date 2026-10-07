from collections import deque
from typing import Deque

class Banco:
    def __init__(self):
        self.fila: Deque[str] = deque()

    def registrar_llegada(self, nombre: str) -> None:
        nombre = nombre.strip()
        if not nombre:
            print("Nombre inválido. No se registró turno.")
            return
        self.fila.append(nombre)
        print(f"[REGISTRO] {nombre} ha tomado turno.")
        print(f"Fila actual: {list(self.fila)}")

    def llamar_siguiente(self) -> None:
        if self.fila:
            cliente = self.fila.popleft()
            print(f"[ATENCIÓN] Pasando a ventanilla: {cliente}")
        else:
            print("[AVISO] No hay turnos pendientes.")

    def mostrar_estado(self) -> None:
        total = len(self.fila)
        print(f"Turnos en espera: {total}")
        if total:
            print("Próximos clientes:", " -> ".join(self.fila))
        else:
            print("La fila está vacía.")

def main():
    banco = Banco()
    print("=== APERTURA DE CAJA ===")
    for i in range(4):
        nombre = input(f"Nombre del cliente {i+1}: ")
        banco.registrar_llegada(nombre)

    print("\n=== ESTADO INICIAL ===")
    banco.mostrar_estado()

    print("\n=== DOS ATENCIONES ===")
    banco.llamar_siguiente()
    banco.llamar_siguiente()

    print("\n=== FILA TRAS DOS ATENCIONES ===")
    banco.mostrar_estado()

    print("\n=== LLEGADA TARDÍA ===")
    nuevo = input("Nombre del nuevo cliente: ")
    banco.registrar_llegada(nuevo)

    print("\n=== ESTADO ACTUALIZADO ===")
    banco.mostrar_estado()

    print("\n=== VACIADO DE FILA ===")
    while banco.fila:
        banco.llamar_siguiente()

    print("\n=== ESTADO FINAL ===")
    banco.mostrar_estado()

if __name__ == "__main__":
    main()