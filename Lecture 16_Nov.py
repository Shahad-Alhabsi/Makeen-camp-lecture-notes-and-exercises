# Exercise 1: Find the sum ofthe integers of a given number
num = input("Enter a number: ")
Sum = 0
i = len(num)
while(num !=0):
    Sum += int(num)//10**(i-1)
    num = int(num)%10**(i-1)
    i -= 1
print(Sum)

# A second way to solve it
num = input("Enter a number: ")
Sum = 0
while(num!=0):
    Sum += int(num)%10
    num = int(num)//10   
print(Sum)

#A third way, using string slicing
num = input("Enter a number: ")
Sum = 0
i = 0
while(i<len(num)):
    Sum += int(num[i])
    i += 1  
print(Sum)

#############################################################
"""
The differance between break and continue:
using both while and for loops
"""
print("In the case of break at 4:")
for i in range(0,10):
    if i == 4:
        break
    else:
        print(i)

print("In the case of continue at 4:")
for i in range(0,10):
    if i == 4:
        continue
    else:
        print(i)

i = 1
while(i<=10):
    if i==4:
        i+=1
        break
    print(i)
    i+=1
    
i = 1
while(i<=10):
    if i==4:
        i+=1
        continue
    print(i)
    i+=1

######################################################
    
# Exercise 2: Simple Cryptograpy, usin both loops
Message = input("Enter your encrypted message:  ")
print("using foor loop: ")
for i in Message:
    print(chr(ord(i)-3), end='')

print("\nusing foor while: ")
i = 0
while(i<len(Message)): 
    print(chr(ord(Message[i])-3), end='')
    i += 1




















    
    