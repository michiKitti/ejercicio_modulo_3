"""
    Create a program that asks the user for their weight (in kg) and height (in meters).
    Calculate the BMI using the formula:
"""

# Ejercicio IMC robusto: aceptación de cm, comas decimales, extracción de números y control de intentos.

import re
from typing import Tuple

"""
 re Programa para calcular el Índice de Masa Corporal (IMC).

"""


def parse_number(text: str) -> float | None:
    """
    Se Intenta convertir una entrada de usuario a float:
    - Reemplaza comas por puntos.
    - Extrae el primer patrón numérico si hay texto adicional (p. ej. "1.75m").
    - Devuelve None si no puede extraer un número.
    """
    if not text:
        return None
    s = text.strip().lower()
    if s in {"salir", "exit", "q"}:
        raise KeyboardInterrupt  # manejamos salir desde el llamador

    s = s.replace(",", ".")
    # Buscamos la primera ocurrencia de número con opcional parte decimal
    m = re.search(r"\d+(?:\.\d+)?", s)
    if not m:
        return None
    try:
        return float(m.group(0))
    except ValueError:
        return None


def ajustar_unidades_altura(altura: float) -> float:
    """
    Ajusto la altura si parece estar en centímetros.
    Regla práctica:
      - Si la altura es mayor que 3 (metros), asumimos que está en cm y la convertimos (/100).
      - Si la altura está entre 2.5 y 3.0 m pedimos confirmación más abajo.
    """
    if altura > 3.0:
        # Probablemente el usuario introdujo centímetros (ej. 170)
        return altura / 100.0
    return altura


def confirmar_valor(valor: float, nombre: str, min_ok: float, max_ok: float) -> bool:
    """
    Si el valor está fuera del rango razonable [min_ok, max_ok], pregunto al usuario si está seguro.
    Retorna True si el valor se acepta, False para reintentar.
    """
    if min_ok <= valor <= max_ok:
        return True

    print(f"Advertencia: el {nombre} = {valor} parece inusual.")
    while True:
        respuesta = input(f"¿Deseas usar {valor} como {nombre}? (s/n) ").strip().lower()
        if respuesta in ("s", "si", "y", "yes"):
            return True
        if respuesta in ("n", "no"):
            return False
        if respuesta in ("salir", "exit", "q"):
            raise KeyboardInterrupt


def pedir_datos_usuario(max_intentos: int = 5) -> Tuple[float, float]:
    """
    Se pide peso y altura al usuario, con parseo tolerante y validaciones.
    - max_intentos: número máximo de intentos antes de salir.
    - Permite escribir 'salir' para terminar.
    Retorna (peso, altura) en kg y metros.
    """
    intentos = 0
    while intentos < max_intentos:
        try:
            texto_peso = input("Digite su peso en Kg (o 'salir' para terminar): ").strip()
            peso_val = parse_number(texto_peso)

            texto_altura = input("Digite su altura en metros (ej. 1.75) o en cm (ej. 175): ").strip()
            altura_val = parse_number(texto_altura)

            if peso_val is None or altura_val is None:
                print("No se reconoció un número válido. Usa un formato como 70, 70.0 o 1.75. Intenta de nuevo.\n")
                intentos += 1
                continue

            # Ajustar altura si parece estar en cm
            altura_val = ajustar_unidades_altura(altura_val)

            # Rangos razonables
            peso_ok = confirmar_valor(peso_val, "peso (kg)", 2.0, 500.0)
            if not peso_ok:
                intentos += 1
                continue

            altura_ok = confirmar_valor(altura_val, "altura (m)", 0.3, 3.0)
            if not altura_ok:
                intentos += 1
                continue

            return peso_val, altura_val

        except KeyboardInterrupt:
            print("\nPrograma finalizado por el usuario.")
            raise

        except Exception:
            # cualquier otro error no esperado
            print("Ocurrió un error al procesar la entrada. Intenta de nuevo.\n")
            intentos += 1

    raise SystemExit(f"Se alcanzaron {max_intentos} intentos fallidos. Ejecuta de nuevo si deseas continuar.")


def calcular_imc(peso: float, altura: float) -> float:
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso y altura deben ser mayores que cero.")
    imc = peso / (altura ** 2)
    return round(imc, 2)


def interpretar_imc(imc: float) -> str:
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"


def main() -> None:
    try:
        peso_usuario, altura_usuario = pedir_datos_usuario()
    except SystemExit as e:
        print(e)
        return
    except KeyboardInterrupt:
        return

    imc_usuario = calcular_imc(peso_usuario, altura_usuario)
    clasificacion = interpretar_imc(imc_usuario)

    print("\n--- Resultado ---")
    print(f"Peso: {peso_usuario} kg")
    print(f"Altura: {altura_usuario} m")
    print(f"Su IMC es: {imc_usuario:.2f}")
    print(f"Clasificación: {clasificacion}")


if __name__ == "__main__":
    main()

