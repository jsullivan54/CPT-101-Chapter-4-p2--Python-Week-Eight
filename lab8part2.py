#Johnathan Sullivan AKA Bruce Wayne_Jung
#Monthly Budget Tracker lab8part2
#October, 20th, 2024

#Named Constants
print()
print('Hello Master Wayne_Jung. Lets create a budget of some expenses for Wayne_Jung Enterprises  ')
print()
MONTHLY_BUDGET = 'Please enter your monthly budget (in USD): '
EXPENSE = 'Enter an expense (enter 0 to end): '
EXPENSES_SUMMARY = 'Your total expenses are: $ '
BUDGET_SUMMARY = 'Your budget is: $ '
OVER_BUDGET = 'You are over your budget by: $ '
IN_BUDGET = 'You are within your budget by: $ '

# Variable
# Monthly Budget
monthly_budget = 0.0

#Total Expenses
total_expenses = 0.0

# Get the monthly budget from the user
monthly_budget = float(input(MONTHLY_BUDGET))

# Input
#Non zero
expense = -1.0
#Loop/Sentinel
while expense != 0:
    #enter an expense
    expense = float(input(EXPENSE))
    #If not 0 then add to the total
    if expense != 0:
        total_expenses = total_expenses + expense

# Display the results
print(f'{BUDGET_SUMMARY}{monthly_budget:.2f}')
print(f'{EXPENSES_SUMMARY}{total_expenses:.2f}')

# Compare total expenses to the budget and display the appropriate message
if total_expenses > monthly_budget:
    over_budget = total_expenses - monthly_budget
    print(f'{OVER_BUDGET}{over_budget:.2f}')
else:
    within_budget = monthly_budget - total_expenses
    print(f'{IN_BUDGET}{within_budget:.2f}')

#END OF LAB8PART2 CODE


#My Ending Signature 
#The original Batman logo program that I use in multiple project endings was created by Carl Mascarenhas (aka carlmas02), 
# Their GitHub page can be located at https://gist.github.com/carlmas02/a0bb1614b61374cab3487d6dce8f9f7b
import turtle

# Function to draw the Batman logo
def draw_batman_logo():
    # Initialize the turtle for Batman logo
    bat = turtle.Turtle()
    bat.turtlesize(1, 1, 1)
    bat.pensize(3)

    # Screen information
    wn = turtle.Screen()
    wn.bgcolor("black")  # Change background to black
    wn.title("BATMAN")

    # Set the color for the turtle (pen and fill)
    bat.color("yellow", "black")

    # Begin filling color for Batman logo
    bat.begin_fill()

    # Drawing the left side of the Batman logo
    bat.left(90)               # Turn pointer direction to left 90 degrees
    bat.circle(50, 85)         # Draw an arc with radius 50 and extent 85 degrees
    bat.circle(15, 110)        # Draw a smaller arc
    bat.right(180)             # Turn around

    # Drawing the bottom left wing
    bat.circle(30, 150)        # Draw another arc
    bat.right(5)
    bat.forward(10)            # Draw forward line of 10 units

    # Drawing the bottom middle part
    bat.right(90)
    bat.circle(-70, 140)
    bat.forward(40)
    bat.right(110)

    # Drawing the right wing
    bat.circle(100, 30)
    bat.circle(30, 100)
    bat.left(50)
    bat.forward(50)
    bat.right(145)

    # Draw the inner part of the right wing
    bat.forward(30)
    bat.left(55)
    bat.forward(10)

    # Reverse path to draw the left wing
    bat.forward(10)
    bat.left(55)
    bat.forward(30)

    # Continue drawing the right wing
    bat.right(145)
    bat.forward(50)
    bat.left(50)
    bat.circle(30, 100)
    bat.circle(100, 30)

    # Drawing the bottom right part
    bat.right(90)
    bat.right(20)
    bat.forward(40)
    bat.circle(-70, 140)

    # Finalizing the logo
    bat.right(90)
    bat.forward(10)
    bat.right(5)
    bat.circle(30, 150)

    # Complete the logo
    bat.left(180)
    bat.circle(15, 110)
    bat.circle(50, 85)

    # End color filling for Batman logo
    bat.end_fill()

    # Move to the position for the heart
    bat.penup()
    bat.goto(0, -150)  # Adjust position for heart
    bat.setheading(0)   # Set heading to face the same direction as the bat logo
    bat.pendown()

    # Draw a smaller heart shape
    bat.color("red", "red")  # Set color for heart
    bat.begin_fill()

    # Drawing the heart
    bat.left(140)            # Angle for the heart
    bat.forward(112)         # Draw left side of heart
    bat.circle(-56, 200)     # Draw left arc of heart
    bat.left(120)            # Angle for the right side
    bat.circle(-56, 200)     # Draw right arc of heart
    bat.forward(112)         # Draw right side of heart

    bat.end_fill()

    # Write text below the heart
    bat.penup()
    bat.goto(0, -210)  # Move below the heart
    bat.color("white")  # Set color for text
    bat.write("Bruce Wayne _Jung Was Here!", align="center", font=("Arial", 16, "bold"))

    bat.penup()
    bat.goto(0, -250)  # Move below the heart
    bat.color("white")  # Set color for text
    bat.write("Lucia Fox saved my company!", align="center", font=("Arial", 14, "bold"))

    # Move the pen away from the text at the end
    bat.goto(0, -260)  # Move the turtle down to avoid overlap with the text

    # Finish the turtle graphics
    turtle.done()

# Call the function to draw the Batman logo and heart
draw_batman_logo()



#Works Cited: 
#The original Batman logo program that I use in multiple project endings was created by Carl Mascarenhas (aka carlmas02), 
# Their GitHub page can be located at https://gist.github.com/carlmas02/a0bb1614b61374cab3487d6dce8f9f7b
