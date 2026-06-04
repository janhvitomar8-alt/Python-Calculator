def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice: ")
    if choice == "5":
        print("Goodbye!")
        break
    elif choice == "1":
        num1=float(input("Enter the first number:"))
        num2=float(input("Enter the second number"))
        result = add(num1,num2)
        print("Answer =", result)
        break
    elif choice =="2":
        num1=float(input("Enter the first number:"))
        num2=float(input("Enter the second number"))
        result = subtract(num1,num2)
        print("Answer =", result)
        break
    elif choice =="3":
        num1=float(input("Enter the first number:"))
        num2=float(input("Enter the second number"))
        result = multiply(num1,num2)
        print("Answer =", result)
        break
    elif choice == "4":
        num1=float(input("Enter the first number:"))
        num2=float(input("Enter the second number"))
        result = divide(num1,num2)
        print("Answer =", result)
        break