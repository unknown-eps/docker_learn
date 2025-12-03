# Docker Compose Application with FastAPI Backend and Streamlit Frontend

This application consists of a FastAPI backend service and a Streamlit frontend service orchestrated with Docker Compose. The frontend communicates with the backend to save text data to a shared file.

## Architecture

- **Backend**: FastAPI application running on port 8000
  - Provides API endpoints for saving text data
  - Persists data to `usr.txt` file
- **Frontend**: Streamlit application running on port 8501
  - Provides a web interface to interact with the backend
  - Allows users to input text and save it via the backend API

## Prerequisites

- Docker (v18.09 or later)
- Docker Compose (v1.25.0 or later)

## How to Run

### 1. Clone or Download the Repository

```bash
# If you have the repository locally
git clone <repository-url>
cd <repository-name>
```

### 2. Run with Docker Compose (Recommended)

```bash
# Build and start the services
docker-compose up --build

# To run in detached mode (background)
docker-compose up --build -d
```

### 3. Access the Applications

After starting the services:

- **Frontend (Streamlit)**: http://localhost:8501
- **Backend (FastAPI)**: http://localhost:8000

### 4. API Endpoints

- `GET /health` - Health check for the backend
- `POST /save` - Save text data to file

### 5. Stop the Services

```bash
# Stop the services (if running in foreground)
# Press Ctrl+C

# Stop the services (if running in detached mode)
docker-compose down
```

## Docker Compose Services

- **backend**: FastAPI service with port 8000 exposed
  - File persistence via volume mapping (`./usr.txt:/app/usr.txt`)
  - Environment variable: `PYTHONUNBUFFERED=1`
- **frontend**: Streamlit service with port 8501 exposed
  - Communication with backend via `BACKEND_URL=http://backend:8000`
  - Depends on backend service

## Development

To make changes:

1. Modify the source code files (`backend.py` or `frontend.py`)
2. Rebuild and restart the services with:
   ```bash
   docker-compose down
   docker-compose up --build
   ```

## Files

- `docker-compose.yaml` - Docker Compose configuration
- `backend.dockerfile` - Dockerfile for the backend service
- `frontend.dockerfile` - Dockerfile for the frontend service
- `backend.py` - FastAPI backend application
- `frontend.py` - Streamlit frontend application
- `requirements.txt` - Python dependencies for both services
- `usr.txt` - Shared file for data persistence (created automatically)

## Troubleshooting

- If you encounter issues accessing the frontend, make sure the backend is running first (Docker Compose handles this dependency)
- Check service logs with `docker-compose logs -f`
- If changes aren't reflected, try rebuilding with `docker-compose up --build --force-recreate`