def complete_task(deadline, completion_time, no_of_tasks):
    """
    Returns the difference between completion time and deadline in descending order.
    :param deadline: Deadline integer values given in list provided by the user.
    :param completion_time: Completion Time integer values given in list provided by the user.
    :param no_of_tasks: Number of tasks for which deadline and completion time is provided by the user.
    :return: difference between completion time and deadline in descending order.
    """
    time_difference = []
    for task in range(no_of_tasks):
        time_difference.append(int(completion_time[task]) - int(deadline[task]))
    time_difference.sort(reverse=True)
    return time_difference


def main():
    no_of_tasks = int(input("Enter the number of tasks to complete: "))
    deadline = []
    completion_time = []
    for task in range(no_of_tasks):
        input_line = input("Enter deadline and completion time for the task {}: ".format(task+1))
        deadline.append(input_line.split(" ")[0])
        completion_time.append(input_line.split(" ")[1])
    time_difference = complete_task(deadline, completion_time, no_of_tasks)
    for diff in time_difference:
        print(diff)


if __name__ == "__main__":
    main()
