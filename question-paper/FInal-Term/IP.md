# General Guidelines 

- Time: 3 hours 
- Maximum Marks: 70 

# Section A 

## Q1. 

1. An atom in Python is something that has a .......... 
2. State TRUE/FALSE: Customized software is a type of system software. 
3. What is the difference between RAM and ROM? 
4. What does a cross-platform language mean? 
5. ......... is a set of valid characters that a language can recognize. 
6. Microphone (mic) is a ......... device. 
7. A table in MySQL is also known as ..........
8. What is the function of memory? 
9. List some of the cloud-based services that you are using at present. 
10. Which operator tests the column for the absence of data (i.e., NULL values)? 
    1.  EXISTS operator 
    2.  NOT operator 
    3.  IS operator 
    4.  None of these 
11. The ........ clause of SELECT query allows us to select only those rows in the result that satisfy a specific condition. 
    1.  having 
    2.  where 
    3.  from 
    4.  distinct 
12. Meta-data refers to ........
13. Which of the following is not a characteristic of a computer? 
    1.  Diligence 
    2.  I.Q. 
    3.  Accuracy 
    4.  Versatility 
14. Char is a ...... length data type.
    1.  Fixed 
    2.  Variable 
    3.  Simple 
    4.  Integer 
15. Which of the following attributes cannot be considered as a choice for primary key? 
    1.  ID 
    2.  Street 
    3.  Dept_id 
    4.  License number 

## Q2.
1. Differentiate between pop() and remove() method of list. 
2. What are iteratioin statements? Name the iteration statements provided by Python.
3. What is Artificial Intelligence (AI)? What are some applications of AI? 
4. What is Robotics? How are Robots useful? 
5. What is DDL? List some commands used in DDL. 
6. What is the difference between the following operations on list1: 
    1. List1=list1*2
    2. list1*2 1
7. Differentiate between proprietary software and freeware software. Name one software of each type. 

# Section-B 

## 1. 
``` python
for i in range(0,10):
    pass 
print(i)
```

## 2. 
```python
a,b = 10,50
if b % a == 0: 
print(b//4)
print(a/2)
else: 
print(a**2)
print(b%3)
```

## 3. 
```python
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

my_list[2:3] = []

print(my_list)

my_list[2:5] = []

print(my_list)
```

# Section C 

4. Write a python program to find the largest number among the three inputted numbers. 
5. Write a python program to display the sum of even numbers up to number n entered by user. 
6. Write a python program that reads a number of seconds and prints it in form: min and seconds. [Hint use // and % to get minutes and seconds]

### 7.

| Column_name  | Datatype(Size)   | Constraint   |
| :---- | :---- | :---- |
| Id | Integer(4) | Primary Key | 
| First_name  | Varchar(20)   | Not null   |
| Last_name  | Varchar(20)   |    |
| Address  | Varchar(25)   |    |
| Phone  | Integer(10)   | Not Null   |

Write the SQL command to create the above table "Customer" with constraints.

8. Write a python program to check whether entered year is a leap year or not. 

# Section D 

### 9. 
Consider the following list- List1=[2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

Write commands for the following: 
1. Add 20 to the list. 
2. Insert 4 to the third positon.
3. Sort the elements of the list.
4. Count how many times 6 is available.
5. Delete all elements form 3rd to 9th position.
6. Delete 11 from the list. 
7. Search the position of 13 in the list.
8. Find the maximum value of the list.
9. Find the length of the list.
10. Delete all the elements of the list.

<br>

10. Write a program to enter 5 subjects marks and calculate the total of entered marks and grades. If the total marks are more than 250 then the grade is "A" otherwise "B". 

### 11. 

Create a table- VOTER with following structure and Insert at least four rows into it.

| Filed name | Date Type/size   | 
| :---- | :---- |
| Vno | Integer(4) | 
| Vname | Varchar(30) | 
| Age | Integer(3) | 
| Address | Varchar(30) | 
| Phone | Double(16) | 

Write the SQLs for the following:

1. To list Vno, Vname, Age for all the voters. This information should be sorted on Age.
2. To list all the voters where address is "Guwahati" 
3. To add one new column named VGender datatype char(1).
4. To list voters where address is "Delhi" but age is between 20 and 30. 
5. To delete the records of all those who are either residing in "Delhi" or whose Age > 35. 
6. To change the age to 45 where Vname contains the word "Kumar". 