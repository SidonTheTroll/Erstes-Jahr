# General Information 

- Time: 3 hours 
- Maximum marks: 70 

# Section A  

## Q1 
1. Number of attribute in a relation is called .........
    1. size 
    2. degree 
    3. cardinality 
    4. weight 
2. The column which has unique values in all the rows but is not a primary key is called .......... key.
    1. Candidate 
    2. Composite 
    3. Alternate 
    4. Foreign
3. Mismatched redundant copies of data is known as data .......
    1. Dependence 
    2. Redundancy
    3. Inconsistency 
    4. Isolation 
4. Which of the following functions print the output to the console? 
    1. Output()
    2. Print()
    3. Echo()
    4. print()
5. What is the value of the expression 100/25.
6. What is an Atom? 
7. An empty/null statement in Python is .........
8. What is debugging? 
9. In the Python statement x=a+5-b, a and b are 
    1.  operands 
    2.  operators 
    3.  expression 
    4.  equation 
10. Which of the following are legitimate variable declarations? 
    1.  My.var 
    2.  _Global
    3.  for 
    4.  while 
    5. Data items having fixed values are called ........
11. Which of the following can be used to create comments? 
    1.  // 
    2.  # 
    3.  "" 
    4.  "..." 
12. How would you view the structure of table demo? 
13. What is the error in the following statement: 
    -  UPDATE EMPL;
    1.  string 
    2.  Characters
    3.  Integers 
    4.  None of these
14. .......... can not be used as identifier names. 

# Section B 
## Q2.
1. What are the different divisions of SQL commands? Give examples. 
2. What are constraints? How is unique constraint different from Primary Key? 
3. What is the purpose of `range()` function? What are its argements? 
4. What is the difference between a keyword and an identifier? 
5. What do you mean by syntax error and semantics error? 

## Q3. Predict the output

### 1. 
```py 
x,y,z = True, False, False
a = x or (y and z)
b = (x or y) and z 
print(a,b)
```

### 2. 
```py
first=2 
second=3
third=first*second
print(first,second,third)
first=(first+second+third)
third=second*first 
print(first,second,third)
```

### 3. 
```py
a=3

b= 3.0 

print(a==b)

print(a is b)
```

### 4. 
```py
for x in range(3,12,2):
    print(x)
```

### 5. 
```py 
s='Sipo'
s1=s+'2'
s2=s*2
print(s1)
print(s2)
```

## Q4. Find the error in the following code fragments. 

### 1. 
```py 
temperature=90
Print temperature 
```

### 2. 
```python
a = 30 
b = a + b
print(a And b)
```

### 3. 
```python
x = 24 
4 = x 
```

### 4. 
```python
print(11+3)
print('11'+3)
```

### 5. 
```python
print("My name is",first_name)
```

## Evaluate the following statements

1. `0 or None and "or"` 
2. `False and 23` 
3. `23 and False`
4. `not(1==1 and 0!=1)` 


# Section C 
5. Write a python program to find sale amount, discount and net payable amount of an item with given quantity, price and discount(%).
6. Write a python program that accepts a character from the keyboard and determines whether it is a vowel or not. 
7. Write a python program that displays first 5 natural numbers and their sum. 
8. Write a python program that accepts 3 numbers from the user and find the largest among 3 numbers. 

# Section D 
## Q9.
### a. Write SQL query to create the following table  
Table: STUDENT 

| Column name | Data type | Size | Constraint | 
|-|-|-|-|
| ROLLNO | Integer | 4 | Constraint | 
| SNAME  | Varchar | 25 | Not Null | 
| Gender  | Char   | 1   | Not Null |
| DOB  | Date   |  | Not Null  | 
| FEES  | Integer   | 4   | Not Null | 
| HOBBY  | Varchar   | 15   | Null | 

### b. Consider a table Empl as given below

| empno | ename | job | mgr | hiredate | sal | comm | deptno |
|-|-|-|-|-|-|-|-| 
| 9369 | SMITH | CLERK | 8902 | 1990-12-18 | 800.00 | NULL | 20 |
| 8499 | ANYA | SALESMAN | 8698 | 1991-02-20 | 1600.00 | 300.00 | 30 | 
| 8521 | SETH | SALESMAN | 8698 | 1991-02-22 | 1250.00 | 500.00 | 30 | 
| 8566 | MAHADEVAN | MANAGER | 8839 | 1991-04-02 | 2985.00 | NULL | 20 |
| 8654 | MOMIN | SALESMAN | 8698 | 1991-09-28 | 1250.00 | 1400.00 | 30 | 
| 8698 | BINA | MANAGER | 8839 | 1991-05-01 | 8839 | 1991-05-01 | 2850.00 | NULL | 30 |
| SHIVANSH | MANAGER | 8839 | 1991-06-09 | 2450.00 | NULL | 10 | 
| 8888 | SCOTT | ANALYST | 8566 | 1991-12-09 | 3000.00 | NULL | 20 | 
| 8839 | AMIR | PRESIDENT | NULL | 1991-11-18 | 5000.00 | NULL | 10 | 
| 8844 | KULDDEP | SALESMAN | 8698 | 1991-09-08 | 1500.00 | 0.00 | 30 | 

1. Display all the records frrm table Empl. 
2. Display empno and ename of all employees from the Empl.
3. List all unique department numbers in the table. 
4. Display employee name, salary and department number who are not getting commission. 
5. List the details of employees who earn more commission than their salaries. 
6. How many job types are offered to employees. 
7. Display records of those employees whose ename ends with letter 'H'.