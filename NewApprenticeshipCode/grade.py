#Zachary Pajela
#Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. 
# If the score is between 0.0 and 1.0, print a grade using the following table:
#
#Score   Grade
#>= 0.9     A
#>= 0.8     B
#>= 0.7     C
#>= 0.6     D
#< 0.6    F
#~~~
#Exercise 7: Rewrite the grade program from the previous chapter using a function called 
# computegrade that takes a score as its parameter and returns a grade as a string.

def computeGrade(score):
        if score > 1:
            a = "Out of range"
        elif score >= .9:
            a = "A"
        elif score >= .8:
            a = "B"
        elif score >= .7:
            a = "C"
        elif score >= .6:
            a = "D"
        elif score < .6:
            a = "F"
        return a

print("\nWelcome to the score evaluator! Follow the instructions as provided.")
loop = 'true'

score = float(input("Enter your score: "))

print(computeGrade(score))
   