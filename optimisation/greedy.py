import math
import sys

# Fonction pour calculer la distance euclidienne
def euclidean_distance(point1, point2):
    """
    Calcule la distance euclidienne entre deux points.

    Paramètres :
        point1 (tuple): Coordonnées du premier point (x1, y1).
        point2 (tuple): Coordonnées du second point (x2, y2).

    Retourne :
        float: La distance euclidienne entre point1 et point2.
    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Fonction pour résoudre le TSP avec l'algorithme du plus proche voisin
def tsp_nearest_neighbor(points):
    """
    Résout le problème du voyageur de commerce (TSP) en utilisant l'algorithme du plus proche voisin.

    Paramètres :
        points (list of tuple): Liste de tuples représentant les coordonnées des points (x, y).

    Retourne :
        tour (list): Liste des indices des points dans l'ordre de visite.
        total_distance (float): Distance totale du parcours.
    """
    n = len(points)  # Nombre total de points
    visited = [False] * n  # Liste pour suivre les points visités
    tour = []  # Liste pour le parcours
    total_distance = 0.0  # Distance totale du parcours

    # Point de départ : commencer au premier point (index 0)
    current_index = 0
    visited[current_index] = True  # Marquer le point de départ comme visité
    tour.append(current_index)  # Ajouter le point de départ au parcours

    # Boucle pour visiter tous les points restants
    for step in range(1, n):
        nearest_distance = float('inf')  # Initialiser la distance la plus proche avec l'infini
        nearest_index = None  # Initialiser l'index du point le plus proche

        # Trouver le point le plus proche qui n'a pas encore été visité
        for i in range(n):
            if not visited[i]:  # Vérifier si le point i n'est pas visité
                # Calculer la distance entre le point actuel et le point i
                distance = euclidean_distance(points[current_index], points[i])
                # Vérifier si cette distance est la plus courte trouvée jusqu'à présent
                if distance < nearest_distance:
                    nearest_distance = distance  # Mettre à jour la distance la plus proche
                    nearest_index = i  # Mettre à jour l'index du point le plus proche

        # Vérification si un point le plus proche a été trouvé
        if nearest_index is None:
            print("Erreur : Aucun point non visité trouvé.", file=sys.stderr)
            return tour, total_distance  # Retourner les valeurs actuelles

        # Affichage de débogage pour suivre le processus
        print(f"Étape {step}: point actuel {current_index}, point le plus proche {nearest_index} avec distance {nearest_distance}", file=sys.stderr)

        # Mettre à jour la distance totale et le parcours
        total_distance += nearest_distance  # Ajouter la distance du point le plus proche à la distance totale
        current_index = nearest_index  # Déplacer le point actuel au point le plus proche
        visited[current_index] = True  # Marquer ce point comme visité
        tour.append(current_index)  # Ajouter le point visité au parcours

    # Retourner au point de départ après avoir visité tous les autres points
    final_leg_distance = euclidean_distance(points[current_index], points[0])  # Calculer la distance de retour
    total_distance += final_leg_distance  # Ajouter cette distance à la distance totale
    tour.append(0)  # Ajouter le point de départ au tour final

    # Affichage de la dernière distance ajoutée et de la distance totale finale
    print(f"Retour au point de départ: ajout de la distance {final_leg_distance}", file=sys.stderr)
    print(f"Distance totale finale : {total_distance}", file=sys.stderr)

    return tour, total_distance  # Retourner le parcours et la distance totale
