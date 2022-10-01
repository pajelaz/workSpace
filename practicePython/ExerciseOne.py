"""
Zachary Pajela
    
Create a program that asks the user to 
enter their name and their age. 
Print out a message addressed to them that 
tells them the year that they will turn 100 
years old. Note: for this exercise, the 
expectation is that you explicitly write out 
the year (and therefore be out of date the 
next year).     
    
    
    
"""

nameInput = input("What is your name? ")
ageInput = int(input("What is your age? "))

calculatedAge = (100 - ageInput) + 2022

print (f"Dear {nameInput}, you will turn 100 \
years old in the year {calculatedAge}")