# calculo_total.py
# Tarea práctica: Definición y uso de funciones en Python
# Problema: Calcular el total de una compra en una tienda

def calcular_total(precio, cantidad):
    """
    Calcula el total de una compra multiplicando el precio
    del producto por la cantidad que lleva el cliente.

    Parámetros:
        precio (float): Precio unitario del producto.
        cantidad (int): Cantidad de unidades que lleva el cliente.

    Retorna:
        float: El total a pagar por la compra.
    """
    total = precio * cantidad
    return total


if __name__ == "__main__":
    # Datos de ejemplo
    precio = 10
    cantidad = 3

    # Llamada a la función
    resultado = calcular_total(precio, cantidad)

    # Mostrar el resultado en consola
    print(f"Total de la compra: ${resultado}")

