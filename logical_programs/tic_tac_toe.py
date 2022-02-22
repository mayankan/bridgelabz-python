import random

BOARD = [0, 1, 2, 3, 4, 5, 6, 7, 8]
WIN_COMBINATIONS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def cross_game():
    """
    Iterates Tic Tac Toe Game till user enters anything other than y as input for Play Again(y/n):
    """
    try:
        while True:
            tictactoe()
            if input('Play Again(y/n): ') != 'y':  # Asking whether the users want to play again
                break
    except Exception as e:
        print("{} is raised.".format(e))


def tictactoe():
    """
    Iterates Tic Tac Toe Game for both Player 1 and Player 2 turns until game ends.
    """
    try:
        end = False
        # Possible winning outcomes
        while not end:
            draw()
            end = game_over()
            if end is True:
                break
            print('Player 1 play...')
            player1()
            print()
            draw()
            end = game_over()
            if end is True:
                break
            print('Player 2 play...')
            player2()
            print()
    except Exception as e:
        print("{} is raised.".format(e))


def draw():
    """
    Prints the draw board after the game is draw.
    """
    try:
        print(BOARD[0], BOARD[1], BOARD[2])
        print(BOARD[3], BOARD[4], BOARD[5])
        print(BOARD[6], BOARD[7], BOARD[8])
        print()
    except Exception as e:
        print("{} is raised.".format(e))


def player1():
    """
    Randomly checks a position on the board for Player 1(Computer) and updates Board positions for Player 1.
    """
    try:
        n = random.randrange(0, 9)
        if BOARD[n] == 'X' or BOARD[n] == 'O':
            player1()
        else:
            BOARD[n] = 'O'
    except Exception as e:
        print("{} is raised.".format(e))


# Asking 2 to choose the position to fill up the value and then printing the board
def player2():
    """
    Calls choose_number function to take input for Player 2 and updates Board position for Player 2 if not already
    checked.
    """
    try:
        n = choose_number()
        if BOARD[n] == 'X' or BOARD[n] == 'O':
            print('\n Value already there')  # if the values are already present then ask again to play
            player2()
        else:
            BOARD[n] = 'X'
    except Exception as e:
        print("{} is raised.".format(e))


def choose_number():
    """
    Gets a number from user to select a Board position and checks for issues.
    """
    while True:
        try:
            a = int(input())
            if a in BOARD:
                return a
            else:
                print('Try Again')
        except ValueError:
            print('Not a number. Retry')
        except Exception as e:
            print("{} is raised.".format(e))


def game_over():
    try:
        # if the winning combination is satisfied, then the respective player wins
        count = 0
        for i, j, k in WIN_COMBINATIONS:
            if BOARD[i] == BOARD[j] == BOARD[k] == 'O':
                print('Player 1 Wins!')
                print('Congratulations!')
                return True
            if BOARD[i] == BOARD[j] == BOARD[k] == 'X':
                print('Player 2 Wins!')
                print('Congratulations!')
                return True
        # Printing tie if all the cells are full of no win combinations
        for i in range(9):
            if BOARD[i] == 'X' or BOARD[i] == 'O':
                count += 1
                if count == 9:
                    print('Tie')
                    return True
    except Exception as e:
        print("{} is raised.".format(e))


def main():
    try:
        cross_game()
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
