import random

class Cartas:
    """
    Clase para manejar una baraja de cartas española o francesa.

    Atributos:
        tipo (str): Tipo de baraja ('espanola' o 'francesa').
        baraja_original (list): Baraja completa, sin modificaciones.
        baraja (list): Baraja actual, que puede cambiar al robar o barajar.
    """
    def __init__(self, tipo: str = "espanola"):
        self.tipo = tipo.lower()
        self.baraja_original = self._crear_baraja()
        self.baraja = self.baraja_original.copy()

    def _crear_baraja(self):
        """
        Crea la baraja original según el tipo.

        Returns:
            list: Lista de cartas como strings.
        """
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
        """
        Mezcla aleatoriamente las cartas de la baraja actual.
        """
        random.shuffle(self.baraja)

    def robar(self, cantidad: int = 1):
        """
        Roba una o más cartas de la baraja actual.

        Args:
            cantidad (int): Número de cartas a robar.

        Returns:
            list: Lista de cartas robadas.
        """
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0.")
        if cantidad > len(self.baraja):
            raise ValueError("No hay suficientes cartas para robar.")
        cartas_robadas = self.baraja[:cantidad]
        self.baraja = self.baraja[cantidad:]
        return cartas_robadas

    def reiniciar_baraja(self):
        """
        Restaura la baraja actual a su estado original.
        """
        self.baraja = self.baraja_original.copy()
