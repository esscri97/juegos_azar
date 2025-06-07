# test/test_dados.py

import pytest
from src.dados import Dados

def test_crear_dado_valido():
    dado = Dados(6)
    assert dado.caras == 6

def test_crear_dado_caras_negativas():
    with pytest.raises(ValueError):
        Dados(-4)

def test_crear_dado_caras_no_entero():
    with pytest.raises(ValueError):
        Dados("seis")


def test_lanzar_dado_varias_veces():
    dado = Dados(10)
    resultado = dado.lanzar_dado(5)
    assert len(resultado) == 5

def test_lanzar_dado_con_veces_negativas():
    dado = Dados(6)
    with pytest.raises(ValueError):
        dado.lanzar_dado(-3)

def test_lanzar_dado_con_veces_no_entero():
    dado = Dados(6)
    with pytest.raises(ValueError):
        dado.lanzar_dado("tres")
