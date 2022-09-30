#Zachary Pajela
#Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
#Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by 
#printing a message and exiting the program. 
#Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called 
# computepay which takes two parameters (hours and rate).

#this is the function that calculates pay

def computePay(num1,num2):
    if num1 >= 40.0:
        grossPay = ((num1-40) * (num2 * 1.5)) + (num2 * 40)
    else:
        grossPay = num1*num2
    return grossPay

#this is user input
userHours = float(input("Please enter your hours: \n"))
userRate = float(input("Please enter your pay: \n$"))

#print statement 
print (computePay(userHours,userRate))
