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
