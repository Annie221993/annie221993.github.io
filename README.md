Tarea Mini-Turtle

Este proyecto corresponde a la Tarea Mini-Turtle, cuyo objetivo es aplicar modularidad y programación orientada a objetos (POO) en Python mediante la creación de dos paquetes independientes.

📌 Ejercicio 1: Versión Funcional (Modularidad)
🎯 Objetivo

Transformar las funciones sueltas adelante() y abajo() en un paquete Python distribuible llamado mini_turtle, demostrando la separación entre:

Lógica interna

Interfaz pública

⚙ Requerimientos cumplidos

Interfaz limpia:

from mini_turtle import adelante, abajo, reiniciar

Nueva función reiniciar() que restablece posicion_x a 0

Uso de variable global solo en la versión funcional

📦 Estructura del proyecto
mini_turtle/
│
├── mini_turtle/
│   ├── _init_.py
│   └── drawer_logic.py
│
└── main.py
🧠 Lógica (drawer_logic.py)
posicion_x = 0


def adelante(pasos):
    global posicion_x
    posicion_x += pasos
    print(f"Avanza {pasos} pasos → x = {posicion_x}")


def abajo():
    print("Lápiz abajo")


def reiniciar():
    global posicion_x
    posicion_x = 0
    print("Posición reiniciada a 0")
🧪 Prueba (main.py)
from mini_turtle import adelante, abajo, reiniciar


print("Dibujando escalera")
abajo()
adelante(2)
adelante(2)
adelante(2)


reiniciar()


print("\nDibujando algo nuevo")
adelante(5)
adelante(3)


## Ejercicio 1 – Versión Funcional
Repositorio:
https://github.com/Annie221993/mini_turtle

## Ejercicio 2 – Versión Orientada a Objetos (POO)
Repositorio:

https://github.com/Annie221993/annie221993.github.io/tree/2ebdb9a82ef30bff23529e542d12c7e11f51832a/blog
