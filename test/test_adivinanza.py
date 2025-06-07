import pytest
import random
from unittest.mock import patch
from src.adivinanza import Adivinanza

def test_rango_personalizado():
    juego = Adivinanza(minimo=10, maximo=50)
    assert juego.minimo == 10
    assert juego.maximo == 50
    assert 10 <= juego.numero_secreto <= 50

def test_rango_fallido():
    with pytest.raises(ValueError):
        juego = Adivinanza(20, 10)

def test_intento_numero_en_letra(capsys):
    juego = Adivinanza(minimo=1, maximo=10)

    inputs = ["cinco", str(juego.numero_secreto)]

    with patch("builtins.input", side_effect=inputs):
        juego.jugar()

    salida = capsys.readouterr().out

    assert "Elección no válida" in salida
    assert "¡Correcto!" in salida
