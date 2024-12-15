monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

monthly_savings =float(monthly_income) - float(monthly_expenses)
ProjectedSavings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
ProjectedSavings = int(ProjectedSavings)

print(f"Enter your monthly income: {monthly_income}")
print(f"Enter your total monthly expenses: {monthly_expenses}")
print(f"Your monthly savings are ${int(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${ProjectedSavings}.")
