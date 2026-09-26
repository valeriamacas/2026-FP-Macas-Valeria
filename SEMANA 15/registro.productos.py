def mostrar_menu():
    print("\n" + "=" * 35)
    print("   SISTEMA DE GESTIÓN DE TIENDA")
    print("=" * 35)
    print("1. Registrar nuevo producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar un producto")
    print("4. Eliminar un producto")
    print("5. Salir")
    print("=" * 35)


def main():
    productos_unicos = set()

    precios = {}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            print("\n--- REGISTRAR PRODUCTO ---")
            nombre = input("Nombre del producto: ").strip().capitalize()

            if not nombre:
                print("⚠️ El nombre del producto no puede estar vacío.")
                continue

            try:
                precio = float(input("Precio del producto ($): "))
                if precio < 0:
                    print("⚠️ El precio no puede ser negativo.")
                    continue

                if nombre in productos_unicos:
                    print(f"ℹ️ El producto '{nombre}' ya existía. Se actualizó su precio.")
                else:
                    productos_unicos.add(nombre)
                    print(f"✅ Producto '{nombre}' registrado correctamente en el conjunto.")

                precios[nombre] = precio

            except ValueError:
                print("❌ Error: Ingrese un valor numérico válido para el precio.")

        elif opcion == "2":
            print("\n--- INVENTARIO ACTUAL ---")
            if productos_unicos:
                for prod in productos_unicos:
                    print(f"• Producto: {prod:<15} | Precio: ${precios[prod]:.2f}")
            else:
                print("La tienda no tiene productos registrados.")

        elif opcion == "3":
            print("\n--- BUSCAR PRODUCTO ---")
            busqueda = input("Ingrese el producto a buscar: ").strip().capitalize()

            if busqueda in productos_unicos:
                print(f"🔍 Encontrado: {busqueda} | Precio: ${precios[busqueda]:.2f}")
            else:
                print(f"❌ El producto '{busqueda}' no se encuentra en el inventario.")

        elif opcion == "4":
            print("\n--- ELIMINAR PRODUCTO ---")
            eliminar = input("Ingrese el producto a eliminar: ").strip().capitalize()

            if eliminar in productos_unicos:
                productos_unicos.remove(eliminar)
                del precios[eliminar]
                print(f"🗑️ Producto '{eliminar}' eliminado exitosamente.")
            else:
                print(f"❌ No se puede eliminar. El producto '{eliminar}' no existe.")

        elif opcion == "5":
            print("\n¡Gracias por usar el sistema de gestión de tienda! Hasta luego.")
            break

        else:
            print("❌ Opción no válida. Por favor, seleccione un número del 1 al 5.")


if __name__ == "__main__":
    main()