import random


def gambling(stake, goal, trials):
    """
    Does Gambling for a user with given stake, a goal amount to reach and provided no. of trials and returns no. of wins and percentage of wins and losses.
    :param stake:
    :param goal:
    :param trials:
    :return:
    """
    bets = 0
    wins = 0

    for t in range(trials):
        cash = stake
        # The user bets until he/she reaches the goal or gets broke
        while 0 < cash < goal:
            bets += 1
            if random.randrange(0, 2) == 0:
                cash += 1
            else:
                cash -= 1
        if cash == goal:
            wins += 1
    print(str(wins) + ' wins')
    print(str(100 * wins / trials) + '% wins')
    print(str((1 - wins / trials) * 100) + '% loss')


def main():
    try:
        stake = int(input("Enter stake: "))
        goal = int(input("Enter a goal: "))
        trials = int(input("Enter no. of trials: "))
        gambling(stake, goal, trials)
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
