# program to count the nunber of characters in a string
text = "David dada is a good boy" 
 
def charCounter():
    character_counter = 0 
    for char in text:
        character_counter = character_counter + 1
    print("The number of string in the is", character_counter)
charCounter()
