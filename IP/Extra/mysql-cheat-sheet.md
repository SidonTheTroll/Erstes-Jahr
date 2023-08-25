# MySQL Cheat Sheet

## Basics 

- Connect to MySQL:  
`mysql -u username -p`

- Create **Database**:  
`CREATE DATABASE database_name;` 

- Use **Database**:  
`USE database_name;`

- Show **Databases**:  
`SHOW DATABASES;`

- Create **Table**:  
```
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);
```

- Show **Tables**:  
`SHOW TABLES;`

- Describe **Table**:  
`DESC table_name;`

## CRUD Operations 

- Insert **Data**:  
`INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);`

- Select Data:  
```
SELECT * FROM table_name;
SELECT column1, column2 FROM table_name WHERE condition;
```

- Update **Data**:  
`UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;`


## Query Modifiers 

- **Order by**:  
`SELECT * FROM table_name ORDER BY column_name [ASC|DESC];`

- **Limit**:  
`SELECT * FROM table_name LIMIT num_rows;`

- **Group by**:  
`SELECT column, COUNT(*) FROM table_name GROUP BY column;`

- **Join**: 
`SELECT * FROM table1 JOIN table2 ON table1.column = table2.column;`

## Advanced Concepts 

- **Indexes**:  
`CREATE INDEX index_name ON table_name (column_name);`

- **Foreign keys**:  
`ALTER TABLE table_name ADD FOREIGN KEY (column_name) REFERENCES parent_table(column_name);`


- **Aggregate Functions**:  
`SELECT AVG(column_name), SUM(column_name), MIN(column_name), MAX(column_name) FROM table_name;`

- **Subqueries**:  
`SELECT column FROM table_name WHERE column IN (SELECT column FROM another_table);`

- **Transactions**:  
``` 
START TRANSACTION;
-- SQL statements
COMMIT; -- or ROLLBACK;
```