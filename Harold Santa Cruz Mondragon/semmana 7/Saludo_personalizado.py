def construir_saludo(nombre: str) -> str:
    nombre_limpio = nombre.strip()
    if not nombre_limpio:
        return "¡Hola! Bienvenido al curso."
    return f"¡Hola, {nombre_limpio.upper()}! Bienvenido al curso."

def main():
    entrada = input("¿Cómo te llamas? ")
    print(construir_saludo(entrada))

if __name__ == "__main__":
    main()