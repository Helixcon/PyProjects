def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero.")

def calculator():
    print("Welcome to the Command-Line Calculator!")
    print("Enter 'exit' to quit.")
    
    while True:
        try:
            # Read input from the user
            expression = input("Enter an expression (e.g., 2 + 3): ")
            
            # Check for exit command
            if expression.lower() == 'exit':
                print("Exiting the calculator.")
                break

            # Evaluate the expression
            result = eval(expression)

            print("Result:", result)
        
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    calculator()
