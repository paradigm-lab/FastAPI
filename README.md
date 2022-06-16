# FastAPI:
## A super fast python Web Framework

## Features:

* Automatic Docs
	- Swagger UI
	- ReDoc

* Just Modern Python
	- Python 3.6 with type using Pydantic library

* Based on open standards
	- JSON Schema
	- Open API

* Security and Authentication 
	- HTTP Basic
	- OAuth2 (Also with JWT Tokens)
	- API Keys in 
		- Headers 
		- Query parameters
		- Cookies, etc.

* Dependency Injection 

* Unlimited "Plug-ins"

* Tested (PyTest)

* Starlette Features
	- WebSocket support 
	- GraphQl support
	- In-process background tasks
	- Startup and shutdown events
	- Test client build on request
	- CORS, GZip, Static Files, Streaming responses.
	- Session and Cookie support

* SQL databases

* NoSQL databases

* GraphQL


## Server startup 
Start server: uvicorn main:app (Server, fileName/module Name:FastAPI Instance)
	Option: --reload
	pip3 or pip freeze "This will show all package installed in the venv interpreter"

## docs
	localhost:8000/docs "Testing the API"

## redoc
	localhost:8000/redoc "API documentation"

## Parameters
	Path parameter
	Query parameter

## Request Body
	Create the pydantic base Model
	Use the blog model in the parameter 
	Use the model to get the value

## Get the requirements.txt file
	python3 -m venv blog-env

	source blog-env/bin/activate

	pip3 install -r requirements.txt

## To start the blog module server
	uvicorn blog.main:app 
	Option: --reload

## Database Connection
	Pydantic Schema: "SQLAlchemy"
	ORM 
	Model & Table

## Exception & Status Code
	200 - OK
	201 - CREATED
	HTTPException


## Packages
	__init__.py (Required for the package concept) dunder __init__ file
	uvicorn app.main:app --reload

## Database
	Database is a collection of organized data that can be easily accessed and managed.
	We don't work or interact with database directly.
	Instead we make use of a software referred to as a Database Management System (DBMS)
	Popular DBMS:	Relational and NoSQL Databases
	Relational Database are MySQL, PostgreSQL, Oracle, SQL Server
	NoSQL Database are MongoDB, DynamoDB, Oracle, SQL server
	Structured Query Language(SQL)- Language used to communicate with DBMS

## Postgres 
	Each instance of postgres can be carved into multiple separate databases.
	By default every Postgres installation comes with one database already created called "postgres"
	This is important because Postgres requires you to specify the name of a database to make connection. 
	So there needs to always to one database.

## Tables
	A table represents a subject or event in an application. eg: Users, Products and Purchases

## Columns Vs Rows
	A table is made up of columns and rows
	Each Column represents a different attribute eg: id, name, Age, Sex
	Each row represents a different entry in the table eg: Unique user or Record

## Postgres DataTypes
	Databases have datatypes just like any programming language

	Data Type: Numeric, Text, bool, sequence
	Postgres: {Int, decimal, precision}, {Varchar, Text}, Boolean, array
	Python: {Int, Float}, String, boolean, list

## Primary Key 
	Is a column or group of columns that uniquely identifies each row in table
	Table can have one and only one primary key.
	The primary key does not have to be the ID column always. It's up to you to decide which column uniquely defines each record.
	Since an email can only be registered once, the email column can also be used as the primary key.
	Note: Each Entry must be unique, No DUPLICATES!!!!!

## Constraints
	A Unique constraint can be applied to any column to make sure every record has a unique value for that column
	
	Null constraints by default when adding a new entry to a database, any column can be left blank. When a column is left blank, it has a null value
	If you need column to be properly filled in to create a new record, a NOT NULL constraint can be added to the column to ensure that the column is never left blank

	
## psycopg2
	Psycopg is a PostgreSQL database adapter for the Python programming language. It conforms to DB-API 2.0 standard.
	It is designed for multi-threaded applications and manages its own connection pool.
	Postgres Database driver

## Note:
	Using Raw SQL to send queries to the database.


## Object Relational Mapper(ORM)
	Layer of abstraction that sits between the database and us
	We can perform all database operations through traditional python code. No more SQL!
	Abstracts the SQL complexity

## What can ORMs Do
	Instead of manually defining tables in postgres, we can define our tables as python models
	Queries can be made exclusively through python code. No SQL is necessary

## SQLALCHEMY 
	Sqlalchemy is one of the most popular python ORMs.
	It is a standalone library and has no association with FastAPI. It can be used with any other python web frameworks or any python based application.
	No any relationship with FastAPI and Not part of FastAPI.

