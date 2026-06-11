"""Configuración global: nombre del alumno, timestamp y rutas del proyecto."""

from datetime import datetime

nom_alumne = "Nikolay Mihailov Yosifov"
date_time = datetime.now().strftime('%Y%m%d_%H%M%S')

DATA_PATH = "src/data/laliga.csv"
IMG_PATH = "src/img/"
