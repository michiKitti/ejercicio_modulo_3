"""
Ejercicio 7: Filtrado de estudiantes usando filter y lambda.
"""

from typing import List, Tuple


def filtrar_aprobados(estudiantes: List[Tuple[str, float]]) -> List[Tuple[str, float]]:
    """
    Filtra únicamente los estudiantes con nota igual o superior a 3.0.

    Args:
        estudiantes (List[Tuple[str, float]]): Lista de tuplas (nombre, nota).

    Returns:
        List[Tuple[str, float]]: Lista de estudiantes aprobados.
    """
    return list(filter(lambda e: e[1] >= 3.0, estudiantes))


def main() -> None:
    estudiantes = [
        ("Ana", 4.5),
        ("Juan", 2.8),
        ("Maria", 3.9),
        ("Diana", 1.5),
    ]

    aprobados = filtrar_aprobados(estudiantes)
    print("Estudiantes aprobados:", aprobados)


if __name__ == "__main__":
    main()
