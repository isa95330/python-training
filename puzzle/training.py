from collections import Counter


def create_phone_number(n):
    """
    Cette fonction prend une liste de 10 chiffres et retourne une chaîne de caractères
    au format d'un numéro de téléphone américain (XXX) XXX-XXXX.

    Arguments:
    n -- liste de 10 chiffres (par exemple, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

    Retourne:
    Une chaîne formatée au format "(XXX) XXX-XXXX", par exemple "(123) 456-7890".

    Explication :
    - La méthode `format` est utilisée pour insérer chaque chiffre au bon endroit dans la chaîne.
    - L'opérateur `*n` décompresse la liste `n` en arguments individuels, ce qui permet
      de passer chaque élément de la liste comme un argument distinct à `format`.
      Cela évite d'avoir à référencer chaque élément individuellement (par exemple n[0], n[1], ...).
    """

    # Utilisation de format pour placer les chiffres de la liste aux bons emplacements
    # dans la chaîne. La chaîne "{}{}{} {}{}{}-{}{}{}{}" attend 10 arguments.
    # L'opérateur * décompose la liste `n` en 10 arguments distincts pour format.
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


def order(sentence):
    """Trie les mots d'une phrase en fonction du chiffre contenu dans chaque mot.

    Cette fonction prend une chaîne de caractères en entrée, où chaque mot contient un seul chiffre
    (de 1 à 9). Elle renvoie une nouvelle chaîne de caractères, où les mots sont réorganisés selon
    l'ordre déterminé par les chiffres qu'ils contiennent.

    La fonction commence par vérifier si la chaîne d'entrée est vide. Si c'est le cas, elle renvoie
    une chaîne vide. Sinon, elle divise la phrase en mots, puis trie ces mots en utilisant une clé
    de tri définie par un lambda qui extrait le chiffre du mot. Le chiffre est extrait à l'aide de
    la fonction `filter`, qui utilise `str.isdigit` pour isoler les chiffres présents dans chaque mot.

    Args:
        sentence (str): La phrase d'entrée contenant des mots avec des chiffres (de 1 à 9).

    Returns:
        str: La phrase avec les mots ordonnés par le chiffre qu'ils contiennent. Si la chaîne d'entrée
              est vide, la fonction renvoie également une chaîne vide.
    """
    # Vérifie si la chaîne est vide et renvoie une chaîne vide si c'est le cas
    if not sentence:
        return ""

    # Utilise une compréhension de liste pour extraire et trier les mots par le chiffre qu'ils contiennent
    return ' '.join(sorted(sentence.split(), key=lambda word: int(next(filter(str.isdigit, word)))))


def longest(a1, a2):
    """Retourne la chaîne la plus longue possible composée de caractères uniques, triée par ordre alphabétique.

    Cette fonction prend deux chaînes de caractères en entrée et renvoie une nouvelle chaîne
    contenant tous les caractères uniques des deux chaînes d'entrée, triés par ordre alphabétique.

    Args:
        a1 (str): La première chaîne de caractères.
        a2 (str): La deuxième chaîne de caractères.

    Returns:
        str: Une chaîne contenant tous les caractères uniques des deux chaînes d'entrée,
              triés par ordre alphabétique.
    """
    # Utilise un ensemble pour obtenir les caractères uniques des deux chaînes
    unique_chars = set(a1 + a2)
    # Trie les caractères uniques par ordre alphabétique et les joint en une seule chaîne
    return ''.join(sorted(unique_chars))


def is_triangle(a, b, c):
    """
    Détermine si trois longueurs de côtés peuvent former un triangle valide.

    Un triangle est valide si la somme des longueurs de deux côtés est toujours supérieure
    à la longueur du troisième côté. De plus, les trois longueurs doivent être strictement positives.

    La fonction effectue les étapes suivantes :
    1. Trie les longueurs des côtés dans l'ordre croissant pour simplifier les comparaisons.
    2. Vérifie si la plus petite longueur est strictement positive.
    3. Vérifie que la somme des deux plus petites longueurs est supérieure à la plus grande.

    Args:
        a (int, float): La première longueur du côté.
        b (int, float): La deuxième longueur du côté.
        c (int, float): La troisième longueur du côté.

    Returns:
        bool: Retourne True si les longueurs peuvent former un triangle valide, sinon False.

    Exemple d'utilisation :
        >>> is_triangle(3, 4, 5)
        True
        >>> is_triangle(1, 2, 3)
        False
        >>> is_triangle(0, 5, 7)
        False

    Pourquoi cette méthode fonctionne :
    - En triant les côtés, on s'assure que les deux premières longueurs (les plus petites)
      sont comparées à la plus grande, ce qui permet de simplifier la vérification.
    - Le tri permet également de ne vérifier qu'une seule condition sur la somme des deux plus petits côtés
      par rapport au troisième, au lieu de vérifier trois conditions séparées.
    """
    sides = sorted([a, b, c])
    return sides[0] > 0 and sides[0] + sides[1] > sides[2]


def rgb(r, g, b):
    """Convertit des valeurs RGB décimales en une représentation hexadécimale.

    Cette fonction prend trois valeurs entières représentant les composantes
    rouge, verte et bleue d'une couleur. Chaque valeur doit être comprise entre
    0 et 255. Si une valeur est en dehors de cette plage, elle est arrondie
    à la valeur la plus proche (0 ou 255).

    Les valeurs résultantes sont ensuite formatées en une chaîne hexadécimale
    de six caractères, où chaque paire de caractères représente une des
    composantes de couleur. La représentation hexadécimale est toujours en
    majuscules.

    Args:
        r (int): La valeur de la composante rouge, entre 0 et 255.
        g (int): La valeur de la composante verte, entre 0 et 255.
        b (int): La valeur de la composante bleue, entre 0 et 255.

    Returns:
        str: Une chaîne de caractères hexadécimale représentant la couleur,
              formatée sous la forme 'RRGGBB', où RR, GG et BB sont des
              valeurs hexadécimales de deux chiffres pour les composantes
              rouge, verte et bleue respectivement.

    Examples:
        >>> rgb(255, 255, 255)
        'FFFFFF'
        >>> rgb(255, 255, 300)
        'FFFFFF'
        >>> rgb(0, 0, 0)
        '000000'
        >>> rgb(148, 0, 211)
        '9400D3'

    Notes:
        - Les valeurs de couleur doivent être des entiers.
        - Si une valeur est inférieure à 0, elle sera considérée comme 0.
        - Si une valeur est supérieure à 255, elle sera considérée comme 255.
    """
    # Utilise max et min pour restreindre les valeurs entre 0 et 255, puis formate en hexadécimal
    return ''.join(f'{max(0, min(255, c)):02X}' for c in (r, g, b))



def count(s):
    """Compte le nombre d'occurrences de chaque caractère dans une chaîne donnée.

    Args:
        s (str): La chaîne d'entrée dont les caractères doivent être comptés.

    Returns:
        dict: Un dictionnaire contenant les caractères comme clés et leurs
              occurrences comme valeurs.
    """
    return dict(Counter(s))

def dir_reduc(arr):
    """
    Cette fonction prend une liste de directions (nord, sud, est, ouest) et retourne une liste de directions
    simplifiée en éliminant les directions opposées consécutives.

    Arguments:
    arr -- liste de directions (par exemple, ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])

    Retourne:
    Une liste de directions simplifiée, sans les directions opposées consécutives.
    """

    # Définit une correspondance entre les directions opposées
    opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}

    # Initialise une pile pour stocker les directions simplifiées
    stack = []

    # Parcourt chaque direction dans la liste
    for direction in arr:
        # Vérifie si la pile n'est pas vide et si la direction actuelle est opposée à la dernière direction empilée
        if stack and stack[-1] == opposites[direction]:
            # Supprime la dernière direction
            stack.pop()
        else:
            # Empile la nouvelle direction
            stack.append(direction)

    # Retourne la liste de directions simplifiée
    return stack


def dig_pow(n, p):
    k = 0
    for i, digit in enumerate(str(n), start=p):
        k += int(digit) ** i
        return -1
    else:
        return k // n