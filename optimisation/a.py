import math
import heapq

def a_star(n, s, g, heuristics, edges):
    """
    Implémente l'algorithme A* pour trouver le chemin le plus court dans un graphe pondéré.

    L'algorithme A* utilise une heuristique pour estimer le coût d'atteindre le but
    à partir de chaque nœud, combinant le coût déjà parcouru (g) et le coût estimé
    à atteindre le but (h). Il est particulièrement efficace pour les graphes où une
    estimation précise du coût est disponible.

    Type d'algorithme :
    L'algorithme A* est un algorithme de recherche de chemin qui fonctionne en temps polynomial,
    généralement O(E), où E est le nombre d'arêtes dans le graphe. Il utilise une file de priorité
    pour explorer les nœuds en fonction de leur coût total estimé (f = g + h).

    Paramètres :
        n (int): Le nombre total de nœuds dans le graphe.
        s (int): L'indice du nœud de départ.
        g (int): L'indice du nœud objectif.
        heuristics (list of int): Liste des valeurs heuristiques pour chaque nœud,
                                   où heuristics[i] est la valeur heuristique pour le nœud i.
        edges (list of tuple): Liste des arêtes du graphe, où chaque arête est représentée
                               par un tuple (x, y, c) indiquant une connexion entre les nœuds x et y
                               avec un coût c.

    Retour :
        list of tuple: Une liste des nœuds explorés dans l'ordre, où chaque nœud est associé
                       à sa valeur f (le coût total estimé) au moment de l'exploration.
    """

    # Initialisation du graphe sous forme de dictionnaire
    graph = {i: [] for i in range(n)}
    for x, y, c in edges:
        graph[x].append((y, c))  # Ajoute une connexion de x à y avec le coût c
        graph[y].append((x, c))  # Ajoute une connexion de y à x avec le coût c (graphe non orienté)

    # Initialisation des valeurs g (coût réel) et f (coût total estimé) pour chaque nœud
    g_values = {node: math.inf for node in range(n)}  # Coût initialisé à l'infini
    g_values[s] = 0  # Coût de départ est 0
    f_values = {node: math.inf for node in range(n)}  # Coût total estimé initialisé à l'infini
    f_values[s] = heuristics[s]  # Coût total estimé pour le nœud de départ

    # Utilisation d'un tas (min-heap) pour la file de priorité
    open_set = [(f_values[s], s)]  # Initialisation de la file avec le nœud de départ
    explored_order = []  # Pour garder la trace des nœuds explorés

    # Un ensemble pour suivre les nœuds visités
    visited = set()

    while open_set:
        # Extraction du nœud avec le plus petit f (coût total estimé)
        current_f, current = heapq.heappop(open_set)

        # Éviter d'explorer les nœuds déjà visités
        if current in visited:
            continue
        visited.add(current)

        # Enregistrement de l'ordre d'exploration
        explored_order.append((current, current_f))

        # Si on atteint le but, on peut arrêter l'exploration
        if current == g:
            break

        # Exploration des voisins
        for neighbor, cost in graph[current]:
            tentative_g = g_values[current] + cost  # Calculer le coût du chemin temporaire

            # Vérifiez si le chemin trouvé est meilleur
            if tentative_g < g_values[neighbor]:
                g_values[neighbor] = tentative_g  # Mettre à jour le coût réel pour le voisin
                f_values[neighbor] = tentative_g + heuristics[neighbor]  # Mettre à jour le coût total estimé

                # Ajouter le voisin à la file de priorité
                heapq.heappush(open_set, (f_values[neighbor], neighbor))

    return explored_order  # Retourne l'ordre d'exploration des nœuds

# Fonction principale pour exécuter l'algorithme
def main():
    # Définir les valeurs d'entrée
    n = 4  # Nombre de nœuds
    e = 3  # Nombre d'arêtes
    s = 0  # Nœud de départ
    g = 2  # Nœud de destination
    heuristics = [33, 11, 0]  # Heuristiques
    edges = [(0, 1, 10), (0, 2, 40), (1, 2, 20)]  # Arêtes (x, y, coût)

    # Exécuter l'algorithme A*
    results = a_star(n, s, g, heuristics, edges)
    # Afficher les résultats
    for node, f_value in results:
        print(f"{node} {f_value}")

# Exécute le programme principal
if __name__ == "__main__":
    main()
