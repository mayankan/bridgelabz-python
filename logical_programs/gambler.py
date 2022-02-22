# Import random package to get random 0 or 1 which means user won or lost the bet.
import random


def gambling(stake, goal, trials):
    """
    Does Gambling for a user with given stake, a goal amount to reach and provided no. of trials and returns no. of
    wins and percentage of wins and losses.
    :param stake: The Initial Stake Amount the user is gambling.
    :param goal: The Goal Amount till User wants to Gamble.
    :param trials: The Number of Trials User wants to Gamble.
    :return: The Number of Wins and Number of Trials user played in the gamble.
    """
    try:
        trials_completed = 0
        wins = 0
        for times in range(trials):
            while stake != goal and stake != 0:
                trials_completed += 1
                if random.randint(0, 1) == 0:
                    stake += 1
                    wins += 1
                else:
                    stake -= 1
            if stake == goal:
                break
        return wins, trials_completed
    except Exception as e:
        print("{} is raised.".format(e))


def main():
    try:
        stake = int(input("Enter stake: "))
        goal = int(input("Enter a goal: "))
        trials = int(input("Enter no. of trials: "))
        wins, no_of_trials = gambling(stake, goal, trials)
        print(str(wins) + ' wins')
        print(str(100 * wins / no_of_trials) + '% wins')
        print(str((1 - wins / no_of_trials) * 100) + '% loss')
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
