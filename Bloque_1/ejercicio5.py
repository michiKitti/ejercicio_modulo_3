"""
Ejercicio 5: Cálculo de IVA usando variable global.
"""

# Variable global (por defecto en Colombia)
TASA_IVA: float = 0.19


def calcular_iva(precio_base: float) -> float:
    """
    Calcula el valor del IVA para un precio dado usando la tasa actual.

    Args:
        precio_base (float): Precio sin IVA.

    Returns:
        float: Valor del IVA calculado.
    """
    if precio_base < 0:
        raise ValueError("El precio no puede ser negativo.")
    return round(precio_base * TASA_IVA, 2)


def actualizar_tasa_iva(nueva_tasa: float) -> None:
    """
    Actualiza la tasa de IVA de forma global.

    Args:
        nueva_tasa (float): Nuevo valor de la tasa IVA (ej: 0.10 para 10%).
    """
    global TASA_IVA
    if nueva_tasa < 0 or nueva_tasa > 1:
        raise ValueError("La tasa debe estar entre 0 y 1.")
    TASA_IVA = nueva_tasa


def main() -> None:
    precio = 100000

    print(f"IVA con tasa inicial ({TASA_IVA}):", calcular_iva(precio))
    actualizar_tasa_iva(0.10)
    print(f"IVA con nueva tasa ({TASA_IVA}):", calcular_iva(precio))


if __name__ == "__main__":
    main()
