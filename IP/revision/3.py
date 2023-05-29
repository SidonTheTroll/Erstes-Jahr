'''
    Write a program to check if a given triangle is quable or not. A triangle is said to be quable when its perimeter and area both are same.
    For example a right angled triangle with its sides 5, 12, 13 has same perimeter and area
'''

print("Please enter the measurements of the triangle.")

b = int(input("Enter the base: "))
p = int(input("Enter the height: "))
h = int(input("Enter the hypotenuse: "))

area = 1/2 * b * p 
peri = p + b + h 

if area == peri: 
    print("Yes, the triangle is quable")

else: 
    print("No, the triangle is not quable")