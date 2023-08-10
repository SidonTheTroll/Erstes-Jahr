# 01/08/23

## Types of control flow  

```
if 
for loop 
while loop 
```

## Types of statements 

- Empty statement: Uses 'pass' syntax 
- Single statement: One line statement 
- Compound statement: More than one statement 


### To keep an empty statement, pass syntax is used. 
```
if ch == '':        # this is a header 
    spaces += 1     # this is a body  
    chars += 1      # this is a body 
```

### Program to print the smallest number 
```py
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

min = x 

if y < min: 
    min = y 

if z < min: 
    min = z 

print(f"The smallest number is {min}.")

```


# 09/08/23 

### Program to print a right-angle triangle 
```py 
for i in range(1,6): 
    for j in range(i):
        print(1, end='')
    print()
```

```py
a = 5; b = 2 

for i in range(1,6): 
    for j in range(1, a): 
        print("", end=" ")

    for k in range(1,b):
        print('1', end='')

    a -= 1 
    b += 2 
    print()
```