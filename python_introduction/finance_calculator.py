income = int(input("Enter your monthly income: "))

mo_expenses = int(input("Enter your total monthly expenses: "))

mo_saving = income - mo_expenses

annual_interest = 0.05

projected_saving = int((mo_saving *12) + (mo_saving * 12 * 0.05))

print ("Your monthly savings are $" + str(mo_saving) + ".")

print ("Projected savings after one year, with interest, is: $" + str(projected_saving) + ".")
