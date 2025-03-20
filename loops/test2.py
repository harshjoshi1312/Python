#  inumareator expnese

expeses = [10.50, 8, 5, 15, 20, 5, 3]
total = 0


for i , expense in enumerate(expeses):
    total += expense
    print(f"Month: {i+1}, expenses: {expense}, total: {total}")