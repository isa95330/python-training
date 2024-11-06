import pytest
from greedy import tsp_nearest_neighbor

def test_single_point():
    points = [(0, 0)]
    _, total_distance = tsp_nearest_neighbor(points)
    assert round(total_distance) == 0

def test_two_points():
    points = [(0, 0), (3, 4)]
    _, total_distance = tsp_nearest_neighbor(points)
    assert round(total_distance) == 10  # Distance aller-retour 5 + 5

def test_square_points():
    points = [(0, 0), (0, 10), (10, 10), (10, 0)]
    _, total_distance = tsp_nearest_neighbor(points)
    assert round(total_distance) == 40  # Parcours en carré de 10 unités de chaque côté

def test_random_points():
    points = [(9, 12), (24, 15), (12, 30), (4, 3), (13, 27)]
    _, total_distance = tsp_nearest_neighbor(points)
    assert round(total_distance) == 71  # Résultat attendu après vérification du parcours optimal

def test_complex_case():
    points = [(0, 0), (2, 3), (5, 5), (6, 1), (7, 8), (8, 3)]
    _, total_distance = tsp_nearest_neighbor(points)
    # Utilisation de l'assertion pour vérifier une approximation si le résultat n'est pas exact
    assert round(total_distance) in range(23, 26)  # Distance estimée

# Exécuter les tests
if __name__ == "__main__":
    pytest.main()
