#QUESTION 1
def reverse(string):
    string = string[::-1]
    return string



string=str(input("enter the string:"))

print("The reverse of string is:",reverse(string))

#QUESTION 2
a=int(input("starting of range:"))
b=int(input("ending of range:"))
c=int(input("enter number to check divisiblity:"))

for i in range(a,b):
    if i%c==0:
        print(i)

#QUESTION 3
import math
def heron():
    s = (side_1+side_2+side_3)/2
    area = math.sqrt(s*(s-side_1)*(s-side_2)*(s-side_3))
    return area

side_1=int(input("Enter length of side one :"))
side_2=int(input("Enter length of side two :"))
side_3=int(input("Enter length of side three :"))
if side_1 + side_2 > side_3 and side_2 + side_3 > side_1 and side_3 + side_2 > side_1:
    print("Area of given triangle",heron())
else:
    print("Invalid input of sides,triangle not possible")


#QUESTION 4
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end='')

    print("\n")

for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print("*", end='')

    print("\n")

#QUESTION 5

k=ord("A")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(chr(k), end='')
        k=k+1

    print("\n")
#QUESTION 6

start=int(input("Enter strating of range:"))
stop=int(input("Enter ending of range:"))
for number in range(start,stop):
    for i in range(2,number):
        if (number%i)==0:
            break

    else:
        print(number)


print("QUESTION 7")
#QUESTION 7
for i in range(1,501):
    if i%11==0:
        if i%7==0:
            print(i)

#QUESTION 8
lst = []
positive_numbers = set()
negative_numbers = set()
odd_numbers = set()
even_numbers = set()
print ('Enter the 10 no. for list:')
for i in range(0,10):
    print ('Enter the', i+1,'no. for list')
    n = int(input())
    lst.append(n)  # adding the element
print ('list entered',lst)
for i in lst:
    if (i>0):
        positive_numbers.add(i)
    if (i<0):
        negative_numbers.add(i)
    if (i%2!=0) :
        odd_numbers.add(i)
    if (i%2==0) :
        even_numbers.add(i)
print ("positive no. \n", positive_numbers)
print ('negative no.\n', negative_numbers)
print ('odd no.\n', odd_numbers)
print ('even no.\n', even_numbers)
number_occurs= dict()
for i in lst:
    if i in number_occurs:
        number_occurs[i]+=1
    else:
        number_occurs[i]=1
print('No. of occurrence is',number_occurs)

#QUESTION 9
word_list=[]
elements=int(input('Enter total elements in the list:'))
for word in range(1,elements+1):
  x=input('Enter a word ')
  word_list.append(x)
for element in word_list:
  occ=0                                 #counter for occurrences in a list
  for element1 in word_list:
    if element==element1:
      occ+=1
  print(f"{element} occurs {occ} times")