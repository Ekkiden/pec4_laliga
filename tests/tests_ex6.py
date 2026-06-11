"""Tests de la función fun_total_goals (ejercicio 6)."""

import os
import sys
import unittest

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.exercises.ex6 import fun_total_goals


class TestFunTotalGoals(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({"FTHG": [1, 2, 3], "FTAG": [0, 1, 2]})
        self.ceros = pd.DataFrame({"FTHG": [0, 0, 0], "FTAG": [0, 0, 0]})
        self.vacio = pd.DataFrame({"FTHG": [], "FTAG": []})

    def test_devuelve_tupla_de_tres(self):
        result = fun_total_goals(self.data)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)

    def test_goles_locales(self):
        home, _, _ = fun_total_goals(self.data)
        self.assertEqual(home, 6)

    def test_goles_visitantes(self):
        _, away, _ = fun_total_goals(self.data)
        self.assertEqual(away, 3)

    def test_total_es_la_suma(self):
        home, away, total = fun_total_goals(self.data)
        self.assertEqual(total, home + away)
        self.assertEqual(total, 9)

    def test_todo_ceros(self):
        self.assertEqual(fun_total_goals(self.ceros), (0, 0, 0))

    def test_dataframe_vacio(self):
        self.assertEqual(fun_total_goals(self.vacio), (0, 0, 0))

    def test_son_enteros(self):
        for valor in fun_total_goals(self.data):
            self.assertIsInstance(valor, int)


if __name__ == "__main__":
    unittest.main()
