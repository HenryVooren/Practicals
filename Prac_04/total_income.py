"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
update to commit to prac_05 feedback
"""


def report_income(num_months, incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = float(input("Enter income for month {:2.0f}: ".format(month)))
        incomes.append(income)

    report_income(num_months, incomes)


main()
