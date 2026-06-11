# Análisis de La Liga 1995-2025

PEC4 de Programación para la ciencia de datos (22.503), Grado en Ciencia de Datos Aplicada de la UOC.

Autor: Nikolay Mihailov Yosifov

## De qué va

Es un análisis de los resultados de la Liga española desde la temporada 1995-96 hasta 2025-26, usando el dataset de Kaggle (kishan305/la-liga-results-19952020). Se hacen 7 análisis, cada uno en su propio módulo dentro de `src/exercises`:

- ex1: cargar el dataset y un EDA básico (info, describe, boxplots de goles)
- ex2: partidos totales que ha jugado cada equipo
- ex3: distribución de goles por partido
- ex4: cuántos partidos gana el local, el visitante o acaban en empate
- ex5: clasificación acumulada de todos estos años y ganador histórico
- ex6: resumen de puntos y goles + gráfica del podio
- ex7: grafo con los enfrentamientos entre el top 5 (con networkx)

El ex5 no genera gráfica, solo saca por pantalla la clasificación. El resto sí guardan una imagen en `src/img`.

## Estructura

```
laliga_project/
├── src/
│   ├── config.py        # nombre del alumno, fecha y rutas
│   ├── main.py          # se ejecuta esto
│   ├── exercises/       # ex1 ... ex7
│   ├── data/            # aquí va el laliga.csv
│   └── img/             # las gráficas salen aquí
├── tests/
│   └── tests_ex6.py     # tests del ejercicio 6
├── doc/                 # documentación de pydoc
├── screenshots/         # capturas
├── requirements.txt
├── LICENSE
└── README.md
```

## Montar el entorno

Yo lo he hecho en Windows. Desde la carpeta del proyecto:

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

En Linux o Mac el activate es `source .venv/bin/activate`.

El dataset hay que bajarlo de Kaggle y dejarlo en `src/data/laliga.csv`. El link es este:
https://www.kaggle.com/datasets/kishan305/la-liga-results-19952020

## Cómo se ejecuta

Importante: ejecutarlo como módulo con `-m`, así no hay problemas con las rutas de los imports.

```
python -m src.main -ex 7
```

El `-ex` es hasta qué ejercicio quieres llegar. Por ejemplo `-ex 5` ejecuta del 1 al 5. Si no pones nada hace todos. Y `python -m src.main -h` enseña la ayuda.

Las gráficas se guardan solas en `src/img` con el nombre `grafica_exN_NombreAlumno_fecha.png`.

## Linting

Pylint no viene en el requirements, hay que instalarlo aparte:

```
pip install pylint
pylint src
```

No da un 10 perfecto pero el enunciado dice que no hace falta.

## Documentación

Se genera con pydoc. Un comando por módulo (desde la carpeta del proyecto):

```
python -m pydoc -w src.config
python -m pydoc -w src.main
python -m pydoc -w src.exercises.ex1
python -m pydoc -w src.exercises.ex2
python -m pydoc -w src.exercises.ex3
python -m pydoc -w src.exercises.ex4
python -m pydoc -w src.exercises.ex5
python -m pydoc -w src.exercises.ex6
python -m pydoc -w src.exercises.ex7
```

Eso crea los .html en la carpeta, y luego los muevo a doc con `move *.html doc\`.

## Tests

```
pip install pytest
python -m pytest tests/tests_ex6.py -v
```

Son 7 tests sobre la función fun_total_goals del ejercicio 6.

## Notas

- Acuérdate de cambiar el nombre en config.py si reutilizas esto.
- No subir la carpeta .venv en el zip, que pesa un montón.
