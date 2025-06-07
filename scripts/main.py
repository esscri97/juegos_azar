from src.dados import Dados

if __name__ == '__main__':
    dado = Dados(6)
    print(f'Lanzar dado 3 veces: {dado.lanzar_dado(3)}')