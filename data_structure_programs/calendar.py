import sys


# import sys
class Calendar:
    def beg_week_of_month(self, month_find, year_find):
        d = int(1)
        m = int(month_find)
        y = int(year_find)
        try:
            if (m in range(1, 13)) and (y > 0):
                y0 = y - ((14 - m) / 12)
                x = y0 + (y0 / 4) - (y0 / 100) + (y0 / 400)
                m0 = m + 12 * ((14 - m) / 12) - 2
                d0 = (d + x + ((31 * m0) / 12)) % 7
                d0 = int(d0)
                return d0
        except:
            print("Error in the month or year !!!!")

    def leap_year_find(self, year):
        if year in range(1000, 10000):
            if year % 400 == 0:
                return True
            elif (year % 4 == 0) and (year % 100 != 0):
                return True
            else:
                return False

    def month_days(self, month, year):
        mon = month
        if mon == 2:
            is_leap = Utility.leap_year_find(year)
            if is_leap:
                return 29
            else:
                return 28
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        else:
            return 30

    def find_beg_day_ofmonth(self, month, year):
        week_day = self.beg_week_of_month(month, year)
        return week_day

    def num_of_days(self, month, year):
        days_in_month = self.month_days(month, year)
        return days_in_month

    def calendar_print(self, month, year, week_day, days_in_month):
        """ Function to print the calendar """
        print("\nPython cal", month, year)
        print("\r")
        number_of_days = days_in_month
        start_day = week_day
        day_lis = []
        print("S  M  T  W  Th  F  S")
        print("\r")
        new_line = [6, 13, 20, 27, 34]
        for i in range(start_day):
            day_lis.append("  ")
        for k in range(1, number_of_days + 1):
            day_lis.append(k)
        for index, j in enumerate(day_lis):
            if j == "  ":
                pass
            else:
                if int(j) < 10:
                    print("", end=" ")
            print(j, end=" ")
            if index in new_line:
                print("\r")
                print("  ")
            if index == len(day_lis) - 1:
                print("\n")


def main():
    calendar = Calendar()
    month = int(sys.argv[1])  # getting the month and year values from th commandline
    year = int(sys.argv[2])
    week_day = calendar.find_beg_day_ofmonth(month, year)
    print(week_day)
    days_in_month = calendar.num_of_days(month, year)
    calendar.calendar_print(month, year, week_day, days_in_month)


if __name__ == "__main__":
    main()
