import json

ARCHIVO = "inventario.json"


def guardar_inventario(inventario):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, indent=4)


def cargar_inventario():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


def agregar_producto():
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))

    inventario = cargar_inventario()
    inventario.append({"nombre": nombre, "cantidad": cantidad})
    guardar_inventario(inventario)

    print("✅ Producto guardado con éxito!")


def ver_inventario():
    inventario = cargar_inventario()

    print("\n--- INVENTARIO ---")
    if not inventario:
        print("No hay productos aún.")
        return

    for producto in inventario:
        print(f"{producto['nombre']} - {producto['cantidad']} unidades")
    print()


def main():
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_inventario()
        elif opcion == "3":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción no válida")


if __name__ == "__main__":
    main()
