# FastAPI Todo API with Docker

## Overview

This project is a RESTful Todo API built using **FastAPI** and **MongoDB**. It supports user authentication using JSON Web Tokens (JWT), allowing authenticated users to manage their own todo items securely.

The project also demonstrates how to containerize a FastAPI application using **Docker** and **Docker Compose**, making it easy to run the API and MongoDB together in a consistent environment.

---

## Features

* User registration
* User login with JWT authentication
* Password hashing using Passlib and Bcrypt
* Protected API endpoints
* Create Todo
* Retrieve all Todos
* Retrieve a Todo by ID
* Update Todo
* Delete Todo
* MongoDB integration using Motor (Async MongoDB Driver)
* API documentation with Swagger UI
* Unit testing with Pytest
* Environment variable configuration using `.env`
* Dockerized application
* Docker Compose configuration for FastAPI and MongoDB

---

## Technologies Used

* Python
* FastAPI
* MongoDB
* Motor
* Pydantic
* JWT (python-jose)
* Passlib
* Bcrypt
* Uvicorn
* Docker
* Docker Compose
* Pytest

---

## Project Structure

```
project/

├── routers/
│   ├── users.py
│   └── todos.py
│
├── tests/
│   ├── test_users.py
│   └── test_todos.py
│
├── auth.py
├── database_connection.py
├── dependencies.py
├── main.py
├── models.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .env
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Create and activate a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
MONGO_URI=mongodb://localhost:27017
DATABASE_NAME=todo_db

SECRET_KEY=mysecretkey123
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

API will be available at:

```
http://localhost:8000
```

Swagger Documentation:

```
http://localhost:8000/docs
```

ReDoc Documentation:

```
http://localhost:8000/redoc
```

---

## Running Tests

Execute all tests using:

```bash
pytest
```

---

# Docker

## Build the Docker Image

```bash
docker compose build
```

or

```bash
docker compose up --build
```

---

## Start the Containers

```bash
docker compose up
```

---

## Stop the Containers

```bash
docker compose down
```

---

## Docker Services

The project consists of two containers:

* **API Container** – Runs the FastAPI application using Uvicorn.
* **MongoDB Container** – Stores application data.

Docker Compose automatically creates a network so the API can communicate with MongoDB.

---

## Authentication Flow

1. Register a new user.
2. Login using your username and password.
3. Receive a JWT access token.
4. Authorize using the token in Swagger UI.
5. Access protected Todo endpoints.

---

## API Endpoints

### User

| Method | Endpoint          | Description                 |
| ------ | ----------------- | --------------------------- |
| POST   | `/users/register` | Register a new user         |
| POST   | `/users/login`    | Login and receive JWT token |

### Todo

| Method | Endpoint      | Description       |
| ------ | ------------- | ----------------- |
| POST   | `/todos/`     | Create a new Todo |
| GET    | `/todos/`     | Get all Todos     |
| GET    | `/todos/{id}` | Get Todo by ID    |
| PUT    | `/todos/{id}` | Update Todo       |
| DELETE | `/todos/{id}` | Delete Todo       |

---

## Security

* Passwords are securely hashed before storage.
* JWT authentication protects Todo endpoints.
* Secret keys and database configuration are stored using environment variables.

---

## Learning Objectives

This project demonstrates:

* Building REST APIs with FastAPI
* JWT-based authentication
* MongoDB integration
* Asynchronous database operations
* API testing with Pytest
* Environment configuration using `.env`
* Docker containerization
* Multi-container applications with Docker Compose

---

## Author

Created as part of a FastAPI backend development project to practice API development, authentication, testing, documentation, and Docker deployment.
