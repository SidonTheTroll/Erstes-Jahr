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


