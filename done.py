#Zachary Pajela
#Exercise 1: Write a program which repeatedly reads numbers until the user enters "done". 
# Once "done" is entered, print out the total, count, and average of the numbers. 
# If the user enters anything other than a number, detect their mistake using try and 
# except and print an error message and skip to the next number.


#num = 0
#tot = 0.0
#while True:
#    number = input("Enter a number")
#    if number == 'done':
#        break
#    try :
#        num1 = float(number)
#    except:
#        print('Invailed Input')
#        continue
#    num = num+1 #finds count
#    tot = tot + num1 #adds the two together
#print ('all done')
#print (tot,num,tot/num)


#Exercise 2: Write another program that prompts for a list of numbers as 
# above and at the end prints out both the maximum and minimum of the numbers instead of the average.

y = []
foo = 1

for x in range(0,10):
    userInput = int(input("Give me input: "))
    y.append(userInput)

print(min(y), max(y))
