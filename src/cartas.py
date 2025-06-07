import random

class Cartas:
    def __init__(self, tipo: str = "espanola"):
        self.tipo = tipo.lower()
        self.baraja_original = self._crear_baraja()
        self.baraja = self.baraja_original.copy()

    def _crear_baraja(self):
        if self.tipo == "espanola":
            palos = ['oros', 'copas', 'espadas', 'bastos']
            numeros = [i for i in range(1, 13) if i not in (8, 9)]
            return [f"{numero} de {palo}" for palo in palos for numero in numeros]
        elif self.tipo == "francesa":
            palos = ['PICAS', 'CORAZONES', 'DIAMANTES', 'TREBOLES']
            numeros = ['A'] + list(map(str, range(2, 11))) + ['J', 'Q', 'K']
            return [f"{numero}-{palo}" for palo in palos for numero in numeros]
        else:
            raise ValueError("Tipo de baraja no reconocido. Usa 'espanola' o 'francesa'.")

    def barajar(self):
        random.shuffle(self.baraja)

    def robar(self, cantidad: int = 1):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0.")
        if cantidad > len(self.baraja):
            raise ValueError("No hay suficientes cartas para robar.")
        cartas_robadas = self.baraja[:cantidad]
        self.baraja = self.baraja[cantidad:]
        return cartas_robadas

    def reiniciar_baraja(self):
        self.baraja = self.baraja_original.copy()
