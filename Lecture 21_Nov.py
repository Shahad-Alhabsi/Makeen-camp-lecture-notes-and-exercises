# find the area of a polygon
def area(n, side):
    res = n * side**2/ (4 * tan(pi/n))
    print("The area of the polygon = ", res)
    print("The area of the polygon = %.2f "%(res))
    
from math import *
area(5,6.5)


# take a string and return it with upper case for the vowel litters only 
def upperVowels(strg):
    strg = strg.lower()
    for i in strg:
        for v in ["A", "U", "O", "I", "E"]: 
            if i.upper() == v:
                strg = strg.replace(i, v)          
    return strg

print(upperVowels("Shahad"))



# find the number of negative numbers in a list
x = [-1,2,-3, 9]

count = 0
for i in x:
    if i < 0:
        count += 1
        
print(count)

# a program that lets the user construct a lis of integers
result = []
while 1:
    try:
        n = input("Enter an integer 0r 'Q' to quit: ")
        if n.upper() == "Q":
            print(result)
            break
        else:
            result.append(int(n))
    except:
        print("ERROR! Invalid input")

# a program that prints the first number > 100 in a list of numbers
nums= [100, 22, 105, 8000]
result = "There is no number greater than 100 in te list"
for n in range(len(nums)):
    if nums[n] > 100:
        result = (f"--> number {nums[n]} in position {n}")
        break
print(result)


"""
This function takes the number of sides of a die and a list representing the numbers gaind from rolling it
then returns back how many times did each number(side) appear.
"""
def countInputs(sides, inp):
    counter = [0 for o in range(sides)]
    for i in inp:
        counter[i-1] += 1
    return counter

def printCounters(counter):
    for i in range(1,len(counter)+1):
        print(i,":", counter[i-1])
                
def main():
    go = True
    try:
        sides = int(input("\nHow many sides does your die have? "))
        List = input("Enter the numbers that you got fron rolling the die (separated by a space): ")
        List = [int(i) for i in List.split()]
        for i in List:
            if not (1 <= i <=sides):
                print(f"ERROR! you cannot get a number graeter that {sides}")
                go = False
                break         
    except:
        print("make sure you enter integers only")
        main()
        
        
    else:
        # if every thing went ok
        if go:
            printCounters(countInputs(sides,List))
        else:
            main()
            
main()
    
