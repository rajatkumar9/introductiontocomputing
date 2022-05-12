#QUESTION 1

import math
n = int(input('Enter a number'))
print(f'Binary equivalent of {n} is',bin(n)[2:])


#QUESTION 2

# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y

# This function gives exponent value
def exponent(x,y):
    return x**y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.exponent")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4','5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            print(num1, "^", num2, "=", exponent(num1, num2))


        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")


#QUESTION 3

print("(3+4)*5 is",(3+4)*5)

n=int(input("enter value of n :"))
print(n*(n-1)/2)

r=int(input("enter value of r :"))
print(4*math.pi*(r**2))

a=int(input("enter value of angle 1 (a):"))
b=int(input("enter value of angle 2 (b) :"))
print(((r*(math.cos(a))**2)+(r*(math.sin(b))**2))**(1/2))

#QUESTION 4

print("numbersin range(5)")
for i in range(5):
    print(i)

print("numbersin range(3,10)")
for i in range(3,10):
    print(i)

print("numbersin range(4,13,3)")
for i in range(4,13,3):
    print(i)


print("numbersin range(15,5,-2)")
for i in range(15,5,-2):
    print(i)

print("numbersin range(5,3)")
for i in range(5,3):
    print(i)


#QUESTION 5



Number_of_carbon=int(input("Enter number of carbon:"))
Number_of_hydrogen=int(input("Enter number of hydrogen:"))
Number_of_oxygen=int(input("Enter number of oxygen:"))

print("molecular weight of compound in grams per mole=",(Number_of_oxygen*15.9994)+(Number_of_hydrogen*1.00794)+(Number_of_carbon*12.0107))

