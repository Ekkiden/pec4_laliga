"""Ejercicio 3: distribución del número de goles por partido"""

import pandas as pd
import matplotlib.pyplot as plt

import src.config as config


def _distribution(serie: pd.Series) -> pd.DataFrame:
    """Cuenta en cuántos partidos se marcó cada número de goles"""
    return (serie.value_counts()
            .sort_index()
            .rename_axis("goals")
            .reset_index(name="matches")
            .set_index("goals"))


def goals_distribution(data: pd.DataFrame):
    """Distribución de goles locales y visitantes (FTHG, FTAG)"""
    distr_goals_home = _distribution(data["FTHG"])
    distr_goals_away = _distribution(data["FTAG"])
    return distr_goals_home, distr_goals_away


def plot_goals_distribution(distr_goals_home: pd.DataFrame,
                            distr_goals_away: pd.DataFrame) -> None:
    """Dos diagramas de barras con la distribución de goles local/visitante"""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].bar(distr_goals_home.index, distr_goals_home["matches"], color="steelblue")
    axes[0].set_title("Goles locales (FTHG)")
    axes[0].set_xlabel("Goles")
    axes[0].set_ylabel("Partidos")

    axes[1].bar(distr_goals_away.index, distr_goals_away["matches"], color="salmon")
    axes[1].set_title("Goles visitantes (FTAG)")
    axes[1].set_xlabel("Goles")
    axes[1].set_ylabel("Partidos")

    fig.suptitle("Distribución de goles por partido")
    plt.tight_layout()
    plt.savefig(f"{config.IMG_PATH}grafica_ex3_{config.nom_alumne}_{config.date_time}.png")
    plt.close()
