'''
    Write a program to input a 3-digit number from user. Now print the summation of first and second digit and product of first and third number
'''

a = int(input("Enter a 3-digit number: "))

x = a % 10 

a //= 10 

y = a % 10 

z = a // 10 

s = z + y 
p = x * z 

print(f"{s}" + f"{p}") 



