# author    https://github.com/iroshanvidanage
# date      05/14/2023

def digit_num(num):
    value = 0
    for _ in num:
        value += int(_)

    return value


# print(digit_num(str(input('Enter two digit number: '))))

#########################################################

two_digit_number = input('Enter two digit number: ')
# print(type(two_digit_number))
# int(two_digit_number)

try:
    int(two_digit_number)
    print(int(two_digit_number[0]) + int(two_digit_number[1]))
except ValueError as e:
    print('Enter only integer\n', e)


#########################################################

# author    https://github.com/iroshanvidanage
# date      05/14/2023

# BMI Calculator
def bmi_cal():
    weight = float(input('Enter weight in kgs: '))
    height = float(input('Enter height in meters: '))
    bmi = weight // (height ** 2)
    print(int(bmi))


bmi_cal()

#########################################################

# author    https://github.com/iroshanvidanage
# date      05/14/2023

# your life in weeks

import datetime


def life_cal(birth_day):
    today = datetime.date.today()
    b_day = datetime.date.fromisoformat(birth_day)
    date_diff = today - b_day
    days_left = 90 * 365 - date_diff.days
    years = days_left // 365
    months = (days_left - years * 365) // 30
    days = (days_left - years * 365 - months * 30)

    print(f'As of today {today}, you have {years} year(s), {months} month(s) and {days} day(s) left.')


birthday = str(input('Enter your birthday in the following format yyyy-mm-dd: '))
life_cal(birthday)
# print(datetime.date.fromisoformat(birthday))
# print(datetime.date.today())
# print(datetime.date.today()-datetime.date.fromisoformat(birthday))
