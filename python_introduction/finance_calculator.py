income = float(input("Enter your income: "))

mo_expenses = float(input("Enter your total monthly expenses: "))

mo_saving = income - mo_expenses

annual_interset = 0.05

projected_saving = (mo_saving *12) + (mo_saving * 12 * 0.05)

print ("Your monthly savings are $" + str(mo_saving))

print ("Projected savings after one year, with interest, is: $" + str(projected_saving))
