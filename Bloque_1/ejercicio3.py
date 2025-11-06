"""
Ejercicio 3: Contador usando closures.
"""


def crear_contador():
    """
    Crea un contador independiente, usando un closure.

    Returns:
        function: Función que, al llamarse, incrementa y devuelve el conteo.
    """
    conteo = 0

    def incrementar():
        nonlocal conteo
        conteo += 1
        return conteo

    return incrementar


def main() -> None:
    contador_a = crear_contador()
    contador_b = crear_contador()

    print("Contador A:", contador_a())  # 1
    print("Contador A:", contador_a())  # 2
    print("Contador B:", contador_b())  # 1
    print("Contador A:", contador_a())  # 3
    print("Contador B:", contador_b())  # 2


if __name__ == "__main__":
    main()
