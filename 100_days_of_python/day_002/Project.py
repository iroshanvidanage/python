# author    https://github.com/iroshanvidanage
# date      05/15/2023

def tip_cal(tot_bill, pct, ppl):
    return round((tot_bill * (100 + pct)) / (ppl * 100), 2)


bill = float(input('What was the total bill? '))
tip_per = float(input('What percentage tip would you like to give? 10, 12 or 15? '))
people = int(input('How many people to split the bill? '))

print(tip_cal(tot_bill=bill, pct=tip_per, ppl=people))
