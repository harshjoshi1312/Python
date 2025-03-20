#  using for loop sum of the all list item 
#  for checking the monthly expenses


expenases = [100, 200, 300, 400, 500]

# for expens in expenases:
#     print(expens)

#  this givses the individually all the expenses

totalexpense = 0

for expense in expenases:
    totalexpense = totalexpense + expense

print("Total expenses: ", totalexpense)