"""Punto de entrada del proyecto La Liga 1995-2025."""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import src.config as config
from src.exercises.ex1 import load_and_eda, plot_home_away_goals
from src.exercises.ex2 import total_matches, plot_matches_team_total
from src.exercises.ex3 import goals_distribution, plot_goals_distribution
from src.exercises.ex4 import FTR, plot_FTR
from src.exercises.ex5 import add_points, fun_total_points, alltime_winner
from src.exercises.ex6 import (fun_total_goals, fun_total_goals_by_team,
                               fun_summary_1996_2025, podium)
from src.exercises.ex7 import graf


def parse_args():
    """Lee los argumentos de la línea de comandos."""
    parser = argparse.ArgumentParser(
        description="Análisis histórico de La Liga española 1995-2025")
    parser.add_argument("-ex", type=int, choices=range(1, 8), metavar="N", default=7,
                        help="ejecuta los ejercicios del 1 al N (por defecto, todos)")
    return parser.parse_args()


def ex1():
    print("[Ej 1] Carga del dataset y EDA")
    data = load_and_eda(config.DATA_PATH)
    plot_home_away_goals(data)
    return data


def ex2(data):
    print("[Ej 2] Partidos totales por equipo")
    matches_team_total = total_matches(data)
    print(matches_team_total.head(10))

    max_matches = matches_team_total["total_matches"].max()
    siempre = matches_team_total[matches_team_total["total_matches"] == max_matches]
    print(f"\nEquipos siempre en primera ({max_matches} partidos):")
    print(siempre)

    plot_matches_team_total(matches_team_total)


def ex3(data):
    print("[Ej 3] Distribución de goles")
    distr_home, distr_away = goals_distribution(data)
    print(distr_home)
    print(distr_away)
    plot_goals_distribution(distr_home, distr_away)


def ex4(data):
    print("[Ej 4] Resultados en casa / fuera")
    ftr = FTR(data)
    print(ftr)
    pct_home = ftr.loc["H", "matches"] / ftr["matches"].sum() * 100
    print(f"\nLos locales ganan el {pct_home:.1f}% de los partidos")
    plot_FTR(ftr)


def ex5(data):
    print("[Ej 5] Clasificación acumulada 1995-2025")
    data = add_points(data)
    print(data.head(10))
    total_points, df_total_points = fun_total_points(data)
    print(df_total_points.head(10))
    print(f"\nGanador histórico: {alltime_winner(df_total_points)}")
    return data, total_points


def ex6(data, total_points):
    print("[Ej 6] Resumen y podio")
    home_goals, away_goals, total_goals = fun_total_goals(data)
    print(
        f"Goles locales: {home_goals} | visitantes: {away_goals} | total: {total_goals}")

    home_by_team, away_by_team, total_by_team = fun_total_goals_by_team(data)
    print(total_by_team.head(10))

    summary = fun_summary_1996_2025(
        total_points, home_by_team, away_by_team, total_by_team)
    print(summary.head())
    podium(summary)
    return summary


def ex7(data, summary):
    print("[Ej 7] Grafo de enfrentamientos")
    top5 = list(summary.head(5).index)
    print(f"Top 5: {top5}")
    graf(data, top5)


def main():
    """Ejecuta los ejercicios hasta el indicado por -ex."""
    n = parse_args().ex
    os.makedirs(config.IMG_PATH, exist_ok=True)

    data = ex1()
    if n >= 2:
        ex2(data)
    if n >= 3:
        ex3(data)
    if n >= 4:
        ex4(data)

    # A partir del ejercicio 5 necesitamos los puntos acumulados
    total_points = None
    if n >= 5:
        data, total_points = ex5(data)

    summary = None
    if n >= 6:
        summary = ex6(data, total_points)

    if n >= 7:
        ex7(data, summary)

    print("\nHecho.")


if __name__ == "__main__":
    main()
