#Enter the Golfers score
golf_score = float(input("Please Enter the Golfers score: "))
#Make sure the score is inclusive to 18-110 inclusively
while golf_score <18 or golf_score > 110:
#Score is inclusive to 18-110 then it is valid
    print('Please Enter a valid score')
    golf_score = float(input("Please Enter the Golfers score: "))
    if golf_score == 18:
        print(f'Hole in One! ')

    while golf_score > 18 and golf_score < 74:
        print('Please Enter a valid score')
        golf_score = float(input("Please Enter the Golfers score: "))
    #a par score is 74
    if golf_score == 74:
        print(f'Achieved a PAR score')
    if golf_score == 74 - golf_score:
        print(f'Your are under par by ')





if golf_score >= 74:
    print()
    #golf_score = int(input("Please Enter the Golfers score: "))
if golf_score >=110:
    print(f'YOU ARE OVER PAR {golf_score - 74}')
    #golf_score = int(input("Please Enter the Golfers score: "))