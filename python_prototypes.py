 
#  This is a prototype program file to test code for efficiency of code


# Get user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

def descending_order(a, b, c):
    numbers = [a, b, c]
    numbers.sort(reverse=True)
    return numbers


# Call the function and print the result
result = descending_order(num1, num2, num3)
print("Numbers in descending order:", result)
