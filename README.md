# FastAPI Recommendation System

This project is a FastAPI-based recommendation system. It uses a PostgreSQL database to store user information and recommends users based on their attributes using a nearest neighbors algorithm.

- [Project Structure](#project-structure)
  - [Main Components](#main-components)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Build and Run the Application](#build-and-run-the-application)
  - [Database Migrations](#database-migrations)
- [API Endpoints](#api-endpoints)
  - [Recommendations](#recommendations)
  - [Users](#users)
- [Development](#development)
  - [Install Dependencies](#install-dependencies)
  - [Run Migrations](#run-migrations)
  - [Run the Application](#run-the-application)
- [License](#license)

## Project Structure

```md
├── Dockerfile
├── alembic
│ ├── README
│ ├── env.py
│ ├── script.py.mako
│ └── versions
├── alembic.ini
├── app
│ ├── config.py
│ ├── database.py
│ ├── main.py
│ ├── models.py
│ └── recommendations
│ ├── dao.py
│ ├── recsys.py
│ ├── router.py
│ └── schemas.py
├── docker-compose.yml
├── entrypoint.sh
├── .env
├── requirements.txt
└── README.md
```

### Main Components

- **main.py**: Entry point of the FastAPI application.
- **database.py**: Configures the SQLAlchemy engine and session maker.
- **models.py**: Contains the SQLAlchemy models for the database tables.
- **config.py**: Handles configuration settings.
- **recsys.py**: Contains the recommendation system logic.
- **router.py**: Defines the API endpoints for the recommendations and user operations.
- **dao.py**: Data Access Object functions for interacting with the database.

## Getting Started

### Prerequisites

- Docker
- Docker Compose


### Build and Run the Application

1. **Build and start the application using Docker Compose**:

    ```sh
    docker-compose up --build
    ```

2. **Access the FastAPI documentation**:

    Open your browser and navigate to `http://localhost:8000/docs`.

### Database Migrations

Alembic is used for database migrations. The migrations are automatically generated and applied when the Docker container starts.

## API Endpoints

### Recommendations

- `GET /recommendations/{user_id}`: Get recommendations for a specific user.

### Users

- `GET /users/{user_id}`: Get a single user by ID.
- `GET /users`: Get all users.
- `POST /user`: Create a new user.


## Development

If you want to run the application locally without Docker:

### Install Dependencies

```sh
pip install -r requirements.txt
```

### Run Migrations

```sh
alembic revision --autogenerate -m "init"
alembic upgrade head
```

### Run the Application

```sh
uvicorn app.main:app --host $FASTAPI_HOST --port $FASTAPI_PORT
```

### License
This project is licensed under the MIT License.
