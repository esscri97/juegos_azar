import random

class Adivinanza:
    def __init__(self, minimo: int = 1, maximo: int = 100):
        if minimo > maximo:
            raise ValueError(f"El valor mínimo ({minimo}) no puede ser mayor que el máximo ({maximo}).")
        self.minimo = minimo
        self.maximo = maximo
        self.intentos = 6
        self.numero_secreto = random.randint(self.minimo, self.maximo)

    def jugar(self):
        print(f"Adivina el número entre {self.minimo} y {self.maximo}")

        while self.intentos > 0:
            try:
                intento = int(input("Introduce tu número: "))
                
                if intento < self.minimo or intento > self.maximo:
                    print(f"Por favor, elige un número entre {self.minimo} y {self.maximo}")
                    continue

                if intento < self.numero_secreto:
                    print("¡Te has quedado corto! Prueba uno más alto.")
                elif intento > self.numero_secreto:
                    print("¡Te has pasado! Prueba uno más bajo.")
                else:
                    print("¡Correcto! Has adivinado el número.")
                    break
                
                self.intentos -= 1
                if self.intentos <= 2 and self.intentos > 0:
                    print(f"¡Afina la puntería! sólo te quedan {self.intentos} intento(s)")
                elif self.intentos == 0:
                    print("¡Vaya! has perdido. \nSuerte la próxima vez")
                
            except ValueError:
                print("Elección no válida. Por favor, introduce un número entero.")
