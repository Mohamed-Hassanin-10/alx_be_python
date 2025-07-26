monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

annual_interest = 0.05
projected_saving = int((monthly_savings * 12) + (monthly_savings * 12 * annual_interest))

print("Your monthly savings are $" + str(monthly_savings) + ".")
print("Projected savings after one year, with interest, is: $" + str(projected_saving) + ".")

