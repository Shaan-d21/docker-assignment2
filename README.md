
# Quiz Application - FastAPI & PostgreSQL

## Overview
This is a Quiz Application backend built with FastAPI and PostgreSQL, containerized using Docker Compose. The application allows users to interact with a quiz system through an API.

## 🛠️ Tech Stack
- **FastAPI** (Backend framework)
- **PostgreSQL** (Database)
- **Docker & Docker Compose** (Containerization)

## Getting Started

### 1 Prerequisites
Ensure you have the following installed:
- **Docker** & **Docker Compose**
- **Git** 

### 2 Clone the Repository
```sh
git clone <your-repo-url>
cd <your-repo-folder>
```

### 3 Set Up Environment Variables
Create `.env` files based on the provided `db.env` and `backend.env`.

#### **db.env**
```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=root123
POSTGRES_DB=QuizApplicationDatabase
```

#### **backend.env**
```env
APP_ENV=production
APP_NAME=quiz_app
ADDRESS=0.0.0.0:8000
POSTGRES_USER=postgres
POSTGRES_PASSWORD=root123
POSTGRES_DB=QuizApplicationDatabase
POSTGRES_HOST=db  
POSTGRES_PORT=5432
DATABASE_URL=postgresql://postgres:root123@db:5432/QuizApplicationDatabase
```

### 4 Start the Application
Run the following command to build and start the services:
```sh
docker-compose up --build -d
```

This will start:
- `backend_service`: FastAPI application running on `http://localhost:8000`
- `db_service`: PostgreSQL database accessible on `localhost:5432`

### 5 Verify the Services
Check running containers:
```sh
docker ps
```

Check logs (optional):
```sh
docker logs backend_service
```

### 6 Access the Application
- **FastAPI Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Database (PgAdmin or CLI)**: Connect to PostgreSQL at `localhost:5432` using the credentials from `db.env`.

## Stopping the Application
To stop and remove the running containers:
```sh
docker-compose down
```

## Troubleshooting
### Issue: "Database does not exist"
- Ensure the database container is running: `docker ps`
- Recreate the containers: `docker-compose down && docker-compose up --build -d`

### Issue: "Connection refused on port 5432"
- Ensure PostgreSQL is running: `docker logs db_service`
- Check if another service is using port `5432`



