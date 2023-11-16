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


# Exercise 4: Write a program that takes two times of the day and prints out wa time comes before the other.
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
    

# Exercise 5: Wrie a progra tha simulates an ATM, the program should ask the user foue their PIN
# it it's correct, allow them to check palance, withdraw money, or deposit money.
PIN = 1234
balance = 1000000
user_pin = int(input("Enter your PIN: "))

cancle = False
while not cancle:
    if user_pin == PIN:
        print("\nA. Check palance\nB. withdraw money\nC. deposit money")
        choice = input("Your Choice (A,B or C)? ")
        if choice.upper() == "A":
            print("Your Palance = " + str(balance) + " OR")
            c = input("Exit (y/n)? ")
            if c.upper() == "Y":
                cancle =True
        
        elif choice.upper() == "B":
            withdraw_amount = float(input("Enter amount to withdraw: "))
            if withdraw_amount > balance:
                print("Insuffecient balance")
            else:
                balance -= withdraw_amount
                print(str(withdraw_amount) + " OR whas withdrawed from your account successfully")
                c = input("Exit (y/n)? ")
                if c.upper() == "Y":
                    cancle =True
        elif choice.upper() == "C":
            deposit_amount = float(input("Enter amount to deposit: "))
            balance += deposit_amount
            print(str(deposit_amount) +" OR whas withdrawed from your account successfully")
            c = input("Exit (y/n)? ")
            if c.upper() == "Y":
                cancle =True                
        else:
            print("Invalid Choice!\n try again \n")
    else:
        print("Invalid PIN!\n try again \n")


# Exercise 6: Find the leap year
stop = False
while not stop:
    year = input("Enter the year: ")
    while(year=='' or not year.isdigit()):
            year = input("The year must be an integer number without spaces. Try again: ")
    if (int(year)%4==0):
        print("This year is a leap year")
    else:
        print("This year is not a leap year")
    exit = input("Exit? (y/n): ")
    if exit.upper() == "Y":
        stop = True




















