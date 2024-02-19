# swedish robbers language
def translate(word,resultantWord):
    vowels = ["a","e","i","o","u"]
    wordArray = []
    for char in word:
       wordArray.append(char)
    
    for _ in wordArray:
        if _ in vowels:
            print(True)
        else :
            print(False)    


translate("David","null")
def translate2(word):
    resultantWord = " "
    for i in word:
        if i not in ("aeiou"):
            resultantWord = resultantWord + "o" + i
        else  :
            resultantWord = resultantWord + i
    final =  resultantWord.replace(" ","")
    print(final)        
              
translate2("David is a fun guy")         
# initiate a word parameter
# create another string to store the resultant text
# create an array that stores all vowels
# use this array to check if it is a vowel or not
# take the word provided break it into an array of elemets
# if it is a vowel we append o to it 
# then we append to letter again after the o
# we convert this array back to a string
# then we save it to the resultantword variable