"""Ejercicio 7: grafo de enfrentamientos entre los 5 mejores equipos"""

from collections import Counter

import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

import src.config as config


def graf(data: pd.DataFrame, selected_teams: list) -> None:
    """Dibuja un grafo con los enfrentamientos entre los equipos seleccionados

    Solo se tienen en cuenta los partidos en los que ambos equipos están en
    selected_teams. Cada arista muestra cuántas veces se han enfrentado
    (suma de partidos como local y como visitante).
    """
    mask = data["H"].isin(selected_teams) & data["A"].isin(selected_teams)
    filtered = data[mask]

    # Agrupamos los dos sentidos del enfrentamiento en una sola arista
    counts = Counter(tuple(sorted(pair)) for pair in zip(filtered["H"], filtered["A"]))

    graph = nx.Graph()
    graph.add_nodes_from(selected_teams)
    for (team_a, team_b), n in counts.items():
        graph.add_edge(team_a, team_b, weight=n)

    fig, ax = plt.subplots(figsize=(8, 6))
    pos = nx.circular_layout(graph)

    nx.draw_networkx_nodes(graph, pos, ax=ax, node_size=2000, node_color="steelblue")
    nx.draw_networkx_labels(graph, pos, ax=ax, font_size=9,
                            font_color="white", font_weight="bold")
    nx.draw_networkx_edges(graph, pos, ax=ax, width=2, edge_color="gray")
    nx.draw_networkx_edge_labels(
        graph, pos, ax=ax,
        edge_labels={(u, v): d["weight"] for u, v, d in graph.edges(data=True)})

    ax.set_title("Enfrentamientos entre el top 5 histórico")
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(f"{config.IMG_PATH}grafica_ex7_{config.nom_alumne}_{config.date_time}.png")
    plt.close()
