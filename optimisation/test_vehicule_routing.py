import pytest
from vehicule_routing import create_routes, build_distance_matrix


def test_create_routes_single_route():
    clients = [(1, 2, 3, 4), (2, 5, 1, 3)]  # (index, x, y, demand)
    capacity = 10
    routes = create_routes(clients, capacity)
    assert routes == [[1, 2]]  # Tous les clients tiennent dans un seul véhicule


def test_create_routes_multiple_routes():
    clients = [
        (1, 2, 3, 4),
        (2, 5, 1, 3),
        (3, -2, -2, 7),
        (4, -3, 4, 6),
        (5, 0, -4, 5)
    ]
    capacity = 10
    routes = create_routes(clients, capacity)
    # Vérifie si les routes sont bien calculées pour ne pas dépasser la capacité
    assert all(sum(clients[i - 1][3] for i in route) <= capacity for route in routes)


def test_build_distance_matrix():
    depot = (0, 0)
    clients = [(1, 2, 3, 0), (2, 5, 1, 0)]
    distance_matrix = build_distance_matrix(depot, clients)
    assert distance_matrix[0][1] == 4  # Distance du dépôt au client 1
    assert distance_matrix[1][2] == 4  # Distance entre client 1 et client 2
    assert distance_matrix[2][0] == 5  # Distance du client 2 au dépôt


def test_create_routes_exact_capacity():
    clients = [(1, 2, 3, 5), (2, 5, 1, 5)]
    capacity = 5
    routes = create_routes(clients, capacity)
    assert routes == [[1], [2]]  # Chaque client a une demande égale à la capacité


def test_create_routes_no_clients():
    clients = []
    capacity = 10
    routes = create_routes(clients, capacity)
    assert routes == []  # Pas de clients, pas de routes


if __name__ == "__main__":
    pytest.main()
