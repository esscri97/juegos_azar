from src.dados import Dados
from src.cartas import Cartas
from src.adivinanza import Adivinanza

if __name__ == '__main__':
    print('JUGANDO A LOS DADOS:')
    
    dado = Dados(6)
    print(f'Lanzar dado 3 veces: {dado.lanzar_dado(3)}')
    
    print('########################################')
    print('JUGANDO A LAS CARTAS:')
    
    baraja_espanola = Cartas('espanola')
    print(baraja_espanola.baraja)
    print('Barajando...')
    baraja_espanola.barajar()
    print('Robando...')
    baraja_espanola.robar(14)
    print(baraja_espanola.baraja)

    print('########################################')
    print('JUGANDO A LA ADIVINANZA:')
    
    adivinanza = Adivinanza(0, 100)
    adivinanza.jugar()