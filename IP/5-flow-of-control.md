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

### Make a pyramid

```py
a = 5
b = 2

for i in range(1,6):
    for j in range(1,a):
        print('', end=' ')
    for k in range(1,b):
        print('1', end='')

    a -= 1
    b += 2
    print()
```

---

# 10/08/23

```py
a = 5; b = 4

for i in range(1,5):
    for j in range(1,a):
        print(b, end = "")
        b -= 1
    print()
    a -= 1
    b = 4

# 4321
# 432
# 43
# 4
```

```py
a = 5; b = 1
for i in range(1,6):
    for j in range(1,a):
        print(" ", end = "")
    for k in range(1, i+1):
        print(b, end="")
        b += 1

    print()
    a -= 1
    b = 1

#     1
#    12
#   123
#  1234
# 12345
```

# 16/08/23

## While loop

```py
# Prints GTBA 5 times

i = 1
while(i<=5):
    print('GTBA')
    i+=1
```

```py
# Print multiplication table of 5

i = 1
s = 0
while(i <= 10):
    s = 5 * i
    print(f"5 X {i} = {s}")
    i += 1
```

```py
# Makes a right triangle with 1

i = 1
j = 1
while i <= 5:
    while j <= i:
        print("1", end=" ")
        j += 1
    print()
    i += 1
    j = 1
```

# 16/08/23

## Q/ Check from 1 to n if its multiples are odd or even.

```py
n = int(input('Enter the value of n: '))
m = int(input('Enter the value of m: '))

print(f'The following are the numbers those are divided by {m} from 1 to {n}:')

for i in range (1 , n + 1):
    if i % m == 0:
        if i % 2 == 0:
            print(f'{i}    (even)')
        else:
            print(f'{i}    (odd)')
```

## The same function in while loop

```py
n = int(input("Enter the value of n: "))
m = int(input("Enter the value of m: "))
print(f"The following are the numbers that those are divided by {m} from 1 to {n}")

i = 1

while i <= n:
    if i % m == 0:
        if i % 2 == 0:
            print(i, "(even)")
        else:
            print(i, "(odd)")
    i += 1
```

# 18/08/23

## Q/ Write a python program to check a given number is a palindrome number or not.

### Note:

A number is said to be palindrome when its reverse form is also same.  
Eg- 323 is a palindrome number

```py
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
```

```py
n = int(input("Enter to check perfect number: "))
r = int(str(n)[::-1])

if r == n:
    print("Yes, it is a perfect number.")
else:
    print("No, it is not a perfect number.")
```

## Q/ Write a program to check a given number is a perfect number or not.

### Note: a perfect number is a positive integer, which is equal to the sum of its divisors, excluding the number.

#### Eg-

Enter a number: 6  
The divisors of 6 are: 1, 2, 3  
Now, the summations of these divisors are: 1 + 2 + 3 = 6  
So we can say that 6 is a perfect number

```py
sum_of_fact = 0

n = int(input("Enter to check perfect number: "))

for i in range(1,n):
    if n % i == 0:
        sum_of_fact += i

if sum_of_fact == n:
    print("Yes it is a perfect number.")
else:
    print("It is not a perfect number.")
```

## Write a program to check if a given number is prime or not. 

```py 
n = int(input("Enter a number: "))
f = 0 
for i in range(1,n+1): 
    if (n%i==0): 
        f += 1 
if (f==2): 
    print("It is a prime number.")
else: 
    print("It is not a prime number.")
```

## Write a program to print all prime number within a given range. 

```py 
a = int(input("Enter the first number of the range: "))
b = int(input("Enter the last number in the range: "))

prime_numbers = []

for num in range(a, b + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)

print("Prime numbers within the range from", a, "to", b, "are:", prime_numbers)

```
