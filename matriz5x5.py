# Crear una matriz de 5 filas por 5 columnas
matriz = [[0 for _ in range(5)] for _ in range(5)]

# Ingresar los 25 valores
for i in range(5):
    for j in range(5):
        valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
        matriz[i][j] = valor

# Mostrar la matriz ingresada
print("\nMatriz ingresada:")

for i in range(5):
    for j in range(5):
        print(matriz[i][j], end="\t")
    print()
