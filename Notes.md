# Notes

## Introduction

In this course, we will be learning SQL and ORM (Object Relational Mapping). You will also gain hands-on experience with GitHub, HTML, CSS, and Python.

### Learning Objectives and Syllabus

By the end of this course, you will be able to:

- Describe what a database is and how to model data.
- Compose SQL queries to insert, select, update, and delete data in a database.
- Understand Object Relational Model (ORM).
- Develop database-powered applications using Django.
- Deploy your Django app on the cloud.

#### Syllabus

**Module 1: Introduction to Databases**

- Course Introduction Video
- Module Intro & Objectives
- Introduction to Databases and Database Management Systems
- Relational Databases
- Relational Data Concepts
- Hands-on Lab: Entity-Relationship Data Modeling
- Practice Quiz: Introduction to Databases
- SELECT Statement
- Hands-on Lab: Simple SELECT Statements
- COUNT, DISTINCT, LIMIT
- INSERT Statement
- UPDATE and DELETE Statements
- Hands-on Lab: INSERT, UPDATE, and DELETE
- Basic SQL Statements Summary
- Practice Quiz: Basic SQL Statements
- (Optional) Overview - Creating Tables, Sorting Results, and Join
- (Optional) CREATE Table Statements
- (Optional) ALTER, DROP, and Truncate Table
- (Optional) Sorting Result Sets
- (Optional) Join Overview
- (Optional) Summary
- (Optional) Practice Quiz: Creating Tables, Sorting Results, and Joins

**Module 2: ORM: Bridging the Gap between the Real World and Relational Model**

- Module Introduction and Learning Objectives
- Object-Relational Mapping (ORM)
- Django Model
- Hands-on Lab: Create a Django project in Theia
- Optional Lab: Create a Standalone Django ORM Project Template
- Quiz: ORM and Django Model
- Django CRUD
- Hands-on Lab: CRUD on Django Model Objects
- Quiz: Django Model API
- Related Objects
- Hands-on Lab: Query Spanning Relationships
- Module Summary
- Practice Quiz
- Graded Quiz

**Module 3: Full-stack Django Development**

- Module Introduction and Learning Objectives
- Django Model-View-Template pattern
- Quiz: MVC and Django MVT pattern
- Create a Django app
- Hands-on Lab: Create your first Django App
- Django Admin Site
- Hands-on Lab: Django Admin
- Django Views
- Django Templates
- Hands-on Lab: Views and Templates
- Module Summary
- Practice Quiz
- Graded Quiz

**Module 4: Consolidate and Deploy Your Django App**

- Module Introduction and Learning Objectives
- Class-based and Generic Class Views
- Quiz: Function-based and Class-based View
- Hands-on Lab: Class-based and Generic Views
- Django Authentication System
- Hands-on Lab: User Signup and Signin
- Bootstrap integration
- Hands-on Lab: Bootstrap Integration
- Manage Static Files
- Deploy your Django App on IBM Cloud
- Hands-on Lab: Deploy your Django app on IBM Cloud Foundry
- Module Summary
- Practice Quiz
- Graded Quiz

**Final Exam and Project: Enhance Online Course App with New Features**

- Final Exam
- Final Project Overview and Scenario
- Hands-on Lab 1: Understand the Project Requirements and Get the Final Project Template
- Hands-on Lab 2: Build Course Exam Related Models and Templates
- Hands-on Lab 3: Build Views and Templates to Submit, Display, and Evaluate Exam Results
- Hands-on Lab 4: Test and Deploy Your App on IBM Cloud
- Peer Review

## What is SQL

SQL stands for

 Structured Query Language. It is a language used to interact with databases. You can use SQL to perform various operations such as creating databases, creating tables within databases, retrieving data from tables, updating tables, and more. SQL is an ANSI (American National Standards Institute) standard. It provides capabilities to execute queries, insert records, update records, create databases and tables, and delete tables.

## What is a Database

A database is a collection of related data. Data is a collection of facts and figures that can be processed to produce information. In a database, data is organized in a manner that allows a computer program to quickly retrieve desired pieces of data. You can think of a database as an electronic filing system.

## Basic SQL Commands

- Create a table
- Insert
- Select
- Delete

## Relational Databases

Data in relational databases is stored in rows and columns, similar to a table. The data is related to each other through common fields. Relational databases allow you to retrieve data from multiple tables using a single query, providing a better understanding of the whole picture. Relational databases offer flexibility, reduce redundancy, provide meaningful information, and ease of backup and restore. They are well-suited for OLTP applications, data warehouses, and IoT systems. However, they don't work well with semi-structured or unstructured data, and migration requires identical schemas and data types.

## Relational Data Concepts

Relational model is the most used data model. 

Gives data independance. 
Entity-Relationship model
A tool to design relational databases

Attributes tell us more about an entity. 

When mapping the entities become a table. 

Attributes get translated into columns

A primary key uniquesly identifies a specific row in a table. 


## Lesson Summary

Structured Query Language, or SQL, was designed for managing data in relational databases and is useful in handling structured data. 
Data is a collection of facts in the form of words, numbers, and pictures. 
A database is a repository of data that provides functionality for adding, modifying, and querying data. 
Relational databases store tabular data as collections of related items, with columns containing item properties. 
The basic SQL statements are CREATE TABLE, INSERT, SELECT, UPDATE, and DELETE. 
Relational databases are ideal for the optimized storage, retrieval, and processing of large volumes of data. 
RDBMS is a mature and well-documented technology, providing flexibility, reduced redundancy, ease of backup and disaster recovery, and ACID compliance. 
An Entity-Relationship model is a tool for designing relational databases. Entities become tables, and attributes are translated into columns. 

## Using the SELECT Statement

SELECT statement are used to read and modify data. 

The output is called a result set

 E.g: db2 => select book_id, title, edition, year, price, ISBN

 ### Restricitng the Result Set: WHERE Clause

 - Restricts the result set
 - Always requires a Predicate:

''' select book_id, title from Book
        WHERE predicate '''

Predicate evaluates to <True> <False> or <unknown>

Used in the search conditoon of the Where clause


e.g. ``` 

db2 => select book_id, title from Book
        WHERE book_id='B1'

```

Operaters:

- =
- >
- <
- >=
etc..




## COUNT, DISTRICT, LIMIT

### COUNT

<COUNT> - A built in fuction that retrevies the number of rows matching the query criteria.

Number of rows in a table:
``` select COUNT(*) from tablename ```

E.g How many Rows in the MEDALS table from Country is Canada:

``` select COUNT(COUNTRY) from MEDALS
            where COUNTRY = 'CANADA'
```

### DISTINCT

DISTINCT is used to remove duplicate values from a result set.

E.g List of unique countries that recieved GOLD medals:

``` 
select DISTINCT COUNTRY from MEDALS
        where MEDALTYPE = 'GOLD'
```

### LIMIT

<LIMIT> is used for restricting the number of rows retrieved from the database

e.g: Retrieve 5 rows in the MEDALS table for a particular year:

``` 
select * from MEDALS
        where YEAR = 2018 LIMIT 5
```

## INSERT statement

Adds rows to a table

1. Create the table (CREAT TABLE statement)

2. Populate table with data:
    > INSERT statement

