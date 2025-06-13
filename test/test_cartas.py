import pytest
from src.juegos_azar.cartas import Cartas

def test_crear_baraja_valido():
    baraja_poker = Cartas('francesa')
    assert baraja_poker.baraja == [
        'A-PICAS', '2-PICAS', '3-PICAS', '4-PICAS', '5-PICAS', '6-PICAS',
        '7-PICAS', '8-PICAS', '9-PICAS', '10-PICAS', 'J-PICAS', 'Q-PICAS', 'K-PICAS',
        'A-CORAZONES', '2-CORAZONES', '3-CORAZONES', '4-CORAZONES', '5-CORAZONES', '6-CORAZONES',
        '7-CORAZONES', '8-CORAZONES', '9-CORAZONES', '10-CORAZONES', 'J-CORAZONES', 'Q-CORAZONES', 'K-CORAZONES',
        'A-DIAMANTES', '2-DIAMANTES', '3-DIAMANTES', '4-DIAMANTES', '5-DIAMANTES', '6-DIAMANTES',
        '7-DIAMANTES', '8-DIAMANTES', '9-DIAMANTES', '10-DIAMANTES', 'J-DIAMANTES', 'Q-DIAMANTES', 'K-DIAMANTES',
        'A-TREBOLES', '2-TREBOLES', '3-TREBOLES', '4-TREBOLES', '5-TREBOLES', '6-TREBOLES',
        '7-TREBOLES', '8-TREBOLES', '9-TREBOLES', '10-TREBOLES', 'J-TREBOLES', 'Q-TREBOLES', 'K-TREBOLES'
    ]
    
def test_baraja_erronea():
    with pytest.raises(ValueError):
        baraja = Cartas('americana')
        
def test_robar_negativo():
    with pytest.raises(ValueError):
        baraja = Cartas('francesa')
        baraja.robar(-3)
        
def test_robar_demasiadas():
    with pytest.raises(ValueError):
        baraja = Cartas('francesa')
        baraja.robar(60)
        
def test_barajar_cambia_orden():
    baraja = Cartas('francesa')
    original = baraja.baraja.copy()
    baraja.barajar()
    barajada = baraja.baraja
    assert set(original) == set(barajada)
    assert original != barajada

def test_reiniciar_baraja():
    baraja = Cartas('francesa')
    baraja.barajar()
    baraja.reiniciar_baraja()
    assert baraja.baraja == baraja.baraja_original