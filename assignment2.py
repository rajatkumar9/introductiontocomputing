QUESTION 1

String="Python is a case sensitive language"


# LENGTH OF STRING USING LENGTH() FUNCTION
print("The length of given string is : ",len(String))

# [starting index:stoping index:gap or order]
print("The reverse of string is:",String[::-1])

# SLICE OPERATION
new_string=String[10:26:1]
print('new string using slice operation :',new_string)


# REPLACING SUBSTRING
replacing=String.replace("a case sensitive","object oriented")    # replacing
print(replacing)


# INDEXING OF SUBSTRING

print("indexes of a are :",String.index("a",0,11),String.index("a",11,16),String.index("a",16,35))

# REMOVE WHITE OR BLANK SPACES
print("string after replacing blank spaces :",String.replace(" ",""))


#QUESTION 2
Name="Rajat"                    # ASSIGNING A STRING VALUE IN A VARIABLE
SID=21107115                    # ASSIGNING A INTEGER VALUE IN A VARIABLE
CGPA=9.9
Department="Mechanical"

print("Hey",Name,"Here!")
print("My SID is",SID)
print("Iam from",Department,"department and my CGPA is:",CGPA)

#QUESTION 3

a=56              # a in binary 111000
b=10              # b in binary   1010


print("A. a & b =", a & b)

# Use of Bitwise OR(|) operator.
print("B. a | b =", a | b)

# Use of Bitwise XOR(^) operator.
print("C. a ^ b =", a ^ b)

# Use of shift(left) operator.
print("D. a << 2 = ", a << 2)

# Use of shift(both) operator.
print("E. a >> 2 = ", a >> 2, " and ", "b >> 4 = ", b >> 4)



#QUESTION 4

string=str(input("Enter a string :"))

if "name" in string:             # USING FOR LOOP TO FIND A SUB STRING
    print("yes")
else:
    print("no")

#QUESTION 5


# Taking inputs of the sides of the triangle.
n1 = int(input("Enter First length : "))
n2 = int(input("Enter Second length : "))
n3 = int(input("Enter Third length : "))

# Checking the condition for triangle to be formed.
F1 = n1 > n2 + n3
F2 = n2 > n1 + n3
F3 = n3 > n1 + n2

# Here we check wheather the all conditions are satisfied or not.
Output = str(F1 or F2 or F3)

print("The triangle can be formed?")

# Using string slicing.
print(Output.replace("True", "No!").replace("False", "Yes!"))




#QUESTION 6

def function(a,b):
    ab_xor=a^b
    count=0
    while ab_xor:

        count=count+ (ab_xor & 1)         # xor gives 1 for different values
                                          # and 0 for same values
        ab_xor=ab_xor>>1
    print(count)


a=int(input("enter number 1:"))
b=int(input("enter number 2:"))
function(a,b)


