# author    https://github.com/iroshanvidanage
# date      06/27/2024


def calculate_tax(annual_salary_before):
    # Define the tax rate slabs
    slabs = [
        (0, 1_200_000, 0),
        (1_200_000, 1_700_000, 6),
        (1_700_000, 2_200_000, 12),
        (2_200_000, 2_700_000, 18),
        (2_700_000, 3_200_000, 24),
        (3_200_000, 3_700_000, 30),
        (3_700_000, float('inf'), 36)
    ]

    # Calculate tax based on slabs
    tax = 0
    for slab in slabs:
        lower_limit, upper_limit, rate = slab
        if annual_salary_before <= lower_limit:
            break
        taxable_amount = min(upper_limit, annual_salary_before) - lower_limit
        tax += (taxable_amount / 12) * (rate / 100)

    return tax


# these cal calculations are wrong
def reverse_calculate_salary(paye_monthly_tax):
    # Define the tax rate slabs (same as in the original function)
    slabs = [
        (0, 1_200_000, 0),
        (1_200_000, 1_700_000, 6),
        (1_700_000, 2_200_000, 12),
        (2_200_000, 2_700_000, 18),
        (2_700_000, 3_200_000, 24),
        (3_200_000, 3_700_000, 30),
        (3_700_000, float('inf'), 36)
    ]

    # Initialize annual salary
    annual_salary_revs = 0
    taxable_amount = 0

    # Calculate annual salary based on tax
    for slab in slabs:
        lower_limit, upper_limit, rate = slab
        if rate != 0:
            taxable_amount = (paye_monthly_tax * 12) / (rate / 100)
        annual_salary_revs += min(upper_limit, taxable_amount + lower_limit)

    return annual_salary_revs


# these calculations are wrong
def reverse_calculate_gross_salary(net_monthly_salary):
    # Define the tax rate slabs (same as in the original function)
    slabs = [
        (0, 1_200_000, 0),
        (1_200_000, 1_700_000, 6),
        (1_700_000, 2_200_000, 12),
        (2_200_000, 2_700_000, 18),
        (2_700_000, 3_200_000, 24),
        (3_200_000, 3_700_000, 30),
        (3_700_000, float('inf'), 36)
    ]

    # Initialize annual salary
    gross_annual_salary = 0
    taxable_amount = 0

    # Calculate annual salary based on net monthly salary
    for slab in slabs:
        lower_limit, upper_limit, rate = slab
        if rate != 0:
            taxable_amount = (net_monthly_salary * 12) / (rate / 100)
        gross_annual_salary += min(upper_limit, taxable_amount + lower_limit)

    return gross_annual_salary


# Example usage
monthly_salary = 550000
annual_salary = monthly_salary * 12  # Replace with the actual annual salary
monthly_tax = calculate_tax(annual_salary)
deducted_salary = monthly_salary - monthly_tax - 25
net_salary = deducted_salary - monthly_salary * 0.04
print(f"Monthly tax for an annual salary of {annual_salary} is: {monthly_tax:.2f}")
print(f"Net salary is {net_salary}")


# Example usage:
# monthly_tax_amount = monthly_tax  # Replace with the desired monthly tax amount
# annual_salary_result = reverse_calculate_salary(monthly_tax_amount)
# print(f"Annual salary corresponding to {monthly_tax_amount:.2f} monthly tax: {annual_salary_result:.2f}")
# print(f"Monthly salary corresponding to {monthly_tax_amount:.2f} monthly tax: {annual_salary_result/12:.2f}")
#
#
# Example usage:
# net_monthly_salary_amount = monthly_salary - monthly_tax  # Replace with the desired net monthly salary
# gross_salary_result = reverse_calculate_gross_salary(net_monthly_salary_amount)
# print(
#     f"Gross annual salary corresponding to {net_monthly_salary_amount:.2f} "
#     f"net monthly salary: {gross_salary_result:.2f}")
