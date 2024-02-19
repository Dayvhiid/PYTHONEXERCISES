# program that returns the largest of three arguments

def returnMax(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print("The greatest number is ",num1)
    elif num2 > num3 and num2 > num1:
        print("The gratest number is ",num2)
    elif num3 > num1 and num3 > num2:
        print("The greatest number is", num3) 
           
returnMax(10,20,30)