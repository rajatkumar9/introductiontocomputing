#QUESTION 1
Marks=int(input("Enter your marks : "))
if Marks<25:
    print("Your grade is F")
elif Marks in range(25,46):
    print("Your grade is E")
elif Marks in range(45,51):
    print("Your grade is D")
elif Marks in range(50,61):
    print("Your grade is C")
elif Marks in range(60,81):
    print("Your grade is B")
elif Marks>80:
    print("Your grade is A")

#QUESTION 2
Year=int(input("Enter a Year :"))

if (Year % 4 ==0):
    print("The entered year is a leap year")
else:
    print("It is not a leap year")

#QUESTION 3

from random import randint

for i in range(1, 11):
    n1 = randint(1, 10)
    n2 = randint(1, 10)

    print("Q" + str(i) + " is: " + str(n1) + "x" + str(n2) + " = ")
    answer = int(input())
    if answer == n1 * n2:
        print("Right!")
    else:
        print("Wrong!")

# QUESTION 4


for i in range(200):
    if i % 5 == 2:
        if i % 6 == 3:
            if i % 7 == 2:
                print("There are " + str(i) + " candies in total")