# Import random package to get random values between 1 and 6 to roll dice.
import random

# Ladder : Dictionary to have Ladder points on board -> Will jump above the player's position.
LADDER = {
    10: 31,
    20: 42,
    45: 78,
    70: 98
}

# Snake : Dictionary to have Snake points on board -> Will climb down the player's position.
SNAKE = {
    30: 2,
    50: 21,
    68: 46,
    72: 55,
    89: 72
}

WIN_POINT = 100  # Final Position of the Winner of the game.


def check_snake_and_ladder(prev_pos, dice):
    """
    Checks the next position of the player for snake or ladder positions and returns the new position accordingly.
    :param prev_pos: Previous Position of the player before rolling the dice. :param dice: Dice value between 1 and
    12 given by random function. :return: New Position which is same as Previous Position if it is above Winning
    Point else adding dice value to the Previous Position and checking snake or ladder positions and returning the
    final value after manipulation.
    """
    try:
        new_pos = prev_pos + dice
        if new_pos <= WIN_POINT:
            _snake = SNAKE.get(new_pos)
            if _snake:
                return "snake", _snake
            _ladder = LADDER.get(new_pos)
            if _ladder:
                return "ladder", _ladder
            return "simple_move", new_pos
        return "above_win_point", prev_pos
    except Exception as e:
        print("{} is raised.".format(e))


def check_win(current_pos):
    """
    Checks if the Player won by having current position to 100.
    :param current_pos: Current Position after adding the Dice value.
    :return: True if Player has won else False.
    """
    try:
        return current_pos == WIN_POINT
    except Exception as e:
        print("{} is raised.".format(e))


def play(prev_pos):
    """
    Snake Ladder game player for a Player's position which returns the next position to continue the game.
    :param prev_pos: Current Position before rolling dice and going to the next position
    :return: -1 if Player as won, else the next position Player stands on.
    """
    try:
        dice = throw_dice()
        re_roll, dice = check_six_on_dice(dice)
        if re_roll:
            print("{0} came on dice after rolling dice twice at {1} position.".format(dice, prev_pos))
        else:
            print("{0} came on dice at {1} position.".format(dice, prev_pos))
        # Optimise this snake and ladder case
        move, new_pos = check_snake_and_ladder(prev_pos, dice)
        if move == "snake":  # if snake return snake value
            print("Snake bite at", new_pos)
            return new_pos
        elif move == "ladder":  # if snake don't check for ladder / if ladder return ladder value
            print("Ladder taken to", new_pos)
            return new_pos
        elif move == "above_win_point":
            print("Sorry, Player will not move as th position is above Winning Point.")
            return new_pos
        else:
            i_won = check_win(new_pos)  # if snake or ladder is there avoid win call
            if i_won:
                return -1
            else:
                print("Player moved from {0} to {1}".format(prev_pos, new_pos))
                return new_pos
    except Exception as e:
        print("{} is raised.".format(e))


def throw_dice():
    """
    Returns the Dice value between 1 and 6 using random function.
    :return: Value between 1 and 6.
    """
    try:
        return random.randint(1, 6)
    except Exception as e:
        print("{} is raised.".format(e))


# Add two dice throws at 6
def check_six_on_dice(dice):
    """
    Checks if dice values is 6 and re-rolls the dice using throw_dice function and adding the value.
    :param dice: Current Dice Value.
    :return: Adding another Dice value if 6 came on previous Dice value.
    """
    try:
        if dice == 6:
            return True, 6 + throw_dice()
        return False, dice
    except Exception as e:
        print("{} is raised.".format(e))


def main():
    try:
        player1 = 0
        player2 = 0
        while True:
            print("Player 1 Rolled dice.")
            player1 = play(player1)
            if player1 == -1:
                print('Player 1 won')
                break
            print("Player 2 Rolled dice.")
            player2 = play(player2)
            if player2 == -1:
                print('Player 2 won')
                break
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()

# def check_snake(prev_pos, dice):
#     new_pos = prev_pos + dice
#     if new_pos <= WIN_POINT:
#         _snake = SNAKE.get(new_pos)
#         if _snake:
#             return _snake
#         else:
#             return new_pos
#     return prev_pos


# def check_ladder(prev_pos, dice):
#     new_pos = prev_pos + dice
#     if new_pos <= WIN_POINT:
#         _ladder = LADDER.get(new_pos)
#         if _ladder:
#             return _ladder
#         else:
#             return new_pos
#     return prev_pos
