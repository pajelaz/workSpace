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


print("\nWelcome to the score evaluator! Follow the instructions as provided. Input \"Help\" for instructions.")
loop = 'true'

while loop == 'true':

    score = input("Enter score: ")
    try:
        score = float(score)
    except ValueError:
        pass
    else:
        if score > 1:
            print("Out of range")
        elif score >= .9:
            print("A")
        elif score >= .8:
            print("B")
        elif score >= .7:
            print("C")
        elif score >= .6:
            print("D")
        elif score < .6:
            print("F")
        continue

    try:
        score = str(score)
    except ValueError:
        pass
    else:
        if score in ['exit', 'Exit','EXIT']:
            print ("Exiting")
            loop = 'false'
        elif score in ['help','Help','HELP']:
            print("\n\nHelp: \n")
            print("Input score from range 0.0 - 1. Type \"Exit\" to exit the program.\n\n")
        else:
            continue
