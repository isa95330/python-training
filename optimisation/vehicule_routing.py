import math

def euclidean_distance(x1, y1, x2, y2):
    """
    Calcule la distance euclidienne entre deux points (x1, y1) et (x2, y2).

    Parameters:
    - x1 (int or float): Coordonnée x du premier point.
    - y1 (int or float): Coordonnée y du premier point.
    - x2 (int or float): Coordonnée x du second point.
    - y2 (int or float): Coordonnée y du second point.

    Returns:
    - int: La distance euclidienne arrondie entre les deux points.

    Description:
    Cette fonction applique la formule mathématique pour calculer la
    distance entre deux points dans un plan 2D. La distance est arrondie
    à l'entier le plus proche pour simplifier les calculs de distance.
    """
    return round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))


def build_distance_matrix(depot, clients):
    """
    Construit une matrice de distances entre le dépôt et les clients.

    Parameters:
    - depot (tuple): Coordonnées du dépôt sous la forme (x, y).
    - clients (list of tuples): Liste de clients, chaque client est représenté
                                par un tuple (index, x, y, demande).

    Returns:
    - list of list of int: Une matrice où chaque élément [i][j] représente
                           la distance entre le client i et le client j
                           ou entre le dépôt et un client.

    Description:
    Cette fonction crée une matrice de distance en ajoutant la distance
    euclidienne entre le dépôt et chaque client, ainsi qu'entre chaque client.
    Le dépôt est traité comme l'élément `0` de la matrice, suivi des clients.
    """
    n = len(clients)
    # Initialise la matrice de distance avec des zéros
    distance_matrix = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(n + 1):
            # Utiliser le dépôt comme point de référence si i ou j est 0
            if i == 0:
                x1, y1 = depot
            else:
                x1, y1 = clients[i - 1][1], clients[i - 1][2]

            if j == 0:
                x2, y2 = depot
            else:
                x2, y2 = clients[j - 1][1], clients[j - 1][2]

            # Calcule et stocke la distance entre les points i et j
            distance_matrix[i][j] = euclidean_distance(x1, y1, x2, y2)
    return distance_matrix


def create_routes(clients, capacity):
    """
    Crée des routes pour des véhicules en fonction de la demande des clients
    et de la capacité maximale des véhicules.

    Parameters:
    - clients (list of tuples): Liste de clients, chaque client est représenté
                                par un tuple (index, x, y, demande).
    - capacity (int): Capacité maximale d'un véhicule.

    Returns:
    - list of lists: Liste des routes, où chaque route est une liste des indices
                     de clients qui peuvent être desservis dans cette route.

    Description:
    Cette fonction utilise un algorithme glouton pour créer des routes :
    1. Trie les clients par demande décroissante.
    2. Itère sur chaque client et essaie de l'ajouter à la route actuelle.
    3. Si l'ajout d'un client dépasse la capacité, la route actuelle est terminée
       et une nouvelle route est créée pour ce client.
    4. La fonction retourne une liste de routes respectant la capacité maximale
       de chaque véhicule.
    """
    # Trie les clients par demande en ordre décroissant pour un remplissage optimal
    clients = sorted(clients, key=lambda client: client[3], reverse=True)
    routes = []       # Liste des routes finales
    current_route = []  # Route en cours de construction
    current_load = 0    # Charge actuelle de la route

    for client in clients:
        client_index, x, y, demand = client

        # Vérifie si le client peut être ajouté à la route actuelle sans dépasser la capacité
        if current_load + demand <= capacity:
            current_route.append(client_index)
            current_load += demand
        else:
            # Si la capacité est dépassée, termine la route actuelle et en commence une nouvelle
            if current_route:
                routes.append(current_route)
            current_route = [client_index]  # Nouvelle route avec le client actuel
            current_load = demand

    # Ajoute la dernière route formée, s'il en reste une
    if current_route:
        routes.append(current_route)

    return routes
