# Enter the Golfer's score
golf_score = int(input("Please Enter the Golfer's score (between 18 and 110): "))

# Ensure the score is within the valid range using one while statement
while golf_score < 18 or golf_score > 110:
    print('Invalid score. Please enter a valid score between 18 and 110.')
    golf_score = int(input("Please Enter the Golfer's score: "))

# Check the golfer's performance against par
if golf_score == 74:
    print('Achieved a PAR score')

if golf_score < 74:
    print(f'YOU ARE UNDER PAR by {74 - golf_score} strokes')

else:
    print(f'YOU ARE OVER PAR by {golf_score - 74} strokes')
