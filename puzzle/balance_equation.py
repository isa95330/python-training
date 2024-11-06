import sympy as sp
import re

def parse_molecule(molecule):
    """Analyse une molécule et renvoie sa composition sous forme de dictionnaire."""
    elements = re.findall(r'([A-Z][a-z]?)(\d*)', molecule)
    composition = {}
    for element, count in elements:
        composition[element] = int(count) if count else 1  # Assigne 1 si pas de chiffre
    return composition

def balance_equation(left, right):
    """Équilibre une équation chimique donnée."""
    # Analyse les réactifs et les produits
    left_comp = [parse_molecule(molecule) for molecule in left.split(' + ')]
    right_comp = [parse_molecule(molecule) for molecule in right.split(' + ')]
    print("left_comp", left_comp)
    print("right_comp", right_comp)

    # Rassemble les éléments uniques
    elements = set().union(*left_comp, *right_comp)
    print("elements", elements)

    # Définit les variables symboliques pour les coefficients
    num_left = len(left_comp)
    num_right = len(right_comp)
    coeffs = sp.symbols(f'c0:{num_left + num_right}')
    print("coeffs", coeffs)
    print("num_left", num_left)
    print("num_right", num_right)

    # Crée les équations pour chaque élément
    equations = []
    for element in elements:
        left_count = sum(coeffs[i] * left_comp[i].get(element, 0) for i in range(num_left))
        print("left_count for", element, ":", left_count)  # Debug
        right_count = sum(coeffs[num_left + j] * right_comp[j].get(element, 0) for j in range(num_right))
        equations.append(sp.Eq(left_count, right_count))

    # Affiche les équations pour débogage
    print("Equations à résoudre:")
    for equation in equations:
        print(equation)

    # Résout le système d'équations
    solution = sp.solve(equations, coeffs, dict=True)
    if not solution:
        return "Impossible à équilibrer"

    # Prend la première solution
    sol = solution[0]

    # Trouve le plus petit commun multiple des dénominateurs pour éliminer les fractions
    denominators = [sp.nsimplify(val).as_numer_denom()[1] for val in sol.values() if val != 0]
    factor = sp.lcm(denominators) if denominators else 1

    # Dictionnaires pour stocker les coefficients des réactifs et des produits
    reactant_coeffs = {}
    product_coeffs = {}

    # Remplit les dictionnaires avec les coefficients
    for i in range(num_left):
        coeff = sol.get(coeffs[i], 0)  # Prend la valeur du coefficient, 0 si pas défini
        coeff_value = factor * coeff.evalf() if hasattr(coeff, 'evalf') else factor * coeff
        coeff_value = int(coeff_value) if coeff_value.is_real and coeff_value.is_integer else 0
        reactant_coeffs[left.split(' + ')[i].strip()] = coeff_value

    for j in range(num_right):
        coeff = sol.get(coeffs[num_left + j], 1)  # Coefficient de 1 par défaut pour les produits
        coeff_value = factor * coeff.evalf() if hasattr(coeff, 'evalf') else factor * coeff
        coeff_value = int(coeff_value) if coeff_value.is_real and coeff_value.is_integer else 1  # Assure que c'est 1 si pas défini
        product_coeffs[right.split(' + ')[j].strip()] = coeff_value

    # Affiche les dictionnaires pour débogage
    print("Coefficients des réactifs:", reactant_coeffs)
    print("Coefficients des produits:", product_coeffs)

    # Construit la chaîne de l'équation équilibrée
    result = []

    for reactant in reactant_coeffs:
        coeff_value = reactant_coeffs[reactant]
        if coeff_value != 0:
            result.append(f"{coeff_value if coeff_value != 1 else ''}{reactant}")

    result.append("->")

    for product in product_coeffs:
        coeff_value = product_coeffs[product]
        if coeff_value != 0:
            result.append(f"{coeff_value if coeff_value != 1 else ''}{product}")

    # Joindre les parties de l'équation avec des espaces
    return " ".join(result)

# Exemple d'utilisation
if __name__ == "__main__":
    left_side = "H2 + O2"
    right_side = "H2O"
    balanced_equation_result = balance_equation(left_side, right_side)
    print(f"Équation équilibrée: {balanced_equation_result}")
