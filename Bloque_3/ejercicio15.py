"""
Ejercicio 15: Cálculo del área de un círculo usando pi.
"""

import math


def area_circulo(radio: float) -> float:
    """
    Calcula el área de un círculo usando la fórmula pi * r^2.
    """
    return round(math.pi * (radio ** 2), 2)


def main() -> None:
    radio = float(input("Digite el radio del círculo: "))
    area = area_circulo(radio)
    print(f"El área del círculo es: {area}")


if __name__ == "__main__":
    main()
