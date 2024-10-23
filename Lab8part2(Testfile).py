# Author: Your Name
# Program: Monthly Budget Tracker
# Description: This program tracks monthly expenses against a user-defined budget.
# The user can enter expenses until they choose to exit by entering zero.

# Constants
BUDGET_PROMPT = "Please enter your monthly budget: "
EXPENSE_PROMPT = "Enter an expense (enter 0 to finish): "
EXPENSES_SUMMARY = "Your total expenses are: $"
BUDGET_SUMMARY = "Your budget is: $"
OVER_BUDGET = "You are over your budget by: $"
WITHIN_BUDGET = "You are within your budget by: $"

# Variable initialization
monthly_budget = 0.0  # User's monthly budget
total_expenses = 0.0  # Sum of all expenses entered

# Get the monthly budget from the user
monthly_budget = float(input(BUDGET_PROMPT))

# Input loop for expenses
expense = -1.0  # Initialize expense to a non-zero value
while expense != 0:  # Loop until user enters zero
    expense = float(input(EXPENSE_PROMPT))  # Get an expense from the user
    if expense != 0:  # Only add to total if the expense is not zero
        total_expenses += expense  # Add the expense to the total

# Display the results using f-strings
print(f"{BUDGET_SUMMARY}{monthly_budget:.2f}.")
print(f"{EXPENSES_SUMMARY}{total_expenses:.2f}.")

# Compare total expenses to the budget and display the appropriate message
if total_expenses > monthly_budget:
    over_budget = total_expenses - monthly_budget
    print(f"{OVER_BUDGET}{over_budget:.2f}.")
else:
    within_budget = monthly_budget - total_expenses
    print(f"{WITHIN_BUDGET}{within_budget:.2f}.")
