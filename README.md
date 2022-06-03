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

## docs
localhost:8000/docs
	-> Testing the API

## redoc
localhost:8000/redoc
	-> API documentation

## Parameters
	Path parameter
	Query parameter

## Request Body
	Create the pydantic base Model
	Use the blog model in the parameter 
	Use the model to get the value

## Pydantic Schema
	SQLAlchemy

## Get the requirements.txt file
	python3 -m venv blog-env

	source blog-env/bin/activate

	pip3 install -r requirements.txt