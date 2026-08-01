#input module for calculator functions
from newmodule import add, subtract, multiply, divide, exit_program
# Example usage of the calculator functions
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
while True:
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        print("Addition: ", add(a, b))
    elif choice == '2':
        print("Subtraction: ", subtract(a, b))
    elif choice == '3':
        print("Multiplication: ", multiply(a, b))
    elif choice == '4':
        print("Division: ", divide(a, b))
    elif choice == '5':
        print("Exiting the program...")
        exit_program()
    else:
        print("Invalid choice. Please try again.")
