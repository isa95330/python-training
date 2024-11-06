# def move_robot(robot_positions):
#     final_positions = []
#     for x, y, direction in robot_positions:
#         if direction == "U":
#             y += 1
#         elif direction == "D":
#             y -= 1
#         elif direction == "L":
#             x -= 1
#         elif direction == "R":
#             x += 1
#         final_positions.append((x, y, direction))
#     return final_positions

def move_robot(robot_positions):
    """
    Calcule les nouvelles positions des robots en fonction de leurs directions respectives.
    Chaque position initiale (x, y) est modifiée en ajoutant un décalage déterminé par
    une direction donnée : 'U' pour haut, 'D' pour bas, 'L' pour gauche, et 'R' pour droite.
    Les directions inconnues sont signalées et le robot conserve sa position initiale.

    Type d'algorithme :
    Cet algorithme utilise une approche de transformation de données en temps linéaire O(n),
    où chaque position de robot est mise à jour indépendamment des autres. Les déplacements
    sont calculés par correspondance via un dictionnaire de direction, assurant une recherche
    en temps constant pour chaque mise à jour.

    Paramètres :
        robot_positions (list of tuple): Liste de tuples (x, y, direction) représentant les
        positions initiales des robots et leurs directions de déplacement.

    Retour :
        list of tuple: Liste des nouvelles positions (x, y, direction) après le déplacement
        des robots.
    """

    # Dictionnaire de décalages pour chaque direction
    directions = {
        "U": (0, 1),    # Direction haut : y augmente de 1
        "D": (0, -1),   # Direction bas : y diminue de 1
        "L": (-1, 0),   # Direction gauche : x diminue de 1
        "R": (1, 0)     # Direction droite : x augmente de 1
    }

    # Liste pour stocker les nouvelles positions des robots après déplacement
    final_positions = []

    # Parcours de chaque robot et de sa direction
    for x, y, direction in robot_positions:
        # Vérifie si la direction est reconnue dans le dictionnaire
        if direction in directions:
            dx, dy = directions[direction]  # Récupère le décalage correspondant
            # Calcule la nouvelle position en ajoutant le décalage
            final_positions.append((x + dx, y + dy, direction))
        else:
            # Gestion de la direction inconnue : affiche un message et ignore le déplacement
            print(f"Direction '{direction}' inconnue, déplacement ignoré.")
            final_positions.append((x, y, direction))  # Ajoute la position d'origine sans déplacement

    # Retourne la liste des nouvelles positions
    return final_positions
