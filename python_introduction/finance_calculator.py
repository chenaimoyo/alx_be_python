mincome = int(input("Enter your monthly income: "))
mexpenses = int(input("Enter your monthly expenses: "))

monthly_savings =float(mincome) - float(mexpenses)
ProjectedSavings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
ProjectedSavings = int(ProjectedSavings)

print(f"Enter your monthly income: {mincome}")
print(f"Enter your total monthly expenses: {mexpenses}")
print(f"Your monthly savings are ${int(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${ProjectedSavings}.")
