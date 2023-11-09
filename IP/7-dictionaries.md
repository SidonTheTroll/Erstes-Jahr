# 16/10/2023

```py
a = {2,4,5,7,9,3}
```
Places can swap in a dictionary 

- **Dictionary is a set of data in an unorganized way.**

| List   | Dictionary |
|--------------- | --------------- |
| 1. The square bracket mark the beginning and end of the list. | 1. The curly braces mark the beginning and end of the dictionary. |
| 2. List maintains the order of the elements.   | 2. Dictionary doesn't maintain the order of elements. There's no guarantee for maintaining order |
| 3. List cannot represent tabular form of data. | 3. Dictionary can represent tabular form of data. | 

### To write the following table, the code should be used. 

| | | | 
|-|-|-|
| A | 10 | 20 |
| B | 15 | 17 | 

```py 
a = {'A': 10, 20; 'B': 15, 17}
A, B are the how header
```

## Characteristics of Dictionary 

1. It is an unordered set of elements.
2. Dictionaries are mutable.
3. While we're saving a tabular data, the row heading should be unique. Elements can be same. 

Q/ Create a dictionary and print it. 

```py
a {'Rohan': 'Assam'; 'Shalini': 'Kolkata'; 'Raja': 'Delhi'}
print(a)
```

Q/ Write a program to input two lists and make them a single dictionary. 

```py
a = ['one','two','three']
b = [1,2,3]

c = dict(zip(a,b))
print(c)
```

# 19/10/2023

```py
m = eval(input("Enter the player serial number and their points: "))

if 50.0 in m.values():
    print("Yes, someone has scored 50.0")
else:
    print("No, nobody has scored 50.0")
```

| Value | Key |
|--------------- | --------------- |
| 1  | 50.0   |
| 2  | 79.4   |
| 3  | 86.3   |
| 4  | 54.9   |

> The headers describe the type of value in a dictionary.


```py 
m = eval(input("Enter the player serial number and their points: "))

if 3 in m.keys(): 
    print("Yes, 3rd number player is in the list")
else: 
    print("No, 3rd player is not in the list.")
```

Q/ Write a program to input 5 students' name along with their marks and check a particular student is present in the list or not. 

```py 
student_data = {}

for i in range(5):
    name = input(f"Enter the name of student {i+1}: ")
    marks = float(input(f"Enter the marks of student {i+1}: "))
    student_data[name] = marks

search_name = input("Enter the name of the student you want to search: ")

if search_name in student_data:
    print(f"{search_name} is present in the list with marks: {student_data[search_name]}")
else:
    print(f"{search_name} is not present in the list.")
```

Q/ Write a program to print an existing dictionary in a tabular format. 

```py 
empl = {"John": {'Age': 30, 'Salary': 25000}, "Diya":{'Age': 28, 'Salary': 30000}}

for key in empl: 
    print("Employee:", key)
    print("Age:", str(empl[key]['Age']))
    print('Salary:', str(empl[key]["Salary"]))
```

# 02/11/2023

### Write a program to store name and marks of given number of students by user. Make a dictionary using these data. Now ask the user if the user if he wants to make any changes in the marks or not. If he wants, they change the mark of particular student.

```py 
dict = {}
n = int(input("Enter the number of students: "))

for i in range(n):
    name, mark = eval(input("Enter the name and marks of student: ", (i+1)))
    dict[name] = mark 

for name in dict: 
    praint(name, ':', dict[name])

y = input("Do you want to make any modification? Y or N: ")

if (y == 'Y'): 
    name = input("Enter the name of student: ")
    if name in dict:
        dict[name] = int(input("Enter the new mark: "))
        for name in dict: 
            print(name, ':', dict[name])
    else:
        print("This student is not in the list.")

else: 
    print("Thank you.")
```

# 03/11/2023

### Write a program to create a third dictionary from two dictionaries having some common keys, in way so that the values of common keys are added in the third dictionary. 

```py 
dct1 = {'1': 100, '2': 200, '3': 300}
dct2 = {'1': 300, '2': 200, '3': 400}

dct3 = dict(dct1)
dct3.update(dct2)

for i, j in dct1.items():
    for x,y in dct2.items(): 
        if i == x: 
            dct3[i] = (j+y)

print("Two given dictionaries are:")
print(dct1)
print(dct2)
print("The resultant dictionary")
print(dct3)
```

# 07/11/2023 

```py 
d = {'Name': "Rahul", 'Salary': 10000, 'Age': 45, 'Dept': 'Sales'}

# Prints raw data
print(d) # {'Name': "Rahul", 'Salary': 10000, 'Age': 45, 'Dept': 'Sales'}

# Print headers
print(d.keys()) # dict_keys(['Name', 'Salary', 'Age', 'Dept'])

d = {'Name': "Rahul", 'Salary': 10000, 'Age': 45}
c = {'Name': "Sonali", 'Salary': 4000, "Age": 20, 'Dept': 'Production'}

d.update(c) # Replace values with dictionary 'c'
# If heading are found to be unique in initial dictionary, the value will remain the same. 

c.clear() # deletes data is dictionary 

del(c) # Deletes dictionary 'c'
```

### 7.11 Consider already created dictionary M that stores roll numbers and marks. Write a program to input a roll number and delete it from the dictionary. Display error message if the roll number does not exist in the dictionary. 

```py 
M = {1:400, 2:420, 3: 480, 4: 222, 5:430}

print("Created dictionary")
print(M)
rno = int(input("Roll no. to be deleted?: "))

if rno in M: 
    del M[rno]
    print("Roll no.", rno, "deleted from dictionary.")
else:
    print("Roll no.", rno, does not exist in dictionary.)

print("Final dictionary")
print("M")
```

# 09/11/2023

## Adding Keys and Elements ouside a Dictionary

```py 
d = {"Name": 'Rahul', "Age": 24, "Salary": 10000}
d['Dept'] = 'Sales'
print(d) # {"Name": 'Rahul', "Age": 24, "Salary": 10000, 'Dept': 'Sales'}
```

## Creating sub categories 

```py 
d = {"Rahul": {'Age': 25, 'Salary': 10000, 'Dept': 'Sales'}, 'Amit': {'Age': 27, 'Salary': 12000, 'Dept': 'Market'}}
print(d) 

for key in d: 
    print(key,': ')
    print('Age:', str(d[key]["Age"]))
    print('Salary:', str(d[key]["Salary"]))
    print('Dept:', str(d[key]["Dept"]))
    print()
```
