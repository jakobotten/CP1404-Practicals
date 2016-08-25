def main():
    number_of_months = int(input("How many months? "))
    incomes = []

    for month in range(number_of_months):
        incomes += [float(input("Enter income for month {}: ".format(month + 1)))]

    display_report(incomes)


def display_report(incomes):
    print("Income Report")
    print("-------------")
    count = 1
    total_income = 0
    for income in incomes:
        total_income += income
        print("Month  {} - Income: $ {:8.2f} Total: $ {:8.2f}".format(count, income, total_income))
        count += 1
main()
