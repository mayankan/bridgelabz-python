import time


def stopwatch_calculation(start_time, end_time):
    """
    Returns elapsed time between start time and end time provided by user.
    :param start_time: Start time provided by user.
    :param end_time: End time provided by user.
    :return: End time minus start time rounded to seconds.
    """
    try:
        # Measuring the elapsed time between start and end
        time_elapsed = end_time - start_time
        return round(time_elapsed, 4)
    except Exception as e:
        print("{} is raised.".format(e))


def main():
    try:
        input("Press Enter to Start")
        start_time = time.time()
        input("Press Enter to Stop")
        end_time = time.time()
        time_elapsed = stopwatch_calculation(start_time, end_time)
        print(time_elapsed, " seconds")
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
