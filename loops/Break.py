#  the break statmenet in the fore loop:-


monthly_sales = [42 , 38 , 33 , 38 , 40 , 41 , 42 ]
months= ['jan','feb','mar','apr','may','jun','july']

thresold = 35


# i have to fid where i hit the sales taget

for slaes_amount,month  in zip(monthly_sales, months):
    # print(month , slaes_amount)
    if slaes_amount < thresold:
      print(f"slaes_amount {slaes_amount} is below the thresold in {month}")
      break
    else:
        print(f"slaes_amount {slaes_amount} is above the thresold in {month}")



#  the mian pillar of any language is the loops and the conditions