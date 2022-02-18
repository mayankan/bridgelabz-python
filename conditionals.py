def if_case(value):
    if value >= 0:
        return "Positive number or Zero"
    return "Out of If Block"


def if_else_case(value):
    if value >= 0:
        return "Positive number or Zero"
    else:
        return "Negative number"


def if_elif_case(value):
    if value > 0:
        return "Positive number"
    elif value == 0:
        return "Zero"
    else:
        return "Negative number"


def nested_if_case(value):
    if value >= 0:
        if value == 0:
            print("Zero")
        else:
            return "Positive number"
    else:
        return "Negative number"


def short_if_else_case(value):
    return "Positive number or Zero" if value >= 0 else "Negative number"


def number_to_day_switch_case(value):
    switcher = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }
    print(switcher.get(value, "Invalid day of the week"))


def main():
    print(if_case(5))
    print(if_else_case(-1))
    print(if_elif_case(0))
    print(nested_if_case(10))
    print(short_if_else_case(-5))
    print(number_to_day_switch_case(5))
    print(number_to_day_switch_case(20))


if __name__ == "__main__":
    main()
