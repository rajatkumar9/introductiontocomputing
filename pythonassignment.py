# QUESTION 1
number_1=int(input("Enter number 1 :"))      #taking input of three integers from user
number_2=int(input("Enter number 2:"))
number_3=int(input("Enter number 3:"))
#The average of three number = sum of all the elements/number of elements
Average=(number_1+number_2+number_3)/3
print('The average is:',Average)


# QUESTION 2
income=int(input("Enter your income in $:"))
dependents_in_family=int(input("Enter number of dependents in your family:")) 
dependent_tax_deduction=3000       #Tax deduction for the person having dependents on him
standard_deduction=10000           #To be charged on all the tax payers
tax_rate=0.2                       #rate of tax implemented on income
income_after_deduction=income-standard_deduction-(dependents_in_family*dependent_tax_deduction)
tax=income_after_deduction*tax_rate
print ("tax on your income is:",tax)


# QUESTION 3
number_of_minutes=int(input("Enter number of seconds : "))                       #takes number of minutes as input from user
# //-  gives Quotient as output
# %-   gives remainder as output
print("It has",number_of_minutes//60,"minutes and " ,number_of_minutes%60,"seconds")


# QUESTION 4
number1=25
number2='25'
number3=25.0
sum= number1+int(number2)+number3    # We made first number2 a integer in order to perform addition
string_sum=str(sum)                  # Here we made the sum which is in floating data type to a string
print(string_sum, type (string_sum))


# QUESTION 5
import math                                 # Command to import math module in order to use mathematical terms and values    
for i in range(0,360,15):                   # for loop is used first shows starting value
                                                             # second shows ending value
                                                             # third shows steps or gaps to be taken                 
    cosine=math.cos(math.radians(i))       # i is a variable runing in for loop
    sine=math.sin(math.radians(i))         # Gives answer in radians 
    print( "cosine(",i,") is",round(cosine,4),"           sine(",i,") is",round(sine,4))