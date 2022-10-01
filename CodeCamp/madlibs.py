"""
Zachary Pajela 

string concatenation 
suppose we wanted to create a string that says
"subscribe to ___"
    
youtuber = "Zachary Pajela"
print ("subscribe to", youtuber)
print ("subscribe to {}".format(youtuber))
print (f"subscribe to {youtuber}")

"""

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famousPerson = input("Famous person: ")

madlib = f"Computer programming is so {adj}!\
 It makes me so excited all the time becauseasd\
 I love to {verb1}. Stay hydrated and {verb2}\
 like you are {famousPerson}!"
            
print(madlib)