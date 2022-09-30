#Zachary Pajela
#Write a program that prompts a user for a language. Print "Hello" in that language.

def greet(lang):
    if lang == 'en':
        print ("Hello!")
    elif lang == 'es':
        print("Hola!")
    elif lang == 'fr':
        print("Bonjour!")
    
print("-------------- \nEnglish = en\nSpanish = es\nFrench = fr\n--------------")
language = input("Give me a language code from the above list: ")

greet(language)