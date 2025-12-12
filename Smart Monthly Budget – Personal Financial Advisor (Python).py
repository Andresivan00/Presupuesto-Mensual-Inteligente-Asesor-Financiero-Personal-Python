"""
 ------------------------------
 Function to request integers from the user
 ------------------------------
"""
def ask_number(message: str) -> int: 
    """
    Asks the user for an integer, validating the input.
    - 'message' is the text shown to the user.
    - If the user writes something that isn't a number, asks again.
    """
    while True:  # infinite loop until a valid number is entered
        try:
            return int(input(message))  # try to convert input to integer
        except ValueError:
            print("Error: enter a valid number.")  # error message if not a number

"""
  ------------------------------
  Function to request housing type
  ------------------------------
"""

def ask_housing_type() -> str:
    """
    Requests and validates the user's housing type.
    - Only accepts 'owned' or 'rented'.
    - If something else is written, asks again.
    """
    while True:  # repeats until the user writes a correct option
        housing_type = input("Type if you have housing 'owned' or 'rented': ").lower()
        if housing_type in ["owned", "rented"]:  # check if option is valid
            return housing_type
        print("Invalid option. Try again, only type ('owned' or 'rented').")  # error message

"""
 ------------------------------
 Function that calculates monthly budget
 ------------------------------
"""
def calculate_budget(salary: int, housing: str, rent: int, bills: int, other: int, desired_savings: int):
    """
    Calculates expenses (money spent) and savings (money left over).
    - expenses = rent + bills + other
    - savings = salary - expenses
    Returns both values.
    """
    expenses = rent + bills + other
    savings = salary - expenses
    return expenses, savings  # return a tuple (two values)

"""
  ------------------------------
  Function that shows results to the user
  ------------------------------
"""
def show_results(expenses: int, savings: int, desired_savings: int, other: int, bills: int):
    """
    Displays the budget summary on screen and gives recommendations.
    - Prints expenses and savings.
    - Gives advice depending on expenses and desired savings.
    """
    print(f"\nYour monthly expenses are: {expenses}")
    print(f"Your monthly savings are: {savings}")

    # If entertainment and food expenses are greater than or equal to bills, gives a warning.
    if other >= bills:
        print("⚠ Your spending on other services is very high, you should try going to the movies less😛")
    
    # If desired savings are greater than actual savings, recommends adjusting expenses.
    if desired_savings > savings:
        print("⚠ You need to take measures to reach your desired savings, you can start by eliminating small unnecessary expenses.")
    else:
        print("✅ Well done, your goals have been achieved🤩")


"""
  ------------------------------
  Main function (program entry point)
  ------------------------------

"""
def main():
    """
    Orchestrates the program:
    1. Asks the user for salary and expenses.
    2. Calculates budget.
    3. Shows results and recommendations.
    """
    print(" Financial algorithm for monthly budget ")

    salary = ask_number("Enter your monthly salary: ")
    housing = ask_housing_type()
    # If housing is rented, asks for rent; if not, value is 0.
    rent = ask_number("Enter your rent expense: ") if housing == "rented" else 0
    bills = ask_number("Enter average expenses for services: ")
    other = ask_number("Enter average for other services (food, entertainment): ")
    desired_savings = ask_number("Enter how much you want to save per month: ")

    # Calculate expenses and savings using the function
    expenses, savings = calculate_budget(salary, housing, rent, bills, other, desired_savings)
    
    # Show results
    show_results(expenses, savings, desired_savings, other, bills)


"""
  ------------------------------
  This ensures the program runs only if executed directly
  and not when imported as a module in another program.
  ------------------------------

"""
if __name__ == "__main__":
    main()
