import numpy as np

class Dados():
    def __init__(self, caras):
        if not isinstance(caras, int) or caras <= 0:
            raise ValueError("El número de caras debe ser un entero positivo.")
        self.caras = caras
        
    def lanzar_dado(self, veces: int = 1):
        if not isinstance(veces, int) or veces <= 0:
            raise ValueError("El número de lanzamientos debe ser un entero positivo.")
        
        resultados = np.random.randint(1, self.caras + 1, size=veces)
        return resultados.tolist()
