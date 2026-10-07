class HistorialNavegador:
    def __init__(self):
        self._paginas = []

    def abrir(self, url: str) -> None:
        url = url.strip()
        if not url:
            print("URL vacía. No se abrió ninguna página.")
            return
        self._paginas.append(url)
        print(f"Página abierta: {url}")
        print(f"Historial: {self._paginas}")

    def volver(self) -> None:
        if len(self._paginas) > 1:
            salida = self._paginas.pop()
            print(f"Saliendo de: {salida}")
            print(f"Ahora estás en: {self._paginas[-1]}")
            print(f"Historial: {self._paginas}")
        else:
            print("No se puede retroceder: no hay página anterior.")

    def actual(self) -> None:
        if self._paginas:
            print(f"Página actual: {self._paginas[-1]}")
        else:
            print("No hay páginas en el historial.")

def mostrar_menu():
    print("\n--- NAVEGADOR ---")
    print("1) Abrir página")
    print("2) Volver atrás")
    print("3) Ver página actual")
    print("4) Salir")

def main():
    historial = HistorialNavegador()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            url = input("URL: ")
            historial.abrir(url)
        elif opcion == "2":
            historial.volver()
        elif opcion == "3":
            historial.actual()
        elif opcion == "4":
            print("Cerrando navegador.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()