"""Ejercicio 1: carga del dataset y análisis exploratorio."""

import pandas as pd
import matplotlib.pyplot as plt

import src.config as config


def load_and_eda(file: str) -> pd.DataFrame:
    """Carga el CSV, elimina las columnas de medio tiempo y muestra una EDA básico"""
    data = pd.read_csv(file)
    data = data.rename(columns={"HomeTeam": "H", "AwayTeam": "A"})
    data = data.drop(columns=["HTHG", "HTAG", "HTR"])

    print(data.head())
    print(data.tail())
    print(data.info())
    print(data.describe())

    return data


def plot_home_away_goals(data: pd.DataFrame) -> None:
    """Boxplots de goles locales (FTHG) y visitantes (FTAG) en una misma figura"""
    fig, axes = plt.subplots(1, 2, figsize=(10, 6))

    axes[0].boxplot(data["FTHG"].dropna(), patch_artist=True,
                    boxprops={"facecolor": "steelblue"})
    axes[0].set_title("Goles equipo local")
    axes[0].set_ylabel("Goles")

    axes[1].boxplot(data["FTAG"].dropna(), patch_artist=True,
                    boxprops={"facecolor": "salmon"})
    axes[1].set_title("Goles equipo visitante")
    axes[1].set_ylabel("Goles")

    fig.suptitle("Distribución de goles: local vs visitante")
    plt.tight_layout()
    plt.savefig(
        f"{config.IMG_PATH}grafica_ex1_{config.nom_alumne}_{config.date_time}.png")
    plt.close()
