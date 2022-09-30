#Zachary Pajela
#Write a program that checks if a number is even or odd. You must use a fruitful function.

def check(num):
    if (num % 2) == 0:
        return 'Even'
    else:
        return 'Odd'

input = int(input("Give me a number: "))
print (check(input))
