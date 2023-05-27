'''
    Write a program to check a given number is special 2 digit number or not.
'''

x = int(input("What is the number? \n"))

b = x // 10
c = x % 10

if ((b + c) + (b * c)) == x:
    print("It is a special 2 digit number")

else: 
    print("It is not a special 2 digit number")