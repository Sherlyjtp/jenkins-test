def game (jugador1, jugador2):
    """
    enter values that represent the player
    choice return p1 if player 1 wins otherway p2
    """
    
    if jugador1 == 'piedra' and jugador2 == 'papel' :
        return 'Gana jugador2'
    elif jugador1 =='piedra' and jugador2 == 'tijera' :
        return 'Gana jugador1'
    elif jugador1 == 'papel' and jugador2 == 'tijera' :
        return 'Gana jugador2'
    elif jugador1 == 'papel' and jugador2 == 'piedra' :
        return 'Gana jugador1'
    elif jugador1 == 'tijera' and jugador2 == 'piedra' :
        return 'Gana jugador2'
    elif jugador1 == 'tijera' and jugador2 == 'papel' :
        return 'Gana jugador2'
    else:
        return 'No hay juego'


