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
    bat.write("Here's Johnny!", align="center", font=("Arial", 14, "bold"))

    # Move the pen away from the text at the end
    bat.goto(0, -260)  # Move the turtle down to avoid overlap with the text

    # Finish the turtle graphics
    turtle.done()

# Call the function to draw the Batman logo and heart
draw_batman_logo()
