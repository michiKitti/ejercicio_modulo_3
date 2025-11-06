"""
Ejercicio 8: List y Dict Comprehensions para procesar texto.
"""

from typing import List, Dict


def palabras_largas(texto: str) -> List[str]:
    """
    Obtiene palabras con más de 5 letras en mayúsculas.

    Args:
        texto (str): Texto de entrada.

    Returns:
        List[str]: Lista de palabras filtradas en mayúsculas.
    """
    return [palabra.upper() for palabra in texto.split() if len(palabra) > 5]


def mapa_longitudes(palabras: List[str]) -> Dict[str, int]:
    """
    Crea un diccionario donde cada palabra se asocia con su longitud.

    Args:
        palabras (List[str]): Lista de palabras.

    Returns:
        Dict[str, int]: Diccionario {palabra: longitud}
    """
    return {palabra: len(palabra) for palabra in palabras}


def main() -> None:
    texto = "Este es un Ejemplo de procesamiento de texto en Python donde algunasPalabras son largas"
    lista = palabras_largas(texto)
    diccionario = mapa_longitudes(lista)

    print("Lista:", lista)
    print("Diccionario:", diccionario)


if __name__ == "__main__":
    main()
