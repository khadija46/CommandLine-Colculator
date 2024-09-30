# Define a calculator function that takes two numbers and an operator as input
def calculator(a, b, opt):
    # Perform addition if the operator is '+'
    if opt == '+':
       return a + b
    # Perform subtraction if the operator is '-'
    elif opt == '-':
        return a - b
    # Perform multiplication if the operator is '*'
    elif opt == '*':
        return a * b
    # Perform division if the operator is '/'
    elif opt == '/':
        if b == 0:  # Check for division by zero
            try:
                return a / b
            except ZeroDivisionError:  # Handle ZeroDivisionError
                print("\n Error! Cannot divide by zero.")

# Print the calculator's functions and a message on how to quit
print ("Simple Command-Line Calculator\n")
print ("Functions \n\t 1. Addition\n\t 2. Subtraction "
       "\n\t 3. Multiplication \n\t 4. Division")
print ("\n Enter 'q' to quit")

# Start an infinite loop to continuously ask for user input
while True:       
    # Prompt the user for input and remove leading/trailing spaces
    input_expression = input("\n Enter an expression (i.e., 2 + 2): ").strip()

    # If the user inputs 'q', break the loop and quit the calculator
    if input_expression.lower() == 'q':
        break
    
    try:
        # Split the input into three parts: operand1, operator, and operand2
        operand1, operator, operand2 = input_expression.split()
        # Convert the operands from strings to floats
        operand1 = float(operand1)
        operand2 = float(operand2)

        # Check if the operator is one of the valid operations
        if operator == '+' or operator == '-' or operator == '*' or operator == '/':
            # Call the calculator function and get the result
            result = calculator(operand1, operand2, operator)
            # Display the result of the calculation
            print(f"\n Result \n\t {input_expression} = {result}")
            print("-----------------------------------")
        else:
            # If the operator is invalid, display an error message
            print("Incorrect operator or expression!")
    
    except:
        # Handle any errors (e.g., if the input is not in the correct format)
        print("\n ValueError: Enter expression in correct format i.e., 2 + 2.")
