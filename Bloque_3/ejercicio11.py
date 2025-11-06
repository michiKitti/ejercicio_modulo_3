"""
Ejercicio 11: Gestor de tareas usando archivo .txt
"""

from typing import List

ARCHIVO_TAREAS = "tareas.txt"


def agregar_tarea(tarea: str) -> None:
    """
    Agrega una tarea al archivo tareas.txt
    """
    with open(ARCHIVO_TAREAS, "a", encoding="utf-8") as archivo:
        archivo.write(tarea + "\n")


def ver_tareas() -> List[str]:
    """
    Retorna una lista con todas las tareas guardadas.
    """
    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
            return [linea.strip() for linea in archivo.readlines()]
    except FileNotFoundError:
        return []


def mostrar_tareas(tareas: List[str]) -> None:
    """
    Muestra las tareas en forma de lista enumerada.
    """
    if not tareas:
        print("\nNo hay tareas registradas.\n")
        return

    print("\n--- LISTA DE TAREAS ---")
    for i, tarea in enumerate(tareas, start=1):
        print(f"{i}. {tarea}")
    print()


def main() -> None:
    """
    Menú principal del programa.
    """
    while True:
        print("\n--- GESTOR DE TAREAS ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Salir")

        option = input("Selecciona una opción: ")

        if option == "1":
            tarea = input("Escribe la tarea: ")
            agregar_tarea(tarea)
            print(" Tarea agregada.")
        elif option == "2":
            tareas = ver_tareas()
            mostrar_tareas(tareas)
        elif option == "3":
            print(" Saliendo del programa...")
            break
        else:
            print(" Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
