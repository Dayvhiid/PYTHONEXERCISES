# program to check if an argument is a vowel

def vowelCheck(character):
    vowels = ["a","e","i","o","u"]
    if character in vowels:
        print(True)
    else:
        print(False)    
vowelCheck("d")