import time


def simulate_stopwatch():
    """
        Simulate Stopwatch - Pressing Enter to start the stopwatch and stop the stopwatch
        :return: prints the Elapsed time
        """
    input("Press Enter to Start")
    start_time = time.time()
    input("Press Enter to Stop")
    end_time = time.time()
    # Measuring the elapsed time between start and end
    time_elapsed = end_time - start_time
    print(round(time_elapsed, 4), " seconds")


def main():
    try:
        simulate_stopwatch()
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
