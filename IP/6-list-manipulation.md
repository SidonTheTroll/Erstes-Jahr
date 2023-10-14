# 04/10/23 

```py
a = 5 
b = 6
c = a + b 
print(c)  # 11
```

Similarly, 

```py
a = 5 
a = 3 
b = 2 
c = a+b 
print(c)  #  5 
```

But for this case, the replaced variable gets deleted. This is the problem of python

- Storage also becomes difficult with huge number of variables. 

List solves that problem 

```py
     0  1  2  3  4  5
E = [50,60,70,80,90,100]
M = [50,60,70,80,90,100]
```

The numbers above are called index value or address.  
They always start from zero. 

```py
print(E[0])  # 50 
print(E[5])  # 100 
```
> The above shows index numbers are used to locate values within a list. 

- **Index value**:
    1. Positive Index Value 
    2. Negative Index Value

- Negative Index value ends with -1 

```python
B = [50,60,70,80,90]
     -5 -4 -3 -2 -1 
```

> It works like a number line. 

## Types of Lists 

```py
a = [1,2,,3,4,5] # Integer list  
b = [1.6,2.3,3.9,4.4,5.6] # Floating-point list  
c = ['W','O','R','L','D'] # Character list  
d = ['so','sehr','schon']  # Word List  
e = [1, 3.5, -2, 'Sekai','L'] # Mixed list   
```

- For calculations, only pure list of one type is applicable. 

## Creating an Empty List 

Q = List[]

- Sequence is also a kind of list 

`a = (1,2,3,4,5) # This is a sequence`

- List follows index values but sequences do not. 

### Converting Sequence to a list 

```py 
a = (1,2,3,4,5)
b = List[a]

print(b) # [1,2,3,4,5]
print(a) # (1,2,,3,4,5)

```

- Sequence can be converted into list but not vice versa. 

# 05/10/2023

## List VS String 

- List: mutable 
- String: non-mutable 

### Q/ Write a program to print the positive and negative indexes of each element of a sequence which is given below along with the elements. (['s','c','h','o','o','l'])

```py
a = ['s','c','h','o','o','l']
L = len(a)
n = 0 

for n in range(L):
    print('At indexes', n, "and", (n-L), 'element is:', (a[n]))

```
> The output will be the following   
> At indexes 0 and -6 element is: s   
> At indexes 1 and -5 element is: c  
> At indexes 2 and -4 element is: h  
> At indexes 3 and -3 element is: o  
> At indexes 4 and -2 element is: o  
> At indexes 5 and -1 element is: l  

- ONLY ADDITION OF ELEMENTS IS ALLOWED IN LISTS 
- AND TWO LISTS CANNOT BE MULTIPLIED

### Program to combine lists

```python

A = [1,2,3,4]
B = [1,2,3]

C = A+B 

print(C) # [1,2,3,4,1,2,3]

```

### Program to multiply the element of list 

```python


B = [1,2,3]
B = B*3 

print(B) # [1,2,3,1,2,3,1,2,3]
```

### Program to check for equal content in list 

```python

A = [1,2,3,4]
B = [1,2,3]

if A == B: 
    print('Equal')
else: 
    print('Not equal')
```

- "Greater than and less than functions can also be used."

### Making new list from existing list 

```python
A = [1,2,3,4,5,6,7]
B = A[3:6]

print(B) # [4,5,6]

# For reverse 

B = A[::-1]
print(B) # [7,6,5,4,3,2,1]

# Skipping values 

B = A[0:5:2]
print(B) # [1,3,5]
```

# 06/10/23 

### Q/ Write a program to store all vowels in a list. Now display any one vowel as per the user's choice. User will choose the vowel as per the index value.

```py
A = ['a', 'e', 'i', 'o', 'u']
n = int(input("Enter a vowel to print, you need to enter number from 1 to 5: "))

print(A[n-1])
```

### Write a program and store 10 different numbers in a list. Print the highest number from the list. 

```py 
A = [5,9,10,2,3,23,17,20,8,1]
n = 0 

for i in range(10):
    if (A[i]>n):
        n = A[i]

print("The highest number is", n)
```

### Write a program to increment the elements of a list with a number 

```py 
myList = [1,2,3,4,5]

value = 10 

# value = int(input("What's the value of incrementation?\n"))

for i in range(len(myList)):
    myList[i] += value 

print("List after incrementing:", myList)
```

### Write a program to reverse a list of integers (in place)

```py 
a = [1,2,3,4,5]

a = a[::-1]

print(a)
```

### Write a program that inputs two lists and creates a third, that contains all element of first followed by all elements of the second. 

```py 
a = [1,2,3,4,5]
b = [6,7,8,9,10]

c = a+b 

print(c)
```

# 10/10/23 

### Write a program to accept numbers from 1 to 12 and transform any number to 10 if its larger than 10. 

```py 
a = eval(input("Enter elements between 1 to 12: "))
for i in range(len(a)):
    if a[i] > 10: 
        a[i] = 10 
print(a)
```

### Write a program to enter numbers and then check if a number is present in the list. 

```py 
a = eval(input("Enter the elements for the list: "))
n = int(input("Enter the number to check: "))
for i in range(len(a)): 
    if a[i] == n: 
        print(f"This number is present in {i+1} position in the list.")
    else: 
        print("This number is not present in the list.")
```

# 11/10/2023

### Write a program to input elements in a list and calculate the number of odd and even numbers. 

```py 
a = eval(input("Enter the elements in the list: "))
odd = even = 0 

if i in range(len(a)):
    if a[i]%2 == 0: 
        even += 1 
    else:
        odd += 1 

print("Total odd numbers:", odd)
print("Total even numbers:", even)
```

### Write a program to ingut elements in a list and find the largest number. 

```python
a = eval(input("Enter the elements: "))
l = 0 

for i in range(len(a)):
    if a[i]>l: 
        l = a[i]
print("The largest number is:", l)
```

### Write a program to input elements in a list and find the lowest number. 

```py 
a = eval(input("Enter the elements: "))
s = a[0] 

for i in range(len(a)):
    if a[i]>l: 
        s = a[i]
print("The smallest number is:", s)
```

### Write a program to input the elements in a list and print the summation of the list followed by the summation of the odd numbers and the summation of even numbers. 

```py 
a = eval(input("Enter the elements: "))
so=se=sl=0

for i in range(len(a)):
    if a[i]%2 == 0: 
        se += a[i]
    else: 
        so += a[i]
    sl += a[i]


print("List summation:", sl)
print("Odd summation:", so)
print("Even summation:", se)
```

# 14/10/2023

- Adding single element  
`<listName>.append(<value>)`

- Adding more than 1 element  
`<listName>.extend([<elements>])`

- Finding largest value in list  
`max(<listName>)`

- Finding smallest value in list  
`min(<listName>)`

- Finding the sum of elements in list  
`sum(<listName>)`

- Sort in ascending order  
`<listName>.sort()`

- Sort in descending order  
`<listName>.sort(reverse=True)`

- Reversing a list  
`<listName>.reverse()`

- Delete element based on index value  
`<listName>.pop(<address>)`

- Remove element based on face value  
`<listName>.remove(<value>)`

> **Note**: This only works for the first value that comes in order.

- Count number of similar elements on face value  
`<listName>.count(<value>)`

> Consider a value is counted that is not in the list, it will give the result as `0`

- Clear all elements of a list  
`<listName>.clear()`
