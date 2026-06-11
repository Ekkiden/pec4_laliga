"""Ejercicio 4: partidos ganados en casa, fuera y empatados."""

import pandas as pd
import matplotlib.pyplot as plt

import src.config as config


# pylint: disable=invalid-name
def FTR(data: pd.DataFrame) -> pd.DataFrame:
    """Cuenta los resultados finales: H (local), A (visitante) y D (empate)"""
    ftr = data["FTR"].value_counts().reindex(["H", "A", "D"])
    return ftr.rename_axis("result").reset_index(name="matches").set_index("result")


def plot_FTR(ftr: pd.DataFrame) -> None:
    """Diagrama de barras con el número de partidos según el resultado."""
    colors = ["steelblue", "salmon", "lightgreen"]

    _, ax = plt.subplots(figsize=(6, 5))
    ax.bar(ftr.index, ftr["matches"], color=colors, width=0.5)
    ax.set_title("Resultados en La Liga (1995-2025)")
    ax.set_xlabel("H = local, A = visitante, D = empate")
    ax.set_ylabel("Partidos")
    plt.tight_layout()
    plt.savefig(
        f"{config.IMG_PATH}grafica_ex4_{config.nom_alumne}_{config.date_time}.png")
    plt.close()
