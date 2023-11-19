"""
Iterations Questions:
=====================


1) Assume that you have a message like "hello", your message was
encrypted to be like "khoor" write programming code to decrepit
the following message to get the original one.
Message = "|rx#duh#juhdwh"
"""
Message = "|rx#duh#juhdwh"

for i in Message:
    print(chr(ord(i)-3), end="")



"""
2) Write a python code to draw this shape:
*
**
***
****
*****
****
***
**
*
"""
for i in range(1,6):
    print('*'*i)

for i in range(4,0,-1):
    print('*'*(i))



"""
3) Print all perfect number from 1 to 100, if you know that a perfect
number is a positive integer that is equal to the sum of its
positive divisors, excluding the number itself. For instance, 6 has
divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so 6 is a
perfect number.
"""
# Find the positive divisors for an integer n by taking the integers 1, 2, 3, . . . , n,
# divide n by each, and those that divide evenly make up the set of positive divisors for n
for i in range(1,101):
    divisors = []
    for d in range(1, (i+1)):
        if (i%d ==0) and (d!=i):
            divisors.append(d)
    if (i>0) and (sum(divisors)==i):
        print(i)



"""
4) Check whether a number is a Narcissistic number or not in Python,
if you know that Narcissistic numbers are the special type of
numbers where that number can be formed by sum of its own
digits raised to the power of no. of digits.
Example output:
153
Yes
"""
ask = True
while ask:
    num = input("Enter a number t heck if narcissistic or not: ")
    if num.isdigit():
        ask = False
num_copy = int(num)
pwr = len(num)
sum_ = 0
for i in num:
    sum_ += (int(num)%10)**pwr
    num = int(num)//10
if sum_ == num_copy:
    print("Yes")
else:
    print("No")
 
 
 
"""
5) Write a program that takes a message and returns the number of integers in it.
"""

message = input("Enter a mesage: ")
sum_= 0
for i in message:
    if i.isdigit():
        sum_ += 1
print(f"The assage contains {sum_} numbers")



"""
6) writhe a program that hecs if a phoe number is valid( or not
"""
answer = "Not Valid"
phone_num = input("Enter a phone number: ")

count_spaces = 0
for char in phone_num:
    if char.isspace():
        count_spaces += 1
        
if count_spaces == 1:
    X, Y = phone_num.split()
    if X=="+968":
        if "-" in Y:
            A, B = Y.split("-")
            if A.isdigit() and len(A)==4 and B.isdigit() and len(B)==4:
                answer = "Valid"
                s
print(answer)
            
"""
7) Update the guessing game by randomizing the correct number

"""
from random import randint
correct_number = randint(1,100)
num = int(input("Guess the number: "))
while (num != correct_number):
    if correct_number>num:
        num = int(input("Up: "))
    else:
        num = int(input("Down: "))
       
print("Win!") 

##########################################################################################
"""
Functions Questions:
====================

1) write a function that takes the grades of n students and returns their average.

"""
def find_average():
    n = int(input("Enter number of students: "))
    sum_ = 0
    for i in range(1,n+1):
        grade = input(f"Student {i} grade: ")
        sum_ += float(grade)
    return (sum_/n)

print("Average = ",find_average())



"""
2) write a function that caculate the area/volume of shapes for the user
"""
def triangle(base, height):
    return(0.5*(base * height))
 
def square(side):
    return(side**2)

def circle(radius):
    from math import pi
    return(pi * radius**2)

def cylender(radius, heiht):
   from math import pi
   return(heiht * pi * radius**2)

Loop = True
while Loop:
    choice = input("\nChoose 1, 2, 3, 4, Q: ")
    if choice.upper() =="Q":
        print("Quit!")
        Loop = False
        
    elif choice == "1":
        print("Calculating the area of a triangle:\n","="*36)
        b = float(input("Enter the base: "))
        h = float(input("Enter the height: "))
        print("The area of the triangle  = %.3f"%(triangle (b, h)))
        
    elif choice == "2":
        print("Calculating the area of a square:\n","="*33)
        s = float(input("Enter the side height: "))
        print("The area of the square = %.3f"%(square(s)))
        
    elif choice == "3":
        print("Calculating the area of a circle:\n","="*33)
        r = float(input("Enter the radius: "))
        print("The area of the circle = %.3f"%(circle(r)))
        
    elif choice == "4":
        print("Calculating the volume of a cylender:\n","="*37)
        h = float(input("Enter the height: "))
        r = float(input("Enter the radius: "))
        print("The volume of of cylinder =  %.3f"%(cylender(r, h)))
    
    else:
        print("Invalid choice. Try again")
        



