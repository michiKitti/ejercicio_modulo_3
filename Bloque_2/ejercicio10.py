"""
Ejercicio 10: Exploración recursiva de estructuras de datos.
"""

from typing import Any


def explorar_estructura(elemento: Any, profundidad: int = 1) -> None:
    """
    Explora estructuras de datos (listas, tuples, diccionarios) e imprime los valores no iterables.

    Args:
        elemento (Any): Estructura a explorar.
        Profundidad (int): Nivel actual de profundidad (inicia en 1).
        :param elemento:
        :param profundidad:
    """
    # Caso base: si es un valor simple → imprimir
    if isinstance(elemento, (int, float, str, bool, type(None))):
        print(f"Valor: {elemento}, Profundidad: {profundidad}")
        return

    # Si es lista o tuple → explorar cada elemento
    if isinstance(elemento, (list, tuple)):
        for e in elemento:
            explorar_estructura(e, profundidad + 1)
        return


    if isinstance(elemento, dict):
        for valor in elemento.values():
            explorar_estructura(valor, profundidad + 1)
        return

    # Si no sabemos qué es → lo mostramos sin recursión
    print(f"Valor desconocido ({type(elemento).__name__}): {elemento}, Profundidad: {profundidad}")


def main() -> None:
    datos = [1, [2, 3], {"a": 4, "b": [5, {"c": 6}]}]
    explorar_estructura(datos)


if __name__ == "__main__":
    main()
