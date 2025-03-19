

def basic_calculator():
     
    """ A simple calculator program that performs basic arithmetic operations. """
   
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return  # Exit the function early
            result = num1 / num2
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
            return

        print(f"{num1} {operation} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    basic_calculator()
