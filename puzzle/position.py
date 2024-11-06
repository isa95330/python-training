import sys
import math

# Lecture des données d'initialisation
surfaceN = int(input())  # Nombre de points définissant la surface de Mars
surface_points = []

# Lecture des points de la surface
for i in range(surfaceN):
    landX, landY = map(int, input().split())
    surface_points.append((landX, landY))

# Détection de la zone d'atterrissage plate
landing_zone_start = None
landing_zone_end = None

for i in range(1, len(surface_points)):
    x1, y1 = surface_points[i - 1]
    x2, y2 = surface_points[i]
    if y1 == y2 and (x2 - x1) >= 1000:
        landing_zone_start = x1
        landing_zone_end = x2
        landing_y = y1
        break

# Boucle de jeu : lecture des données pour chaque tour
while True:
    # Données d'entrée pour chaque tour
    X, Y, hSpeed, vSpeed, fuel, rotate, power = map(int, input().split())

    # Calcul de la distance horizontale entre la capsule et la zone d'atterrissage
    target_x = (landing_zone_start + landing_zone_end) / 2  # Centre de la zone d'atterrissage
    horizontal_distance = X - target_x

    # Ajustement de la rotation pour se diriger vers le centre de la zone d'atterrissage
    if abs(horizontal_distance) > 500:
        # Si on est loin du centre de la zone d'atterrissage, incliner pour ajuster la trajectoire
        if horizontal_distance > 0 and hSpeed > -20:
            rotate = -15  # Inclinaison vers la gauche
        elif horizontal_distance < 0 and hSpeed < 20:
            rotate = 15  # Inclinaison vers la droite
        else:
            rotate = 0  # Reste à l'horizontale si la vitesse est correcte
    else:
        # Rester droit pour un atterrissage en douceur
        rotate = 0

    # Ajustement de la puissance pour gérer la vitesse verticale
    if vSpeed < -40:
        power = min(power + 1, 4)  # Augmenter la puissance pour ralentir la descente
    elif vSpeed > -30:
        power = max(power - 1, 0)  # Réduire la puissance pour économiser du carburant
    else:
        power = min(power, 4)  # Maintenir une poussée modérée

    # Output : les valeurs de rotation et de puissance pour ce tour
    print(rotate, power)
