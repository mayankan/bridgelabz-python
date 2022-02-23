import datetime


class Util:
    @staticmethod
    def day_of_week(year, month, day):
        """
        Returns the day of week derived using the day, month and year given by the user.
        :param year: Year in which day arises provided by the user.
        :param month: Month in which day arises provided by the user.
        :param day: Day in the month provided by the user.
        :return: Day starting from 0 in the week calculated using Gregorian calendar.
        """
        try:
            # Converting the inputs into a date format.
            date1 = datetime.date(month, day, year)
            y = date1.year
            m = date1.month
            d = date1.day

            # Using the following formulas, for the Gregorian calendar.
            y0 = y - (14 - m) // 12
            x = y0 + (y0 // 4) - (y0 // 100) + (y0 // 400)
            m1 = m + 12 * ((14 - m) // 12) - 2
            d0 = (d + x + (31 * m1) // 12) % 7

            # Creating a dictionary to print out the day in the week.
            day_dict = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
            return day_dict[d0]
        except Exception as e:
            print("{} is raised.".format(str(e)))


def main():
    try:
        year = int(input('Enter a year: '))
        month = int(input('Enter a month: '))
        day = int(input('Enter a day: '))

        day_instance = Util()
        day_of_the_week = day_instance.day_of_week(month, day, year)
        print(day_of_the_week)
    except Exception as e:
        print("{} is raised.".format(str(e)))


if __name__ == "__main__":
    main()
