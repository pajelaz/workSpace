"""
Zachary Pajela 

 Ask the user for a number. 
 Depending on whether the number is
 even or odd, print out an appropriate 
 message to the user. Hint: how does an 
 even / odd number react differently when 
 divided by 2?
    
"""

userInput = int(input("Give me a number"))

if userInput % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd")
    