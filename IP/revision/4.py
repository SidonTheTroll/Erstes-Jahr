# Get user input
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))


p = int(input("Press 1 for ascending order or 2 for descending order: "))

if (p==1): 
    def ascending_order(x,y,z):
        num = [x,y,z]
        num.sort()
        return num 

    result = ascending_order(a,b,c)
    print(result)


elif (p==2):
    def descending_order(x,y,z):
        numbers = [x,y,z]
        numbers.sort(reverse=True)
        return numbers


    result = descending_order(a,b,c)
    print(result)

else: 
    print("Invalid input. Please input again.")