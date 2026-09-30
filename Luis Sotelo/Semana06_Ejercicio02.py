
historial = []


def visitar(url):
    historial.append(url)		#Agregar una página a la pila
    print(f"Visitando: {url}")
    print(f"Pila actual: {historial}\n")


def retroceder():
    if len(historial) > 1:
        historial.pop()  		#Quitar la última página
        print("← Retrocediendo...")
        # Mostramos la página actual llamando a la función de abajo
        print(f"Regresó a: {pagina_actual()}")
        print(f"Pila actual: {historial}\n")
    else:
        print("⚠️ No puedes retroceder más, es la primera página.\n")


def pagina_actual():
    if len(historial) > 0:		#Ver la última página sin quitarla
        return historial[-1]  # El índice -1 siempre es el último elemento en Python
    return "Historial vacío"

visitar("Google")
visitar("YouTube")
visitar("GitHub")

retroceder()
retroceder()