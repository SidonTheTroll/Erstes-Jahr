# Intro

**Database**: system that is used to keep records in a computer. 

- Collection of data is called a database which contains information about a particular enterprise. 
    - It can also store interrelated data for multiple applications. 

**A database can be defined as a collection of interrelated data stored together to serve multiple applications.**

# File Based Systems 

Databases are a norm for data storage. 

- Prior, data was stored in flat files or file based systems 

**File based system or flat databases stores all data in one big file** 

- Characteristics:
    - Stores all data in one big file 
    - No structure is associated with the data
    - Common data can be repeated many times 

File based systems may have duplicated data and stored differently in different department files. Various files use these for access and updating data and this leads to **Data Inconsistency**. 

## Limitations of File-based approach

### Difficulty in access

- No structure in storing data 
    - Leads to time consumption in editing

- For a file based system, applications have to be made to support that
    - This leads to inefficient accessing and inorganized data. 

### Data Redundancy

- It is the storage of same data across multiple instances in the database 
    - Typing it over and over take long time <br> 
- Database space is wasted with duplicated data 
- Leads to data inconsistency 

### Data Inconsistency

- It means having multiple copies of data that do not match (in terms of data and/or format)

### Data Isolation 

- It is when data of one file cannot be mapped to other related file in absence of links, mappings or common formats. 

### Data Dependence 

- If some essential parts of the database is changed or the format is altered, it may break the whole application as it won't accept the latest changes in the framework.

- The close relationship between the data and software makes it hard to maintain files. 

### Data Sharing Security/Control Issues

- No data access feature
    - All data is available to every user

# Introducing Database Systems 

"A Database System or a database is an organized collection of structured information, or data, typically stored electronically in a computer system at a central location."

- Database system doesn't keep separate copies of the same data. 
    - All data are stored in a central location that applications can access. 

- If a change is made, it will be only done to one file and the patch will be made to every application referring to it. 

## Database Management System 

- Also known as DBMS 

- DBMS:
    - Database 
    - Software 

It allows the person to store, manipulate and retrieve data in a variety of ways. 

Eg: Oracle, DB2, SQL Server, PostgreSQL, MySQL, etc. 

### Advantages of Database 

#### Reduction of data redundancy 

- All data is stored in a central location which makes sure that data remains consistent and secure. 

#### Reduction of data inconsistency 

- Makes sure that if data is copied due to technical error, updates are made to all of them automatically. 
