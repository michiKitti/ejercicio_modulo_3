"""
    se debe crear un generador de usuarios que lleve no mbre edad
    hobbies redes sociales con funciones como aceptar un nombre y una edad
    como argumentos posicionales obligatorios ademas de asceptar la cantidad deseada de hobbies que el usuario desee
    como argumentos de longitud variable"""

def crear_perfil(usuario: float) -> None:

    nombre:str = input("Ingresa tu nombre: ")
    edad:int = int(input("Ingresa tu edad: "))
    hobbies: tuple[str, ...] = tuple(input("Ingresa tus hobbies separados por coma: ").split(","))
    redes_sociales :str = input("Ingresa tu redes sociales: ")
    return None

"""
Genera un perfil de usuario con su nombre, edad, hobbies y redes sociales.

Parámetros:
- nombre (str): nombre del usuario.
- edad (int): edad del usuario.
- *hobbies (str): lista de hobbies opcionales.
- **redes_sociales (str): redes sociales con sus usuarios.

Retorna:
- str: texto formateado con toda la información del perfil.

Ejemplo:
crear_perfil("Allison", 19, "leer", "bailar", twitter="@alli", instagram="@allisonm")
"""







