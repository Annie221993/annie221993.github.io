blog/tarea2_unidad1.md
ANA CRISTINA OSORIO GARCÍA

Tarea 2 - Ejercicios Unidad 1

En esta página presento los ejercicios básicos y avanzados de la Unidad 1, relacionados con Python y la simulación de la librería turtle.
Incluyo los enunciados, soluciones en Python y una breve explicación.



 Ejercicio 1 – Suma de dos números

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
suma = numero1 + numero2
print("La suma es:", suma)



 Ejercicio 2 – Área de un círculo

import math
radio = float(input("Ingrese el radio: "))
area = math.pi * (radio ** 2)
print("El área del círculo es:", area)


 Ejercicio 3 – Cálculo del IMC

peso = float(input("Ingrese su peso (kg): "))
estatura = float(input("Ingrese su estatura (m): "))
imc = peso / (estatura ** 2)
print(f"IMC: {imc:.2f}")



 Ejercicio 4 – Número par o impar

numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")




Ejercicios Avanzados – Simulación de la tortuga




 Ejercicio Avanzado 1 – Simular avance con print()

print("Simulación de tortuga")
pasos = int(input("¿Cuántos pasos quiere avanzar la tortuga? "))
print("→ " * pasos)




 Ejercicio Avanzado 2 – Tortuga descendiendo

print("Tortuga descendiendo")
pasos = int(input("¿Cuántos pasos hacia abajo? "))
for i in range(pasos):
    print("↓")




 Ejercicio Avanzado 3 – Movimiento en forma de L

print("Simulación en forma de L")

horizontal = int(input("¿Cuántos pasos hacia adelante? "))
vertical = int(input("¿Cuántos pasos hacia abajo? "))

print("→ " * horizontal)

for i in range(vertical):
    print("↓")




 Ejercicio Avanzado 4 – Movimientos encapsulados con funciones

def adelante(n):
    print("→ " * n)

def abajo(n):
    for i in range(n):
        print("↓")

# Ejemplo:
adelante(5)
abajo(3)




 Ejercicio Avanzado 5 –
 Simulación de escalones

def adelante(n):
    print("→ " * n)

def abajo(n):
    for i in range(n):
        print("↓")

# Escalones
adelante(5)
abajo(2)

adelante(5)
abajo(2)
