"""
Ejercicio 4: Función que aplica validadores a listas de datos.
"""

import re
from typing import Callable, List, Any


def aplicar_validador(datos: List[Any], validador: Callable[[Any], bool]) -> List[Any]:
    """
    Aplica una función validadora a cada elemento de la lista.

    Args:
        datos (List[Any]): Lista de valores a validar.
         (Callable[[Any], bool]): Función que determina
                                          si un elemento es válido o no.

    Returns:
        List[Any]: Nueva lista solo con los elementos válidos.
        :param datos:
        :param validador:
        :param validador:
    """
    return [elemento for elemento in datos if validador(elemento)]


def es_email_valido(email: str) -> bool:
    """
    Determina si un string tiene formato válido de correo electrónico.

    Args:
        email (str): Dirección de correo a evaluar.

    Returns:
        bool: True si es válido, False si no.
    """
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(patron, email))


def es_mayor_a_10(numero: int) -> bool:
    """
    Verifica si un número es mayor a 10.

    Args:
        numero (int): Número a evaluar.

    Returns:
        bool: True si es mayor a 10, False si no.
    """
    return numero > 10


def main() -> None:
    datos = ["ana@example.com", "correo-malo", "test@mail.co"]
    mejores = aplicar_validador(datos, es_email_valido)
    print("Correos válidos:", mejores)

    numerous = [2, 35, 10, 50]
    mayores = aplicar_validador(numerous, es_mayor_a_10)
    print("Mayores a 10:", mayores)


if __name__ == "__main__":
    main()
