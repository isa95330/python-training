# Exercices d'Optimisation et Résolution de Problèmes Combinatoires

Ce dépôt contient une série d'exercices sur l'optimisation, principalement axée sur la résolution du **problème du voyageur de commerce (TSP)**, mais incluant également des algorithmes comme **A\*** et d'autres méthodes d'optimisation. Chaque exercice est détaillé dans des fichiers distincts et testé directement à l'intérieur du dossier `optimisation`.

## Structure du Projet

- `optimisation/` : Contient les exercices d'optimisation. Chaque exercice est détaillé avec un docstring pour expliquer l'algorithme, les méthodes utilisées et l'objectif.
- Les tests sont également situés directement dans le dossier `optimisation`, associés à chaque exercice.
- `env/` : Environnement virtuel pour installer les dépendances.
- `requirements.txt` : Liste des dépendances nécessaires pour exécuter le projet, y compris `pytest` pour les tests et d'autres bibliothèques.
- `.git/` : Dossier interne de Git pour la gestion du dépôt.

## Installation

1. Clonez ce dépôt sur votre machine locale :

    ```bash
    git clone https://github.com/username/nom-du-repository.git
    cd nom-du-repository
    ```

2. Créez un environnement virtuel nommé `env` :

    ```bash
    python -m venv env
    ```

3. Activez l'environnement virtuel :
   - Sur **Windows** :
     ```bash
     env\Scripts\activate
     ```
   - Sur **Mac/Linux** :
     ```bash
     source env/bin/activate
     ```

4. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

Après avoir installé les dépendances et configuré l'environnement virtuel, vous pouvez exécuter les exercices d'optimisation directement depuis le dossier `optimisation/`.

### Lancer les tests avec `pytest` :

Les tests sont intégrés directement dans les exercices. Pour exécuter les tests, vous pouvez utiliser la commande suivante :

```bash
pytest optimisation/
