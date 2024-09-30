**Simple Command-Line Calculator**
**Description**
This project is a simple Python-based command-line calculator designed to perform basic arithmetic operations: addition, subtraction, multiplication, and division. The program prompts the user to input an expression, processes the input, and returns the result. It runs in a loop, allowing users to perform multiple calculations without restarting the program, and includes error handling for invalid inputs and division by zero.

**Features**
Addition: Add two numbers (e.g., 2 + 2).
Subtraction: Subtract one number from another (e.g., 5 - 3).
Multiplication: Multiply two numbers (e.g., 4 * 5).
Division: Divide one number by another (e.g., 10 / 2). Handles division by zero with an error message.
Continuous Input: The calculator accepts multiple expressions in a loop until the user decides to exit.
Error Handling: Checks for input format errors and invalid operators. Provides appropriate feedback when an invalid input is entered.

**How to Use**
Clone or download the repository to your local machine.
Run the script in a terminal or command-line environment:

**Copy code**
python calculator.py
Input expressions in the following format:
<number1> <operator> <number2>
Example: 2 + 2
Supported operators:
Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
To quit the calculator, type q and press Enter.

Simple Command-Line Calculator
Functions 
    1. Addition
    2. Subtraction 
    3. Multiplication 
    4. Division

Enter 'q' to quit

Enter an expression (i.e., 2 + 2): 10 / 2
Result
    10 / 2 = 5.0
-----------------------------------
**Error Handling**
Invalid Input: If the user enters an invalid expression or operator, the calculator will display an error message and prompt the user to try again.
Example error message: ValueError: Enter expression in correct format i.e., 2 + 2.
Division by Zero: When attempting to divide by zero, the program catches the error and displays: Error! Cannot divide by zero.

**Requirements**
Python 3.x (Tested with Python 3.x)

**To Do**
Add more complex operations (e.g., exponentiation, modulus).
Implement support for parentheses to allow more advanced expressions.
