mincome = int(input("Enter your monthly income: "))
mexpenses = int(input("Enter your monthly expenses: "))

savings = mincome - mexpenses
ProjectedSavings = savings * 12 + (savings * 12 * 0.05)

print(f"Enter your monthly income: {mincome}")
print(f"Enter your total monthly expenses: {mexpenses}")
print(f"Your monthly savings are ${savings}")
print(f"Projected savings after one year, with interest, is: ${ProjectedSavings}")
