"""
Ejercicio 14: Lectura y procesamiento de texto.
"""

def leer_y_procesar(nombre_archivo: str) -> str:
    """
    Lee un archivo de texto, lo convierte a minúsculas y elimina saltos de línea.
    """
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        texto = archivo.read()

    texto = texto.lower()
    texto = texto.replace("\n", " ")
    return texto


def main() -> None:
    archivo = "mensaje.txt"  # debe existir en la misma carpeta
    resultado = leer_y_procesar(archivo)
    print("\n--- TEXTO PROCESADO ---")
    print(resultado)


if __name__ == "__main__":
    main()
