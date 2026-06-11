"""Ejercicio 6: resumen estadístico 1995-2025 y podio"""

import pandas as pd
import matplotlib.pyplot as plt

import src.config as config


def fun_total_goals(data: pd.DataFrame):
    """Goles locales, visitantes y totales del dataset"""
    home_goals = int(data["FTHG"].sum())
    away_goals = int(data["FTAG"].sum())
    return home_goals, away_goals, home_goals + away_goals


def fun_total_goals_by_team(data: pd.DataFrame):
    """Goles por equipo: como local, como visitante y totales"""
    home_goals_by_team = data.groupby(
        "H")["FTHG"].sum().rename("home_goals").to_frame()
    away_goals_by_team = data.groupby(
        "A")["FTAG"].sum().rename("away_goals").to_frame()

    total = (home_goals_by_team["home_goals"]
             .add(away_goals_by_team["away_goals"], fill_value=0)
             .astype(int)
             .sort_values(ascending=False))
    total_goals_by_team = total.rename("total_goals").to_frame()

    return home_goals_by_team, away_goals_by_team, total_goals_by_team


def fun_summary_1996_2025(total_points_by_team, home_goals_by_team,
                          away_goals_by_team, total_goals_by_team) -> pd.DataFrame:
    """Concatena puntos y goles por equipo en un único dataframe resumen."""
    if isinstance(total_points_by_team, pd.Series):
        total_points_by_team = total_points_by_team.to_frame(
            name="total_points")

    summary = pd.concat([total_points_by_team, home_goals_by_team,
                         away_goals_by_team, total_goals_by_team], axis=1)
    return summary.sort_values("total_points", ascending=False)


def podium(summary_1996_2025: pd.DataFrame) -> None:
    """Gráfica de podio con los tres primeros equipos del ranking

    El campeón va al centro y más alto, el segundo a la izquierda y
    el tercero a la derecha, ambos más bajos
    """
    top3 = summary_1996_2025.head(3)
    teams = list(top3.index)
    points = list(top3["total_points"])

    # Reordenamos a 2º - 1º - 3º para dar forma de podio
    order = [1, 0, 2]
    teams = [teams[i] for i in order]
    points = [points[i] for i in order]
    colors = ["silver", "gold", "#cd7f32"]
    labels = ["2º", "1º", "3º"]

    _, ax = plt.subplots(figsize=(7, 5))
    bars = ax.bar(range(3), points, color=colors, width=0.5)

    for rect, team, label in zip(bars, teams, labels):
        ax.text(rect.get_x() + rect.get_width() / 2,
                rect.get_height() + max(points) * 0.01,
                f"{label}\n{team}", ha="center", va="bottom", fontweight="bold")

    ax.set_title("Podio histórico La Liga 1995-2025")
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(
        f"{config.IMG_PATH}grafica_ex6_{config.nom_alumne}_{config.date_time}.png")
    plt.close()
