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

**`use database_name;`**: switch current working database for queries and operations  
**`create table table_name`**: create a table in a current working database.

> **`(name char(20),`**: create dividision _name_ and limit it to 20 characters.

**`desc table_name;`**: describe a table within a database  
**`insert into table_name`**: insert values in table

> **`values(<values>)`**: insert values in a table

**`select Name,Atten`**: select values name and atten for display in database.

> **`from table_name;`** show table contents with presets

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

`int not null primary key` creates a non-null primary key. 

