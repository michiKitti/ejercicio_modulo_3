"""
Ejercicio 2: Generador de perfiles usando *args y **kwargs.
"""


def crear_perfil(nombre: str, edad: int, *hobbies: str, **redes_sociales: str) -> str:
    """
    Genera una descripción de perfil con hobbies y redes sociales opcionales.

    Args:
        nombre (str): Nombre de la persona.
        Edad (int): Edad de la persona.
        *hobbies (str): Lista variable de hobbies.
        **redes_sociales (str): Diccionario donde la clave es la red social
                               y el valor es el usuario en esa red.

    Returns:
        str: Perfil formateado.
        :param nombre:
        :param edad:
    """
    perfil = f"Nombre: {nombre}\nEdad: {edad} años\n"

    if hobbies:
        perfil += "Hobbies:\n"
        for hobby in hobbies:
            perfil += f"  - {hobby}\n"
    else:
        perfil += "Hobbies: No especificados\n"

    if redes_sociales:
        perfil += "Redes Sociales:\n"
        for red, usuario in redes_sociales.items():
            perfil += f"  - {red}: {usuario}\n"
    else:
        perfil += "Redes Sociales: No registradas\n"

    return perfil.strip()


def main() -> None:
    print("Ejemplo de uso:\n")
    perfil = crear_perfil(
        "Valery",
        20,
        "Cantar", "Hacer postres", "Dormir",
        instagram="@valery", tiktok="@valery_123"
    )
    print(perfil)


if __name__ == "__main__":
    main()





