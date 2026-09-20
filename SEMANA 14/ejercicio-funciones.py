def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

print("--- SISTEMA DE CÁLCULO DE PROMEDIO DE NOTAS ---")

n1 = float(input("Ingrese la primera nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))

resultado_promedio = calcular_promedio(n1, n2, n3)

print(f"\nEl8"
      f" promedio final del estudiante es: {resultado_promedio:.2f}")