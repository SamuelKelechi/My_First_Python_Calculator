# A simple Calculator Program Designed By Samuel, A Product of BrighterDays Codelab

# This function will add two numbers
def add(a, b):
    return a + b

# This function will subtract two numbers
def sub(a, b):
    return a - b

# This function will multiply two numbers
def mul(a, b):
    return a * b

# This function will divide two numbers
def div(a, b):
    return a / b

# A Welcome Display to the Screen
print("Welcome to Samuel's Program")

# This allows User to Input his/her name
name = input("Please Input Your Name:")

# This Prints Out Welcome and the name of the user as inputed
print("Welcome", name)

# This Show Options that the user can pick from
print("Select Operator Choice")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # This will take input from the User
    choice = input("Enter Operator Choice (1/2/3/4): ")

    #This will check if Choice is one of the four options
    if choice in (1, 2, 3, 4):
        FirstNumber = float(input("Enter First Number: "))
        SecondNumber = float(input("Enter First Number: "))

        if choice == 1:
            print(FirstNumber, "+" , SecondNumber, "=", add(FirstNumber, SecondNumber))

        elif choice == 2:
            print(FirstNumber, "-", SecondNumber, "=", sub(FirstNumber, SecondNumber))

        elif choice == 3:
            print(FirstNumber, "*", SecondNumber, "=", mul(FirstNumber, SecondNumber))

        elif choice == 4:
            print(FirstNumber, "/", SecondNumber, "=", div(FirstNumber, SecondNumber))

        else:
            print("Invalid Selection")
