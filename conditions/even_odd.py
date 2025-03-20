#  even odd in py

#  start with the input methods

#  in input you can get stinrg you cnat perform any operation on string
#  so you have to convert it into integer


m = input('enter a number')
print(m)
m = int(m)



if m % 2 ==0:
    print('even')
else:
    print('odd')


#  ternary Operator :-

message = "number is evenr" if m % 2 == 0 else "number is odd"
print(message)