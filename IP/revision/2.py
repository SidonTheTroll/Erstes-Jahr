''' 
    Write a program to input a number from user and print whether if it is negative or positive or neither negative nor positive
'''

x = int(input("What is the number? \n"))

if x < 0: 
    print("The number is negative.")

elif x > 0:
    print("The number is positive.") 

else: 
    print("It is neither positive nor negative.")