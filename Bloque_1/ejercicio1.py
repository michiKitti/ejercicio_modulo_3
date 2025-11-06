"""
Programa para calcular el Índice de Masa Corporal (IMC) de forma segura,
validando entradas y manejando diferentes formatos y unidades.
"""

import re
from typing import Tuple


def parse_number(text: str) -> float | None:
    """
    Convierte una entrada a float. Permite comas y extrae el primer número encontrado.

    Args:
        text (str): Entrada del usuario.

    Returns:
        float | None: Valor numérico o None si no se puede convertir.
    """
    if not text:
        return None
    s = text.strip().lower()
    if s in {"salir", "exit", "q"}:
        raise KeyboardInterrupt

    s = s.replace(",", ".")
    match = re.search(r"\d+(?:\.\d+)?", s)
    if not match:
        return None
    return float(match.group(0))


def ajustar_unidades_altura(altura: float) -> float:
    """
    Convierte altura en centímetros a metros si es necesario.

    Args:
        altura (float): Altura en m o cm.

    Returns:
        float: Altura en metros.
    """
    return altura / 100 if altura > 3 else altura


def confirmar_valor(valor: float, nombre: str, min_ok: float, max_ok: float) -> bool:
    """
    Confirma valores fuera de rango razonable.

    Args:
        valor (float): Valor ingresado.
        nombre (str): Etiqueta (peso o altura).
        min_ok (float): Límite inferior.
        max_ok (float): Límite superior.

    Returns:
        bool: True si se acepta el valor, False si desea reingresarlo.
    """
    if min_ok <= valor <= max_ok:
        return True

    print(f"Advertencia: el {nombre} = {valor} parece inusual.")
    respuesta = input(f"¿Deseas usarlo? (s/n) ").strip().lower()
    return respuesta in ("s", "si", "y", "yes")


def pedir_datos_usuario(max_intentos: int = 5) -> Tuple[float, float]:
    """
    Solicita peso y altura al usuario con validaciones.

    Args:
        max_intentos (int): Intentos permitidos.

    Returns:
        Tuple[float, float]: Peso en kg y altura en metros.
    """
    intentos = 0
    while intentos < max_intentos:
        try:
            peso = parse_number(input("Digite su peso (kg): "))
            altura = parse_number(input("Digite su altura (m o cm): "))

            if peso is None or altura is None:
                print("Entrada inválida. Intenta de nuevo.\n")
                intentos += 1
                continue

            altura = ajustar_unidades_altura(altura)

            if not confirmar_valor(peso, "peso (kg)", 2, 500):
                intentos += 1
                continue
            if not confirmar_valor(altura, "altura (m)", 0.3, 3):
                intentos += 1
                continue

            return peso, altura

        except KeyboardInterrupt:
            raise

    raise SystemExit("Demasiados intentos fallidos.")


def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula el IMC.

    Returns:
        float: IMC redondeado a 2 decimales.
    """
    return round(peso / (altura ** 2), 2)


def interpretar_imc(imc: float) -> str:
    """
    Interpreta el resultado del IMC.

    Returns:
        str: Categoría del IMC.
    """
    if imc < 18.5:
        return "Bajo peso"
    if imc < 25:
        return "Peso normal"
    if imc < 30:
        return "Sobrepeso"
    return "Obesidad"


def main() -> None:
    try:
        peso, altura = pedir_datos_usuario()
        imc = calcular_imc(peso, altura)
        categoria = interpretar_imc(imc)

        print("\n--- Resultado ---")
        print(f"Peso: {peso} kg")
        print(f"Altura: {altura} m")
        print(f"IMC: {imc}")
        print(f"Clasificación: {categoria}")

    except KeyboardInterrupt:
        print("\nPrograma finalizado por el usuario.")


if __name__ == "__main__":
    main()
