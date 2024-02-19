def multiply(numbers):
    total = 1  # holding variable
    for number in numbers:
        total = total * number
    print("The total of everything is", total)
    
def sum(numbers):
    total = 0
    for number in numbers:
        total = total + number
    print("The total of everything is", total)
    
sum([1,2,3])
multiply([2,2,3,4])