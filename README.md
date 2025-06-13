# juegos_azar

Una librería con juegos de azar escritos en Python.

## Descripción

Este proyecto contiene varios juegos simples de azar para practicar Python y divertirse. Actualmente incluye:

-   Juego de adivinanzas (números para adivinar)
-   Juego de dados (lanzar un dado con las caras y veces determinadas)
-   Juego de cartas (simulación básica)

## Instalación

1.  Clona el repositorio:

    ```bash
    git clone [https://github.com/esscri97/juegos_azar.git](https://github.com/esscri97/juegos_azar.git)
    cd juegos_azar
    ```

2.  (Opcional, pero recomendado) Crea y activa un entorno virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    # O para Windows:
    # venv\Scripts\activate
    ```

3.  Instala las dependencias con pip (incluye `numpy` para el juego de dados):

    ```bash
    pip install -r requirements.txt
    ```

### Instalación editable para desarrollo o uso directo en tu proyecto

Si quieres usar la librería directamente desde tu repositorio local y que los cambios que hagas se reflejen automáticamente (por ejemplo, si estás desarrollando o probando), puedes instalarla en modo editable con:

(*Debes tener la librería en el mismo directorio que está tu proyecto*)

```bash
cd ../juegos_azar
pip install -e .
```
Esto instalará la librería desde la carpeta actual (.) y permitirá que las modificaciones que hagas en el código fuente se reflejen inmediatamente sin necesidad de reinstalar.

## Uso

Ejemplos básicos para cada juego:

### Adivinanzas

```python
from juegos_azar.adivinanza import Adivinanza

juego = Adivinanza(minimo=1, maximo=50)
juego.jugar()
```
### Dados 

```python
from juegos_azar.dados import lanzar_dado

dado = Dados(6)
print(f'Lanzar dado 3 veces: {dado.lanzar_dado(3)}')
```

### Cartas

```python
from juegos_azar.cartas import repartir_cartas

baraja_espanola = Cartas('espanola')
print(baraja_espanola.baraja)
print('Barajando...')
baraja_espanola.barajar()
print('Robando...')
baraja_espanola.robar(14)
print(baraja_espanola.baraja)
```

## Tests

Para ejecutar los tests usa
```bash
pytest
```

## Contribuciones
¡Las contribuciones son bienvenidas! Abre un issue o pull request para sugerir mejoras o añadir nuevos juegos.

Desarrollado por David Escrivá