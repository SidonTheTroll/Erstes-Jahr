n = int(input("Enter to check if a number is palindrome or not: "))
rev = 0 
cn = n 

while n > 0: 
    rem = n % 10 
    rev = (rev * 10) + rem 
    n = n // 10 

if rev == cn: 
    print("Yes it is a palindrome number.")
else: 
    print("No it is not a palindrome number.")