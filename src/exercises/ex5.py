"""Ejercicio 5: clasificación acumulada y ganador histórico"""

import pandas as pd


def add_points(data: pd.DataFrame) -> pd.DataFrame:
    """Añade points_home y points_away a partir del resultado (3/1/0)"""
    data = data.copy()
    data["points_home"] = data["FTR"].map({"H": 3, "D": 1, "A": 0})
    data["points_away"] = data["FTR"].map({"A": 3, "D": 1, "H": 0})
    return data


def fun_total_points(data: pd.DataFrame):
    """Puntos acumulados por equipo desde 1995

    Devuelve la misma información como Series y como DataFrame.
    """
    home_pts = data.groupby("H")["points_home"].sum()
    away_pts = data.groupby("A")["points_away"].sum()
    total = home_pts.add(away_pts, fill_value=0).astype(
        int).sort_values(ascending=False)

    total_points_by_team = total.rename("total_points")
    df_total_points_by_team = total_points_by_team.to_frame()
    df_total_points_by_team.index.name = "team"

    return total_points_by_team, df_total_points_by_team


def alltime_winner(df_total_points: pd.DataFrame) -> str:
    """Equipo con más puntos acumulados"""
    return df_total_points["total_points"].idxmax()
