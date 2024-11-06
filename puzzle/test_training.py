import pytest
from training import create_phone_number, order, longest, is_triangle, rgb, count


def test_create_phone_number():
    assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
    assert create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111"
    assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
    assert create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]) == "(023) 056-0890"
    assert create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "(000) 000-0000"


def test_order():

    assert order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
    assert order("4of Fo1r pe6ople g3ood th5e the2") == "Fo1r the2 g3ood 4of th5e pe6ople"
    assert order("") == ""  # Vérifie que l'output est bien une chaîne vide



def test_longest():

    assert longest("aretheyhere", "yestheyarehere") == "aehrsty"
    assert longest("loopingisfunbutdangerous", "lessdangerousthancoding") == "abcdefghilnoprstu"
    assert longest("inmanylanguages", "theresapairoffunctions") == "acefghilmnoprstuy"


def test_is_triangle():
    assert is_triangle(1, 2, 2) == True
    assert is_triangle(7, 2, 2) == False
    assert is_triangle(1, 2, 3) == False
    assert is_triangle(1, 3, 2) == False
    assert is_triangle(3, 1, 2) == False
    assert is_triangle(5, 1, 2) == False
    assert is_triangle(1, 2, 5) == False
    assert is_triangle(2, 5, 1) == False
    assert is_triangle(4, 2, 3) == True
    assert is_triangle(5, 1, 5) == True
    assert is_triangle(2, 2, 2) == True
    assert is_triangle(-1, 2, 3) == False

def test_rgb():
    assert rgb(0, 0, 0) == "000000"
    assert rgb(1, 2, 3) == "010203"
    assert rgb(255, 255, 255) == "FFFFFF"
    assert rgb(254, 253, 252) == "FEFDFC"
    assert rgb(-20, 275, 125) == "00FF7D"


def test_count():
    assert count("aba") == {'a': 2, 'b': 1}
    assert count("abab") == {'a': 2, 'b': 2}
    assert count("aabb") == {'a': 2, 'b': 2}
    assert count("aabbc") == {'a': 2, 'b': 2, 'c': 1}
    assert count("aabbcc") == {'a': 2, 'b': 2, 'c': 2}

