- [1. Intro](#1-intro)
- [2. File Based Systems](#2-file-based-systems)
  - [2.1. Limitations of File-based approach](#21-limitations-of-file-based-approach)
    - [2.1.1. Difficulty in access](#211-difficulty-in-access)
    - [2.1.2. Data Redundancy](#212-data-redundancy)
    - [2.1.3. Data Inconsistency](#213-data-inconsistency)
    - [2.1.4. Data Isolation](#214-data-isolation)
    - [2.1.5. Data Dependence](#215-data-dependence)
    - [2.1.6. Data Sharing Security/Control Issues](#216-data-sharing-securitycontrol-issues)
- [3. Introducing Database Systems](#3-introducing-database-systems)
  - [3.1. Database Management System](#31-database-management-system)
    - [3.1.1. Advantages of Database](#311-advantages-of-database)
      - [3.1.1.1. Reduction of data redundancy](#3111-reduction-of-data-redundancy)
      - [3.1.1.2. Reduction of data inconsistency](#3112-reduction-of-data-inconsistency)
      - [3.1.1.3. Facilitates Sharing of Data](#3113-facilitates-sharing-of-data)
      - [3.1.1.4. Databases Enforce Standards](#3114-databases-enforce-standards)
      - [3.1.1.5. Ensures Data Security](#3115-ensures-data-security)
      - [3.1.1.6. Ensures Data Independence](#3116-ensures-data-independence)
  - [3.2. Converting from file system to DBMS](#32-converting-from-file-system-to-dbms)
  - [3.3. DBMS Key Concepts](#33-dbms-key-concepts)
    - [3.3.1. Database Schema](#331-database-schema)
    - [3.3.2. Database Instance](#332-database-instance)
    - [3.3.3. Metadata](#333-metadata)
      - [3.3.3.1. Data Dictionary](#3331-data-dictionary)
    - [3.3.4. Data Constraints](#334-data-constraints)
    - [3.3.5. Query](#335-query)
    - [3.3.6. Data Manipulation](#336-data-manipulation)
    - [3.3.7. Database Engine](#337-database-engine)
- [4. Relational Database Model](#4-relational-database-model)
  - [4.1. Components of a table](#41-components-of-a-table)
- [5. The Relational Model Terminology](#5-the-relational-model-terminology)
    - [5.0.1. Relation](#501-relation)
    - [5.0.2. Domain](#502-domain)
    - [5.0.3. Tuple](#503-tuple)
    - [5.0.4. Attributes](#504-attributes)
    - [5.0.5. Degree](#505-degree)
    - [5.0.6. Cardinality](#506-cardinality)
  - [5.1. Properties of a Relation](#51-properties-of-a-relation)
    - [5.1.1. Properties of Columns (Attributes)](#511-properties-of-columns-attributes)
      - [5.1.1.1. Sequence/Ordering of Columns is Insignificant](#5111-sequenceordering-of-columns-is-insignificant)
      - [5.1.1.2. Each Column has a Unique Name](#5112-each-column-has-a-unique-name)
    - [5.1.2. Properties of Rows (attributes)](#512-properties-of-rows-attributes)
      - [5.1.2.1. Each Row is Unique (distinct)](#5121-each-row-is-unique-distinct)
      - [5.1.2.2. The Sequence of Rows is Insignificant](#5122-the-sequence-of-rows-is-insignificant)
    - [5.1.3. Properties or Relations](#513-properties-or-relations)
      - [5.1.3.1. Values are Atomic](#5131-values-are-atomic)
      - [5.1.3.2. A column's values are from the same domain](#5132-a-columns-values-are-from-the-same-domain)
      - [5.1.3.3. Columns cannot contain empty values](#5133-columns-cannot-contain-empty-values)
  - [5.2. Keys in a Database](#52-keys-in-a-database)
    - [5.2.1. Primary Key](#521-primary-key)
    - [5.2.2. Candidate Key](#522-candidate-key)
    - [5.2.3. Alternate Key](#523-alternate-key)
    - [5.2.4. Foreign key](#524-foreign-key)
  - [5.3. Referential Integrity](#53-referential-integrity)
  - [5.4. Disadvantages of Databases](#54-disadvantages-of-databases)
- [6. Brief History of MySQL](#6-brief-history-of-mysql)
- [7. MySQL Database System](#7-mysql-database-system)
- [8. MySQL and SQL](#8-mysql-and-sql)
  - [8.1. Processing Capabilities of SQL](#81-processing-capabilities-of-sql)
  - [8.2. Classification of SQL Statments](#82-classification-of-sql-statments)
    - [8.2.1. DDL Commands](#821-ddl-commands)
    - [8.2.2. DML Commands](#822-dml-commands)
    - [8.2.3. TCL Commands](#823-tcl-commands)


# 1. Intro

**Database**: system that is used to keep records in a computer.

- Collection of data is called a database which contains information about a particular enterprise.
  - It can also store interrelated data for multiple applications.

**A database can be defined as a collection of interrelated data stored together to serve multiple applications.**

# 2. File Based Systems

Databases are a norm for data storage.

- Prior, data was stored in flat files or file based systems

**File based system or flat databases stores all data in one big file**

- Characteristics:
  - Stores all data in one big file
  - No structure is associated with the data
  - Common data can be repeated many times

File based systems may have duplicated data and stored differently in different department files. Various files use these for access and updating data and this leads to **Data Inconsistency**.

## 2.1. Limitations of File-based approach

### 2.1.1. Difficulty in access

- No structure in storing data

  - Leads to time consumption in editing

- For a file based system, applications have to be made to support that
  - This leads to inefficient accessing and inorganized data.

### 2.1.2. Data Redundancy

- It is the storage of same data across multiple instances in the database
  - Typing it over and over take long time <br>
- Database space is wasted with duplicated data
- Leads to data inconsistency

### 2.1.3. Data Inconsistency

- It means having multiple copies of data that do not match (in terms of data and/or format)

### 2.1.4. Data Isolation

- It is when data of one file cannot be mapped to other related file in absence of links, mappings or common formats.

### 2.1.5. Data Dependence

- If some essential parts of the database is changed or the format is altered, it may break the whole application as it won't accept the latest changes in the framework.

- The close relationship between the data and software makes it hard to maintain files.

### 2.1.6. Data Sharing Security/Control Issues

- No data access feature
  - All data is available to every user

# 3. Introducing Database Systems

"A Database System or a database is an organized collection of structured information, or data, typically stored electronically in a computer system at a central location."

- Database system doesn't keep separate copies of the same data.

  - All data are stored in a central location that applications can access.

- If a change is made, it will be only done to one file and the patch will be made to every application referring to it.

## 3.1. Database Management System

- Also known as DBMS

- DBMS:
  - Database
  - Software

It allows the person to store, manipulate and retrieve data in a variety of ways.

Eg: Oracle, DB2, SQL Server, PostgreSQL, MySQL, etc.

### 3.1.1. Advantages of Database

#### 3.1.1.1. Reduction of data redundancy

- All data is stored in a central location which makes sure that data remains consistent and secure.

#### 3.1.1.2. Reduction of data inconsistency

- Makes sure that if data is copied due to technical error, updates are made to all of them automatically.

#### 3.1.1.3. Facilitates Sharing of Data

- Individual pieces of data can be shared among several users and also making users see specific data.

#### 3.1.1.4. Databases Enforce Standards

- Ensures all the data are centrally stored and follows specific structure and format.

#### 3.1.1.5. Ensures Data Security

- DBMS ensures data security and privacy by ensuring access to the database is through proper channel and also by carrying out authorization checks whenever sensitive data access is attempted.

#### 3.1.1.6. Ensures Data Independence

- DBMS separates data descriptions and metadata from application programs, allowing changes to data structures without affecting the programs, ensuring data independence.

## 3.2. Converting from file system to DBMS

Things to keep in mind:

1. Relational databases do not store all the data in the same table
2. Repeated data is moved into its own table
3. Separated tables this way are linked through a common field in both the tables (called relationship)

Steps to convert table:

1. Firstly move all duplicated data into a separate table.
2. Establish relationship in the separated tables by adding a common field as we added Doctor ID field in the primary table, using which the records of the duplicate table can be accessed.

## 3.3. DBMS Key Concepts

### 3.3.1. Database Schema

- It is the representation of the structure or design of a database. It repsesents database tables, table structures along with inter-table relationships. Schema is also called visual or logical architecture of a database.

### 3.3.2. Database Instance

A database instance is a snapshot of a database that exists at a particular time, i.e. the data which is stored in the database at a particular moment of time is called instance of the database.  
These instances change over time

### 3.3.3. Metadata

- It refers to the data about the data.
- In DBMS context, the data in tables have certain properties and attributes, (type, length, description) that allow DBMS to process the data meaningfully. These are stored in Data Dictionary.

#### 3.3.3.1. Data Dictionary

- It contains metadata such as the definitions of all schema objects in the database (tables, views, indexes, datatypes,etc) along with information like: space allocated, default values of columns, integrity constraint information, user's name, privelages and roles along with other general information.

### 3.3.4. Data Constraints

Data stored in a database must fulfil some rules and conditions so that only validated and required data is stored. It is called data constraint.  
It makes sure that a set of rules are fulfiled that define valid data. 

- List of primary constraints:  
    1. NOT NULL 
    2. PRIMARY KEY
    3. UNIQUE
    4. CHECK
    5. DEFAULT
    6. FOREIGN KEY

### 3.3.5. Query

- A query is a type of command that retrieves data from a database stored in a server. It is written in SQL (specifically made for typing queries)
- It can either be select query or action query.

- Queries:
  - Select query: Requests data from a database from one or more tables.
  - Action query: Changes, updates or add data into databases.

### 3.3.6. Data Manipulation

- Data manipulation involves using action queries to insert, update, or delete data in database tables.

### 3.3.7. Database Engine

- A database engine is the core software within a DBMS that manages data operations in a database.

- Types:
  - Storage Engine: This component is responsible for storing and retrieving data from stable storage media, such as hard drives or SSDs. It ensures data durability and handles the physical aspects of data management.
  - Query Processor: The query processor is in charge of accepting, parsing, and executing SQL (Structured Query Language) commands. It interprets user queries, interacts with the storage engine to fetch or update data, and returns the results to the user or application.

# 4. Relational Database Model

- Data is organized into tables. These tables are called relations.
- A row in a table represents a relationship among a set of values.
- It is derived from the mathematical term **relation**.

- Rows of realtion are called tuples
- Columns are referred to as attributes.

## 4.1. Components of a table

- **Byte**: it is a group of eight bits and is used to store characters.

- **Data Item (Field)**: A data item is the smallest unit of named data. It may consist of any number of bits or bytes. A data item represents one type of information and is often referred to as a field or data element.

- **Record**: A record is a named collection of data items which represents a complete unit of information.

- **Table**: A table is a named collection of all occurances of a given type of logical record.

- **Other database models**:
  - Network Data Model
  - Hierarchial Data Model
  - Object Oriented Data Model

> **Only one field can have unique value. Such fields are called primary key.**

<br>

A relational data model is based on a collection of tables (relations). The user of the RDBMS may query these tables, insert new tuples, delete tuples and modify tuples.

There are several languages for expressing these operations such as relational query language and relational algebra.

# 5. The Relational Model Terminology

- This model was put forward by E.F. Codd of the IBM. Since then, it is considered very important concept of DBMS technology.

### 5.0.1. Relation

Relation is a table and has the following properties:

1. In any given column of a table, all items are of th esame kind whereas items in different columns may not be the same kind.
2. For a row, each column must have an atomic (indivisible) value and also for a row, a column cannot have more than one value.
3. All rows of a relation are distinct. That is, a relation does not contain two rows which are identical in every column. That is, each row, of the relation can be uniquely identified by its contents.
4. There is no order maintained for rows inside a relation. That is, we cannot retrieve anything by saying that from row number 5, column name is to be accessed.
5. The columns of a relation are assigned distinct names and the ordering of these columns is immaterial.

### 5.0.2. Domain

A domain is a pool of values from which the actual values appearing in a given column are drawn.

- It is said to be atomic if elements of the domain are considered to be individual units.

> An atomic domain means that the values within it are treated as indivisible, single units. In simple terms, you can't break them down into smaller pieces. For example, if you have a domain for "ages," each age is a single, whole number, like 25 or 30, and not something like "25 years and 6 months."

### 5.0.3. Tuple

A row of tables (realtions) are generally referred to as tuples.

### 5.0.4. Attributes

A column of tables (realtions) are generally referred to as attributes.

### 5.0.5. Degree

A relation's degree is determined by the number of attributes it has. If a relation has three attributes, we call it a "degree 3" relation. Likewise, if a relation has 'n' attributes, it's called a "degree n" relation. In simpler terms, the degree of a relation just tells us how many characteristics or properties are associated with that relation.

### 5.0.6. Cardinality

The number of tuples (rows) in a realtion is called the cardinality of the realtion.

## 5.1. Properties of a Relation

### 5.1.1. Properties of Columns (Attributes)

#### 5.1.1.1. Sequence/Ordering of Columns is Insignificant

This property states that the ordering of the columns in the relational table has no meaning. Columns can be retrieved in any order and in various sequences.

#### 5.1.1.2. Each Column has a Unique Name

Since the sequence of columns is insignificant, columns must be referred by name and not by position.

### 5.1.2. Properties of Rows (attributes)

#### 5.1.2.1. Each Row is Unique (distinct)

This property ensures that no two rows in a relational table are identical; there is at laest one column, or set of columns, the values of which uniquely identify each row in the table.

#### 5.1.2.2. The Sequence of Rows is Insignificant

This property states that the ordering of the rows in the relational table has no meaning. Rows can be retrieved in any order and in various sequences.

### 5.1.3. Properties or Relations

#### 5.1.3.1. Values are Atomic

Columns and rows in a relational table cannot contain groups of groups of arrays of values (a row cannot contain multiple values for a `phone_number` column). Exactly, a column must have one value of a row.

#### 5.1.3.2. A column's values are from the same domain

It means that all thn values of a calumn are of the same kind, i.e., from the same domain.

#### 5.1.3.3. Columns cannot contain empty values

Any column's value cannot be left blank.

> If thn value of thn column is unknown or unavailable, a legal blank value of **_NULL_** can be designated to represent missing value.

## 5.2. Keys in a Database

It is required to distinguish rows conceptually, for a database the difference among them must be expressed in terms of their attributes. That is the work of **KEYS**.

### 5.2.1. Primary Key

It is used ti assigne a tuple having a unique value for a distinguished field that are unique to that tuple.

If a primary key consists of more than one attribute, it is called **composite-primary-key**.

> The primary key is non-redundant (doesn't has duplicate values in the same realtion. )
> Non-primary-key attributes of a table can be referred to as **non-key attributes**

### 5.2.2. Candidate Key

If a realtion has more than one attribute possessing the unique identificatiob property, all such instances are called candidate key.

If there are two or more than two candidate keys, one of them can de defined as primary key.

### 5.2.3. Alternate Key

If there are multiple Candidate keys and one if them is defined as primary key, the rest of them are **alternate keys**.

### 5.2.4. Foreign key

A foreign key can be as an non-primary attribute which is the primary key in other table.

The table in which the foreign-key attribute exists is called the Foreign Table of Detail Table.

The table that defines Primary-key, which the _foreign-key_ of _detail-table_ refers to is called the **Primary table** or **Master Table** or the _parent table_ sometimes.

## 5.3. Referential Integrity

A referential integrity is a system of rules that a DBMS uses to ensure that relationships between records in related tables are valid, and that users don't accidentally delete or change related data.

- Referential integrity can be set when all the following conditions are met:

  - The matching field from the primary table is a primary key or has a unique index.
  - The related fields have the same data type.
  - Both tables belong to the same database. If the tables are linked tables, they must be of same DBMS format, and you must open the database in which they are stored to set referential integrity. Referential integrity can't be enforced for linked tables from databases in other formats.

- On setting up Referential Integrity, the following rules must be followed:
  - You can't enter a value in the foreign key field of the related table that doesn't exist in the primary key of the primary table. However, you can't enter a Null value in the foreign key, specifying that the records are unrelated.
  - You can't delete a record from a primary table if matching records exist in a related table.
  - You can't change a primary key value in the primary table, if that record has related records.

## 5.4. Disadvantages of Databases

- Security can be compromised without good controls.
- Integrity may be compromised without goot controls.
- Extra hardware may be required.
- Performance overhead may be significant.
- System is likely to be complex.

# 6. Brief History of MySQL

- MySQL is a freely available open source RDBMS that uses Structured Query Language.
- Information are stored in a table.
- A single MySQL database can contain many tables at once and store thousands of individual records.
- It provides rich set of features that support secure environment for storing, maintaining and accessing data.
- It was created and supported by MySQL AB, a company based in Sweden. This company is now a subsidary of Sun Microsystems, which holds the copyright to most of the codebase.
- On 20th April, 2009, Oracle Corp., which develops and sells the proprietary Oracle database, announced a deal to aquire Sun Microsystems.
- Chief inventor was Michael Widenius (aka Monty).
  - MySQL is named after his daughter '**My**'.
  - The logo dolphin's name is '**Sakila**'.

# 7. MySQL Database System

MySQL database system refers to the combination of a MySQL server instance and a MySQL database. It operates using client/server architecture in which the server runs on the machine containing the databases and client connects to the server over a network. MySQL is a multi-user database system, meaning several users can login simultaneously.

- Here:
  - The server listens for client requests coming in over the network and accesses database contents according to those requests and provides to the clients.
  - Clients are programs that connect to the database server and issue queries in a per-specified format.

<br>

- Features:
  1. **Speed**: If hardware is optimal, MySQL runs very fast.
  2. **Easy of use**: It has a high-performing and relatively simple database.
  3. **Cost**: MySQL is available free of cost. It is an "Open Source" database. It is a part of LAMP (Linux, Apache, MySQL, PHP/Perl/Python) environment, a fast and growing opens source enterprise software stack.
  4. **Query Language Support**: MySQL understands standards based SQL.
  5. **Portability**: It supports various OS and has been tested on different compilers.
  6. **Data Types**: It supports various types of data with fixed or variable length.
  7. **Security**: MySQL offers a privelage and password system that is very flexible and secure, and allows host-based verification. Passwords are secure because all password traffic is encrypted when you connect to a server.
  8. **Scalability and Limits**: MySQL can handle large databases. Real life examples include databases with 5 million to 5 billion rows.
  9. **Connnectivity**: Clients can connect to the server using various protocols.
  10. **Localizaiton**: The client provides error messages in many languages.
  11. **Clients and Tools**: MySQL provides several client and utility programs.

# 8. MySQL and SQL

In order to access data within the MySQL database, all programs and users must use SQL. SQL is a set of commands that is recognised by nearly all RDBMSs.

Usage of SQL has become a standard for most of RDBMSs. Though applications programs and MySQL tools often allow users to access database without directly using SQL, but these applications in turn must use SQL when executing the user's request.

SQL is a language that enables you to create and operate on relational databases, which are sets of related information stored in tables.

## 8.1. Processing Capabilities of SQL

1. **Data Definition Language (DDL)**: The SQL DLL provides commands for defining relatino schemas, deleting relations, creating indexes and modifying relation schemas.
2. **Interactive Data Manipulation Language (DML)**: The SQL DML includes a query language which includes also commands to insert, delete and modify tuples in the database.
3. **Embedded Data Manipulation Language**: The embedded form of SQL is designed to use within general-purporse programming languages such as python, C, CPP, etc.
4. **Authorization**: The SQL DDL includes commands for specifying access rights to relations and views.
5. **Integrity**: The SQL provides (liimited) forms of integrity checking. Future products and standards of SQL are likely to include enhanced features for integrity checking.
6. **Transaction Control**: SQL includes commands for specifying the beginning of and ending of transactions along with commands to have control over transaction processing.

## 8.2. Classification of SQL Statments

SQL, technically speaking, is a data sublanguage, i.e., it is a language used to interact with database only. It is different from other languages such as C, Cpp, javascript, etc.

### 8.2.1. DDL Commands

Data Definition Language (DDL) commands allow the user to perform tasks related to data definition.

Some of its functions are:

1. **Create, alter and drop schema objects**: These commands are used to create or define, change or delete objects such as a table, a view, and index, etc.
   - **ALTER** changes or modifies existing schema objects.
   - **DROP** deletes or removes schema objects.
   - More examples include: **CREATE TABLE, ALTER TABLE, DROP TABLE, CREATE INDEX, ALTER INDEX, RENAME TABLE, TRUNCATE, etc.**
2. **Grant and revoke privileges and roles**: This section of DDL commands are used to grant or revoke permissions or privileges to work upon schema objects. This section of commands are also known as **Data Control Language (DDL)**
   - **GRANT** gives a user certain permissions.
   - **REVOKE** takes away the privileges.
3. **Maintenance Commands**: This section of DDL commands aer used to analyse information on a table with an aim of maintaining it.
   - Some commands are: **ANALYZE TABLE, CHECK TABLE, REPAIR TABLE, RESTORE TABLE, etc**

### 8.2.2. DML Commands

By data manipulation, it means:

- The retrieval of information stored in the database.
- The insertion of new information into the database.
- The deletion of information from the database.
- The modification of data stored in the database.

- DMLs are to two types:
  - **Procedural DML**: requires user to specify what data is needed and how to get it.
  - **Non-procedural DML**: requires a user to specify what data is needed without specifying how to get it.

Data Manipulation Language (DML) commands are used to manipulate data, i.e., DML commands query and manipulate data in existing schema objects. Its commands include: **INSERT INTO, UPDATE, DELET, SELECT, LOCK TABLE, etc.**

### 8.2.3. TCL Commands

A transaction is one complete unit of work, eg., preparing report-card for a student is a transaction, which involves many steps.

A transaction is successfully completed (known as COMMIT) if and only if all its constituent steps are successfully completed. To manage and control the transactions, the transaction control commands (TCL) are used. These commands manage changes made by DML commands.

- Some examples is TCL commands are:
  - **COMMIT**: makes all the changes made by statments issued, permanent.
  - **ROLLBACK**: in undoes all changes since the beginning of a transaction or since a savepoint.
  - **SAVEPOINT**: it marks a point upto which all earlier statements have been successfully completed and if required - in case of failure - one may undo the changes, i.e., rollback up to this very point.
  - **SET TRANSACTION**: It establishes properties for the current transactions.
