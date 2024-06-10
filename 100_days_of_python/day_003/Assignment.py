# author    https://github.com/iroshanvidanage
# date      05/15/2023

def odd_or_even(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


input_number = float(input('Enter number: '))
print(odd_or_even(input_number))

##################################################

# author    https://github.com/iroshanvidanage
# date      05/15/2023

# BMI 2.0

def bmi_cal(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)


def bmi_type(bmi_val):
    if bmi_val <= 18.5:
        return 'Under Weight'
    elif bmi_val <= 25:
        return 'Normal'
    elif bmi_val <= 30:
        return 'Over Weight'
    elif bmi_val <= 35:
        return 'Obese'
    else:
        return 'Clinically Obese'


weight = float(input('Enter weight in kgs: '))
height = float(input('Enter height in meters: '))
bmi_value = bmi_cal(weight, height)
bmi_ty = bmi_type(bmi_value)
print(f'Your bmi value is {bmi_value} and your clinical status is {bmi_ty}.')


#####################################################

# author    https://github.com/iroshanvidanage
# date      05/15/2023

# Leap Year
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def leap_year2(year):
    return (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)


print(leap_year2(int(input('Enter year: '))))


#########################################################

# author    https://github.com/iroshanvidanage
# date      05/15/2023

def pizza_order():
    pizza_size = str(input('Input s, m, l: ')).upper()
    pepp = str(input('Pepperoni y / n ? ')).upper()

    if pizza_size == 'S':
        bill = 15
    elif pizza_size == 'M':
        bill = 20
    else:
        bill = 25

    if pepp == 'Y' and pizza_size == 'S':
        bill += 2
    elif pepp == 'Y' and pizza_size != 'S':
        bill += 3
    else:
        pass

    print(f'Your pizza order is {bill}.')


pizza_order()
