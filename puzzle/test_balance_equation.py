from puzzle.balance_equation import balance_equation

def test_balance_equation():
    assert balance_equation('H2 + O2', 'H2O') == '2H2 + O2 -> 2H2O'


# Appelez cette fonction pour exécuter les tests
test_balance_equation()
