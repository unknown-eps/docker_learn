# Docker Learning Workspace

This repository serves as a comprehensive workspace for learning, practicing, and demonstrating Docker containerization concepts. It contains a variety of applications ranging from simple scripts to multi-container full-stack architectures, covering Dockerfiles, Docker Compose, networking, and volume management.

## 📂 Repository Structure

The workspace is organized into several distinct categories based on the complexity and purpose of the exercises.

### 1. Core Full-Stack Application
A primary exercise involving a decoupled frontend and backend, used to demonstrate networking, environment variables, and database connections.

*   **[example-frontend/](example-frontend/)**: A React application serving as the user interface.
*   **[example-backend/](example-backend/)**: A Go (Golang) server using the Gin framework. It connects to Redis and PostgreSQL.
*   **[joint_app/](joint_app/)**: A directory orchestrating the connection between the `example-frontend` and `example-backend` using Docker Compose.

### 2. Python Applications
*   **[setting_app/](setting_app/)**: A multi-container application demonstrating data persistence.
    *   **Backend**: FastAPI (Python) saving data to a file volume.
    *   **Frontend**: Streamlit interface.
*   **[video_download_compose/](video_download_compose/)** & **[imgur_download/](imgur_download/)**: Utility containers utilizing `yt-dlp`, Python, and FFmpeg to download media, demonstrating how to containerize command-line tools.

### 3. Introductory & Utility Images
*   **[first_images/](first_images/)**: Basic Dockerfiles (Alpine-based) to understand layers and `CMD` vs `RUN`.
*   **[install_curl_image/](install_curl_image/)**: A simple Ubuntu-based image demonstrating package installation (`curl`).
*   **[whoami/](whoami/)**: A lightweight HTTP service that prints its container ID, useful for testing load balancers and orchestration.
*   **[simple_server/](simple_server/)**: A basic Go web service used for testing port mapping.

### 4. Course Material Applications
Located in **[material-applications/](material-applications/)**, this directory contains various legacy or example projects used for specific exercises:
*   **rails-example-project**: A Ruby on Rails application.
*   **spring-example-project**: A Java Spring Boot application.
*   **scaling-exercise**: A calculator app designed to test load balancing and scaling.
*   **simple-web-service**: A versatile binary used to test logging, volumes, and arguments.

## 🛠 Technologies Covered

*   **Containerization**: Docker, Dockerfiles (Multi-stage builds).
*   **Orchestration**: Docker Compose (`docker-compose.yaml`, `compose.yaml`).
*   **Languages**: Go, Python, JavaScript (Node.js/React), Java, Ruby.
*   **Databases & Caching**: PostgreSQL, Redis.
*   **Web Servers**: Nginx (used as a reverse proxy/load balancer).

## 🚀 Getting Started

### Prerequisites
*   [Docker Engine](https://docs.docker.com/get-docker/)
*   [Docker Compose](https://docs.docker.com/compose/install/)

### Running an Example

Most sub-directories contain their own `Dockerfile` or `compose.yaml`.

**To run a single image (e.g., the simple server):**
```bash
cd simple_server
docker build -t simple-server .
docker run -p 8080:8080 simple-server
```

**To run a multi-container application (e.g., the joint app):**
```bash
cd joint_app
docker compose up --build
```

**To run the Python Setting App:**
```bash
cd setting_app
docker compose up
# Access Frontend at http://localhost:8501
# Access Backend at http://localhost:8000
```

## 📝 Key Concepts Demonstrated

1.  **Building Images**: Creating optimized images using `Alpine` and multi-stage builds (seen in [`example-backend`](example-backend ) and [`simple-web-service`](material-applications/simple-web-service )).
2.  **Networking**: Connecting frontend containers to backend containers using internal Docker networks.
3.  **Volumes**: Persisting data (logs, database files) so it survives container restarts (seen in [`compose_log_eg`](compose_log_eg ) and [`setting_app`](setting_app )).
4.  **Environment Variables**: Configuring applications dynamically at runtime without changing code (e.g., [`REACT_APP_BACKEND_URL`](example-frontend/src/util/pingpong.js ), `POSTGRES_HOST`).

## 📚 References

This workspace follows patterns and exercises often found in the [DevOps with Docker](https://devopswithdocker.com/) course (University of Helsinki).
