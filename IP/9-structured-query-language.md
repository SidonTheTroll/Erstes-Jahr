# 19/08/23

- Search for database named 'school'

```
mysql> show databases like 'school';
        Empty set (0.00 sec)
```

- Create database named 'school'

```
mysql> create database school;
        Query OK, 1 row affected (0.10 sec)
```

- Search database named 'school'

```
mysql> show databases like 'school';
        +-----------------+
        |Database (school)|
        +-----------------+
        |School           |
        +-----------------+
        1 row in set (0.00 sec)
```

- Delete database named 'school'

```
mysql> drop database school;
        Query OK, 0 row affected (0.09 sec)
```

- Search database named 'school'

```mysql> show database like 'school';
        Empty set (0.00 sec)
```

---

# 23/08/23

- Switch current working database for queries and operations  
  `use database_name`

- Create table in a current working database.

```
create table table_name
        (name char(20),

```

- Describe a table within a database  
  `desc table_name;`

- Insert value in table

```
insert into table_name
        values(<values>)
```

- Select name and atten to show in a table

```
select Name,Atten
        from table_name;
```

---

# 25/08/23

$\underbar{Primary key}$: In SQL, a primary key is a unique identifier for a record in a table, ensuring each row has a distinct value, enabling data integrity and efficient retrieval.

- Assigning primary key

```
create table table_name
        (ID int not null primary key,
        Name char(20),
        class int);
```

- Create a non-null primary key  
`int not null primary key` 


--- 

# 26/08/23 

- Show table details:
`select * from table_name`

- Order table content alphabetically 
```
select * from tale_name 
	order by name_column;	-- add desc for descending 
```
- Order table content numerically 
``` 
select * from table_name 
	order by number_column;	-- add desc for descending 
```

---

# 02/09/23 

- Show required field condition  
`select field1, desc1, condition1, desc2, condition2 from table_name where condition1 = '{cond1}' or condition2 = '{cond2}'; `

- Show specific column data without dupes  
`select distinct column_name from table_name`

- Show data of characters with initials starting as mentioned character.  
`select column1, column2 from table_name where column1 like '{char}%';` 
