# Exercise 1: find out if a numbe is even or odd
n = int(input("Enter a number: "))
if n%2 == 0:
    print(str(n)+" is an even number")
else:
    print(str(n)+" is an odd number")
    
# Exercise 2: calculate the discount of a shopping cart based on the total amount,
# if the total amount is greater than 100 apply 10% discount, otherwise, apply a 5% disount.
price = float(input("Enter te price: "))
if price > 100:
    print("Your total amount is "+str(price-(price*10/100)))
else:
    print("Your total amount is "+ str(price-(price*5/100)))
    
    
# Exercise 3: Check if the person is a male 24 - 30 years old
gender = input("Enter yor gender(m/f) please: ")
answer = "Not accepted"
if gender.upper() =="M":
    age = int(input("Enter yor age please: "))
    if 30>= age >=24:
        answer = "Accepted"
        
print(answer)

# # Exercise 4: Write a program that takes two times of the day and prints out wa time comes before the other.
time1 = input ("Enter the first time: ")
time2 = input ("Enter the seconnd time: ")

# get only te hours and minutes in a list
T1 = time1[:-2].split(":")
T2 = time2[:-2].split(":")
#get the period (AM/PM)
period1 = time1[-2:]
period2 = time2[-2:]

#The same time of the day, check the hours
if period1 !=  period2:
    #different time of te day, AM comes before PM (PM > AM)
    if period1 > period2:
        print(time2 + " comes before " + time1)
    else:
        print(time1 + " comes before " + time2)
               
else:# the same period
    #check hours
    if int(T1[0]) > int(T2[0]): # T1 hours > T2 hours
        print(time2 + " comes before " + time1)
    if int(T1[0]) < int(T2[0]):# 1- T1 hours < T2 hours
        print(time1 + " comes before " + time2)
        
    else:#same hour, check minutes
        if int(T1[1]) > int(T2[1]):
            print(time2 + " comes before " + time1)
        elif int(T1[1]) < int(T2[1]):
            print(time1 + " comes before " + time2)
        else:
            print(time1 + " is the same as " + time2)
    































