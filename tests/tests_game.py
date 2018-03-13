from game import game

def test_game_01():
    assert game('piedra', 'tijera') == 'Gana jugador1', 'Debe ganar jugador2'
    assert game('tijera', 'piedra') == 'Gana jugador2', 'Unexpected result'
    assert game('tijera', 'papel') == 'Gana jugador2', 'Unexpected result'



