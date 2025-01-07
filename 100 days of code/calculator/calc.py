from art import logo

# Display the logo (if the art module is available)
print(logo)


# Define arithmetic functions
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2


# Dictionary to map operators to functions
operation_dic = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}


# Calculator function
def calc(a, b, sym):
    # Check if the operator is valid
    if sym in operation_dic:
        result = operation_dic[sym](a, b)
        print(f"The result of {a} {sym} {b} is: {result}")
        return result
    else:
        print("Invalid operator. Please try again.")
        return None


# Main program
def calculator():
    print("Welcome to the Calculator!")

    # Take the first number input
    a = int(input("Enter the first number: "))

    while True:
        # Ask for the operator and the second number
        sym = input("Select the operation (+, -, *, /): ")
        b = int(input("Enter the next number: "))

        # Perform calculation
        result = calc(a, b, sym)

        if result is not None:
            # Allow chaining calculations
            a = result

        # Check if the user wants to continue or exit
        con = input("Do you want to continue? Type 'Y' to continue or 'N' to exit: ").upper()
        if con != 'Y':
            print("Goodbye!")
            break


# Run the calculator
calculator()
