#  making the cousinn checker using conditions

indian = ["samosa", "daal", "naan"]
chinese = ["egg role", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]



dish = input("input the dish you want :")

if dish in indian:
    print(f"{dish} if indian")
elif dish in chinese:
    print(f"{dish} is chinese")
elif dish in italian:
    print(f"{dish} is italian")
else:
    print("i dont know which cuisine is this")

#  making the cousinn checker using conditions