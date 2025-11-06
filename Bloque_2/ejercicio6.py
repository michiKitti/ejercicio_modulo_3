"""
Ejercicio 6: Aplicar descuento usando map y funciones lambda.
"""

from typing import List, Dict


def aplicar_descuento(productos: List[Dict[str, float]]) -> List[float]:
    """
    Aplica un 10% de descuento a los precios de una lista de productos.

    Args:
        productos (List[Dict[str, float]]): Lista de productos con clave 'precio'.

    Returns:
        List[float]: Lista con los precios ya descontados.
    """
    return list(map(lambda p: round(p["precio"] * 0.9, 2), productos))


def main() -> None:
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
        {"nombre": "Zapatos", "precio": 120000},
    ]

    precios_con_descuento = aplicar_descuento(productos)
    print("Precios con descuento:", precios_con_descuento)


if __name__ == "__main__":
    main()
