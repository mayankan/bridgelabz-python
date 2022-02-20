import random

# Ladder : Jump to some point

LADDER = {
    10: 31,
    20: 42,
    45: 78,
    70: 98
}

# Snake : Jump down
SNAKE = {
    30: 2,
    50: 21,
    68: 46,
    72: 55,
    89: 72
 }

WIN_POINT = 100


def check_snake(prev_pos, dice):
    new_pos = prev_pos + dice
    if new_pos <= WIN_POINT:
        _snake = SNAKE.get(new_pos)
        if _snake:
            return _snake
        else:
            return new_pos
    return prev_pos


def check_ladder(prev_pos, dice):
    new_pos = prev_pos + dice
    if new_pos <= WIN_POINT:
        _ladder = LADDER.get(new_pos)
        if _ladder:
            return _ladder
        else:
            return new_pos
    return prev_pos


def check_win(new_pos):
    return new_pos == WIN_POINT


def play(prev_pos):
    dice = throw_dice()
    is_snake = check_snake(prev_pos, dice)
    is_ladder = check_ladder(prev_pos, dice)
    if is_snake < prev_pos:  # if snake return snake value
        return is_snake
    elif is_ladder > prev_pos:  # if snake don't check for ladder / if ladder return ladder value
        return is_ladder
    else:
        i_won = check_win(is_snake)  # if snake or ladder is there avoid win call
        if i_won:
            return -1
        else:
            return is_snake


def throw_dice():
    return random.randint(1, 6)


def main():
    player1 = 0
    player2 = 0
    while True:
        player1 = play(player1)
        if player1 == -1:
            print('Player 1 won')
            break
        player2 = play(player2)
        if player2 == -1:
            print('Player 2 won')
            break


if __name__ == "__main__":
    main()
