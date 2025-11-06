"""
Ejercicio 9: Uso de functools. Reduce para operaciones acumulativas.
"""

from functools import reduce
from typing import List


def sumar_lista(numerous: List[int]) -> int:
    """
    Suma todos los números de una lista usando reduce.

    Args:
        numerous (List[int]): Lista de números enteros.

    Returns:
        int: Resultado de la suma.
    """
    return reduce(lambda x, y: x + y, numerous)


def concatenar_texto(partes: List[str]) -> str:
    """
    Une una lista de strings en una sola cadena usando reduce.

    Args:
        partes (List[str]): Lista de strings.

    Returns:
        str: Cadena resultante.
    """
    return reduce(lambda x, y: x + y, partes)


def main() -> None:
    numerous = [1, 2, 3, 4, 5]
    texto = ["Hola", " ", "SENA", "!"]

    print("Suma:", sumar_lista(numerous))
    print("Texto:", concatenar_texto(texto))


if __name__ == "__main__":
    main()

