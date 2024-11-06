from a import a_star
import pytest


@pytest.mark.parametrize("n, e, s, g, heuristics, edges, expected_output", [
    (
            3, 3, 0, 2,
            [33, 11, 0],
            [(0, 1, 10), (0, 2, 40), (1, 2, 20)],
            [(0, 33), (1, 21), (2, 30)]
    ),

    (
            20, 23, 0, 1,
            [366, 0, 160, 242, 161, 178, 77, 151, 226, 244, 241, 234, 380, 98, 193, 253, 329, 80, 199, 374],
            [(12, 19, 71), (12, 15, 151), (0, 19, 75), (0, 15, 140), (0, 16, 118), (16, 9, 111),
             (9, 10, 70), (10, 3, 75), (3, 2, 120), (2, 13, 138), (2, 14, 146), (14, 13, 97),
             (14, 15, 80), (15, 5, 99), (13, 1, 101), (1, 6, 90), (1, 17, 85), (17, 7, 98),
             (7, 4, 86), (17, 18, 142), (18, 8, 92), (8, 11, 87)],
            [(0, 366), (15, 393), (14, 413), (13, 415), (5, 417), (1, 418)]
    ),
])
def test_a_star(n, e, s, g, heuristics, edges, expected_output):
    result = a_star(n, s, g, heuristics, edges)

    # Formatage du résultat pour correspondre à la sortie attendue
    output = [(node, f_value) for node, f_value in result]
    assert output == expected_output


if __name__ == "__main__":
    pytest.main()