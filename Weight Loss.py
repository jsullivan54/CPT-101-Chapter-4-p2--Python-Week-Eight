

#Monthly Loss
monthly_loss= 4 #lbs
#calorie_reduction=
weight = int(input('Please Enter Your weight in lbs: '))
for month in range (1,7):
    weight = weight - monthly_loss
    print(f'current weight at end of {month} is: {weight}:')
