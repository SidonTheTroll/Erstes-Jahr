'''
Write a program which prints the largest and second largest number in a given list. 
'''

a = eval(input("Enter the list: "))

l = s = 0

for i in range(len(a)):
    if a[i] > l:
        s = l
        l = a[i]
    elif a[i] > s and a[i] != l:
        s = a[i]

if s == 0:
    print("There is no second largest number.")
else:
    print("Largest number:", l)
    print("Second largest number:", s)
