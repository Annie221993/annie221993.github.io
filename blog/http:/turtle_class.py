class Tortuga:
    def _init_(self):
        # Estado interno del objeto
        self.posicion_x = 0

    def adelante(self, pasos):
        self.posicion_x += pasos
        print(f"Tortuga avanza {pasos} pasos. Posición: {self.posicion_x}")

    def abajo(self):
        print("Tortuga baja el lápiz")

    def reiniciar(self):
        self.posicion_x = 0
        print("Posición reiniciada a 0")
