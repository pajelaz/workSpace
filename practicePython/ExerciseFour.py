"""
Zachary Pajela

Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you dont know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

"""

userInput = int(input("Give me a number: "))
foo = range(1,userInput+1)

print("Here are all of the divisors: ")
for i in foo:
    if userInput % i == 0:
        print(i)
    else:
        continue
    