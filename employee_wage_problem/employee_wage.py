# Packages
import random


# Constants
WAGE_PER_HR = 20
FULL_DAY_HR = 8
PART_TIME_HR = 6
WORKING_DAY_PER_MONTH = 20
TOTAL_WORKING_HRS = 100


# Case 1 : print daily wage
print('Welcome')
attendance = random.randint(0, 2)

print(f'Attendance {attendance}')

wage_per_day = WAGE_PER_HR * FULL_DAY_HR
print('Wage per day {}'.format(wage_per_day))

part_time_wage_per_day = PART_TIME_HR * WAGE_PER_HR
print('Part time wage per day {0}'.format(part_time_wage_per_day))

_wage = [
    {'attendance': 'absent', 'wage': 0, 'worked_hr': 0},
    {'attendance': 'present', 'wage': wage_per_day, 'worked_hr': FULL_DAY_HR},
    {'attendance': 'part-time', 'wage': part_time_wage_per_day, 'worked_hr': PART_TIME_HR}
]


# print('Wage according to attendance :', _wage.get(attendance))
#
# day_count = 0
# total_wage = 0
# worked_hrs = 0
#
#
# while WORKING_DAY_PER_MONTH > day_count:
#     attendance = random.randint(0, 2)
#     day_count += 1
#     __wage = _wage.get(attendance).get('wage')
#     total_wage += __wage
#     worked_hrs += _wage.get(attendance).get('worked_hr')
#     if worked_hrs > TOTAL_WORKING_HRS:
#         break
#
#
# print('Working day per month {}'.format(total_wage))
# print('Worked hr per month {}'.format(worked_hrs))
# print('Worked for {}'.format(day_count))


def get_total_worked_hrs_data():
    worked_hrs = 0
    day_count = 0
    total_wage = 0
    daily_wage = {}

    while WORKING_DAY_PER_MONTH > day_count:
        attendance = random.randint(0, 2)
        temp = _wage[attendance]['attendance']
        worked_hrs += _wage[attendance]['worked_hr']
        __wage = _wage[attendance]['wage']
        total_wage += __wage
        day_count += 1
        _wage[attendance]['day'] = day_count
        daily_wage[day_count] = __wage

    return total_wage, daily_wage


_total_wage, _daily_wage = get_total_worked_hrs_data()
print('Total wage: ', _total_wage)
print('Daily wage : ', _daily_wage)
