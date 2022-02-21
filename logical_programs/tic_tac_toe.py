board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def cross_game():
    """Cross game or Tic-tac-toe game
    Parameters:
        Taking user input for player1 and player2 to mark X and O
    Returns:
        Prints the board after every step until the result
    """
    while True:
        tictactoe()
        if input('Play Again(y/n)\n') != 'y':  # Asking whether the users want to play again
            break


def tictactoe():
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


# Printing the board
def draw():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])
    print()


# Asking Player1 to choose the position to fill up the value and then printing the board
def player1():
    n = choose_number()
    if board[n] == 'X' or board[n] == 'O':
        print('\n Value already there')
        player1()
    else:
        board[n] = 'X'


# Asking 2 to choose the position to fill up the value and then printing the board
def player2():
    n = choose_number()
    if board[n] == 'X' or board[n] == 'O':
        print('\n Value already there')  # if the values are already present then ask again to play
        player2()
    else:
        board[n] = 'O'


def choose_number():
    # Ensuring that the input value is an integer value displaying on the board
    while True:
        try:
            a = int(input())
            if a in board:
                return a
            else:
                print('\n Try Again')
        except ValueError:
            print('Not a number. Retry')


def game_over():
    # if the winning combination is satisfied, then the respective player wins
    count = 0
    for i, j, k in win_combinations:
        if board[i] == board[j] == board[k] == 'X':
            print('Player 1 Wins!\n')
            print('Congratulations!\n')
            return True
        if board[i] == board[j] == board[k] == 'O':
            print('Player 2 Wins!\n')
            print('Congratulations!\n')
            return True
    # Printing tie if all the cells are full with no win combinations
    for i in range(9):
        if board[i] == 'X' or board[i] == 'O':
            count += 1
            if count == 9:
                print('Tie\n')
                return True


def main():
    try:
        cross_game()
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
