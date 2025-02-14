# 1/07/23

Datatypes form the foundation in python, providing the flexibility and functionality necessary for various computational tasks.

- Datatypes:
  - Character: stores letters, characters, symbols
  - Integer: stores whole numbers
  - String: stores words, sentences, numbers, special symbols
  - Float: Stores decimals
  - Boolean: True or False

> Python's variables are lables, i.e., variables are assigned and can be changed too without changing the value.

- Python by default stores input values as strings.

| Integer   | Decimal   |
| --------- | --------- |
| a = 2     | a = 2     |
| b = 3     | b = 3.5   |
| c = a + b | c = a + b |
| c = 5     | c = 5.5   |

> In python, the input order determines the datatype of output.

`n = int(input("Enter a number: ")) # 3.2 -> 3`  
`n = float(input("Enter a number: ")) # 7 -> 7.0`

- Disadvantages of float datatypes:
	1. It is slower than integer operations
	2. After decimal point the maximum digits accepted is 15.

<br>

- In string datatype, the address lines starts from zero

```
0 1 2 3 -> Forward indexing
R A M A
```
`>` x[0]  
'R'

```
-4 -3 -2 -1 ->  Backward indexing
 R  A  M  A 
```
`>` x[-4]  
'R'

- **Forward indexing** starts from 0
- **Backward indexing** ends with -1

## Lists, Tuples and Dictionary

- List and tuple are used to store multiple items in one variable

**List** offers ***flexibility for modification***.  
**Tuples** provide ***immutability and has fixed collection for values.***

```
list = [1, 2, 3]
tuple = (1, 2, 3)
```

## Boolean Alzebra & Logic Gate

- There are 3 types of logic gates-
	- And gate
	- Or Gate
	- Not gate

- **And gate**: And gate works when all the conditions are true.

Eg- Write a program to input 3 sides of a triangle and check the triangle is equilatreal or not.

```py
a = int(input("Enter the 1st side: "))
b = int(input("Enter the 2nd side: "))
c = int(input("Enter the 3rd side: "))

if (a == b and b == c and c == a):
print("It is an equilatreal triangle.")

else:
print("It is not an equilatreal triangle.")
```

- **Or gate**: Or gate works when any one condition is true.  
Eg- Write a program to input 3 angles of a triangle and check if it is right angled triangle or not.

```py
a = int(input("Enter the 1st angle: "))
b = int(input("Enter the 2nd angle: "))
c = int(input("Enter the 3rd angle: "))

if (a == 90 or b == 90 or c == 90):
print("It is a right angled triangle.")

else:
print("It is not a right angled triangle.")
```

- **Not gate**: Not gate returns complimentary value of a given data or value.  
Eg- write a program to use not gate and print input true as false and false as true.

```py
def not_gate(value):
return not value

def get_user_input():
while True:
input_value = input("Enter True or False: ").lower()
if input_value == "true":
return True
elif input_value == "false":
return False
else:
print("Invalid input. Please enter True or False.")

print(not_gate(get_user_input()))
```

# 06/07/23

## Multiple assignment

```py
x = 5
y = 6
z = x + y

print(z) # 11
```

> the above syntaxes assign values to variables

```py
x , y = 5 , 6 # this syntax is a multiple assignment
z = x + y

print(z) #11 
```
-  One variable can have more than one value in python.

```py
x = 5,6
print(x) # (5,6) because x is now a list
```
```py
x = 5
y = 6
x = x + y
y = y + 1
print(x, y) # 11 12
```
```py
x = 5
y = 6
x,y = x+y , x+1 # multiple assignment
print(x,y) # 11 6
```
- Because multiple assignment doesn't change the value of variable for that line.

- Python doesn't change values till syntax is completed and stores it in the RAM.
