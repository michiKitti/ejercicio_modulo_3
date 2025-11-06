"""
Ejercicio 12: Analizador de columnas numéricas en archivos CSV.
"""

import csv
from typing import Dict


def analizar_csv(nombre_archivo: str, columna: str) -> Dict[str, float]:
    """
    Lee un archivo CSV y calcula promedio, máximo y mínimo de una columna numérica.

    Args:
        nombre_archivo (str): Ruta del archivo CSV a analizar.
        Columna (str): Nombre de la columna numérica.

    Returns:
        Dict[str, float]: Diccionario con promedio, máximo y mínimo.
        :param nombre_archivo:
        :param columna:
    """
    valores = []

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if columna not in fila:
                raise ValueError(f"La columna '{columna}' no existe en el archivo.")
            valores.append(float(fila[columna]))

    if not valores:
        raise ValueError("La columna no contiene datos numéricos.")

    promedio = round(sum(valores) / len(valores), 2)
    maximo = max(valores)
    minimo = min(valores)

    return {
        "promedio": promedio,
        "maximo": maximo,
        "minimo": minimo,
    }


def main() -> None:
    archivo = "estudiantes.csv"  # Debe existir junto al script
    columna = "qualification"

    resultados = analizar_csv(archivo, columna)

    print("\n--- RESULTADOS DEL ARCHIVO ---")
    for clave, valor in resultados.items():
        print(f"{clave.capitalize()}: {valor}")


if __name__ == "__main__":
    main()
