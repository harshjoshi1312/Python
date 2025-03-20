def sum_all(*args):
    total = 0
    print(args)
    for num in args:
        total += num
    return total

total = sum_all(1,2,3,4,5,6,7,8)
print(total)




# *args = multiple functional args 
# **kwargs = key value args