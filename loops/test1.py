#  code for the monthlt index vise expenses

expenases = [100, 200, 300, 400, 500]
total_expenses = 0

#  for the index we usig the range


for i in range(len(expenases)):
    expenas = expenases[i]
    print(f"month {i+1}, expenses: {expenas}")
    total_expenses += expenas  


print("Total expenses: ", total_expenses)