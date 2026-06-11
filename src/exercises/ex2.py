"""Ejercicio 2: partidos totales jugados por cada equipo"""

import pandas as pd
import matplotlib.pyplot as plt

import src.config as config


def total_matches(data: pd.DataFrame) -> pd.DataFrame:
    """Suma partidos como local y visitante para cada equipo.

    Devuelve un dataframe ordenado de más a menos partidos
    """
    home = data["H"].value_counts()
    away = data["A"].value_counts()
    total = home.add(away, fill_value=0).astype(int)

    matches_team_total = pd.DataFrame({"total_matches": total})
    return matches_team_total.sort_values("total_matches", ascending=False)


def plot_matches_team_total(matches_team_total: pd.DataFrame) -> None:
    """Diagrama de barras con el total de partidos por equipo"""
    _, ax = plt.subplots(figsize=(16, 6))
    ax.bar(matches_team_total.index, matches_team_total["total_matches"],
           color="steelblue")
    ax.set_title("Partidos totales jugados por equipo (1995-2025)")
    ax.set_xlabel("Equipo")
    ax.set_ylabel("Partidos")
    plt.xticks(rotation=90, fontsize=8)
    plt.tight_layout()
    plt.savefig(
        f"{config.IMG_PATH}grafica_ex2_{config.nom_alumne}_{config.date_time}.png")
    plt.close()
