# Author: Your Name
# Program: Monthly Budget Tracker
# Description: This program tracks monthly expenses against a user-defined budget.
# The user can enter expenses until they choose to exit by entering zero.
# It supports multiple sessions and handles invalid inputs gracefully.

def get_monthly_budget():
    """Prompt user for their monthly budget and return it."""
    while True:
        try:
            budget = float(input("Please enter your monthly budget: "))
            if budget < 0:
                print("Budget cannot be negative. Please try again.")
            else:
                return budget
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_expense():
    """Prompt user for an expense and return it."""
    while True:
        try:
            expense = float(input("Enter an expense (enter 0 to finish): "))
            return expense
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def track_expenses(monthly_budget):
    """Track expenses against the given budget."""
    total_expenses = 0.0  # Sum of all expenses entered

    while True:
        expense = get_expense()  # Get an expense from the user
        if expense == 0:  # Sentinel value to exit the loop
            break
        if expense < 0:
            print("Expense cannot be negative. Please enter a valid expense.")
        else:
            total_expenses += expense  # Add the expense to the total

    # Display the results
    print(f"Your budget is: ${monthly_budget:.2f}.")
    print(f"Your total expenses are: ${total_expenses:.2f}.")

    # Compare total expenses to the budget and display the appropriate message
    if total_expenses > monthly_budget:
        over_budget = total_expenses - monthly_budget
        print(f"You are over your budget by: ${over_budget:.2f}.")
    else:
        within_budget = monthly_budget - total_expenses
        print(f"You are within your budget by: ${within_budget:.2f}.")


def main():
    """Main function to run the budget tracker."""
    print("Welcome to the Monthly Budget Tracker!")
    while True:
        monthly_budget = get_monthly_budget()  # Get budget
        track_expenses(monthly_budget)  # Track expenses

        again = input("Would you like to track another budget? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the Monthly Budget Tracker!")
            break


if __name__ == "__main__":
    main()
