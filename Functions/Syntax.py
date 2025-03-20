# A function allows you to perform a specific piece of work.
# It helps in reusing your code efficiently.


harsh_expense = [30,40,70,90]
ayushi_expense = [40,50,70,90]


def find_totalexpenses(expenses):
    '''
    :params = input containing numners
    :return = total numbers
    '''
    total = 0;
    for expense in expenses:
        total += expense

    return total


totalharshexpense = find_totalexpenses(harsh_expense)
print(totalharshexpense)

totalayushiexpense = find_totalexpenses(ayushi_expense)
print(totalayushiexpense)

#  function facts 

#  1 - arguments is not nessasary
#  2 - return statemnet is not