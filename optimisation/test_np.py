# test_move_robot.py
from np import move_robot  # Remplacez 'np' par le nom correct de votre fichier si besoin

# Test 1: Un robot allant vers le haut
def test_robot_up():
    robots = [(0, 0, "U")]
    assert move_robot(robots) == [(0, 1, "U")]

# Test 2: Un robot allant vers le bas
def test_robot_down():
    robots = [(0, 0, "D")]
    assert move_robot(robots) == [(0, -1, "D")]

# Test 3: Un robot allant vers la gauche
def test_robot_left():
    robots = [(0, 0, "L")]
    assert move_robot(robots) == [(-1, 0, "L")]

# Test 4: Un robot allant vers la droite
def test_robot_right():
    robots = [(0, 0, "R")]
    assert move_robot(robots) == [(1, 0, "R")]

# Test 5: Plusieurs robots avec différentes directions
def test_multiple_robots():
    robots = [
        (0, 0, "U"),
        (1, 1, "D"),
        (2, 2, "L"),
        (3, 3, "R")
    ]
    assert move_robot(robots) == [(0, 1, "U"), (1, 0, "D"), (1, 2, "L"), (4, 3, "R")]

# Test 6: Robots à des positions négatives
def test_negative_positions():
    robots = [
        (-1, -1, "U"),
        (-2, -2, "D"),
        (-3, -3, "L"),
        (-4, -4, "R")
    ]
    assert move_robot(robots) == [(-1, 0, "U"), (-2, -3, "D"), (-4, -3, "L"), (-3, -4, "R")]

# Test 7: Robots sur une ligne avec directions opposées
def test_same_position_different_directions():
    robots = [
        (5, 5, "U"),
        (5, 5, "D"),
        (5, 5, "L"),
        (5, 5, "R")
    ]
    assert move_robot(robots) == [(5, 6, "U"), (5, 4, "D"), (4, 5, "L"), (6, 5, "R")]

# Test 8: Robots avec des directions inconnues
def test_unknown_directions():
    robots = [
        (0, 0, "X"),
        (1, 1, "Y"),
        (2, 2, "Z")
    ]
    assert move_robot(robots) == [(0, 0, "X"), (1, 1, "Y"), (2, 2, "Z")]


