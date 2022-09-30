# Zachary Pajela
# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, 
# print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:Score   Grade
#>= 0.9     A
#>= 0.8     B
#>= 0.7     C
#>= 0.6     D
#< 0.6    F

userScore = float(input("Please enter your score: \n"))

if userScore >= 1.0:
    print("Error")
elif userScore >= .9:
    print ("A")
elif userScore >= .8:
    print ("B")
elif userScore >= .7:
    print ("C")
elif userScore >= .6:
    print ("D")
elif userScore < .6:
    print ("F")
else: 
    print ("Error")