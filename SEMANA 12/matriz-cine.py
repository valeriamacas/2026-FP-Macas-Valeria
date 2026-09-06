# Programa para gestionar la reserva de asientos de una sala de cine
# La sala tiene 3 filas y 4 columnas.
# 0 = asiento libre
# 1 = asiento reservado

# Crear la matriz de asientos: 3 filas x 4 columnas, todos en 0
asientos = [[0 for columna in range(4)] for fila in range(3)]

# Pedir al usuario la fila y la columna del asiento que desea reservar
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

# Marcar el asiento seleccionado como reservado
asientos[fila][columna] = 1

# Mostrar el estado actual de la sala
print("\nEstado de la sala:")

# Recorrer la matriz utilizando dos bucles anidados
for fila in range(3):
    for columna in range(4):
        print(asientos[fila][columna], end=" ")
    print()  # Salto de línea al terminar cada fila

