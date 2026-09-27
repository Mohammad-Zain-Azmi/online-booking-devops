# Online Booking System

## Project Objective

The Online Booking System is a web-based application developed for booking college events such as technical fests, cultural events, and career seminars.

The project demonstrates software development, automated testing, containerization, deployment, and CI/CD practices.

## Features

* View upcoming college events
* View event details
* Check available seats
* Book seats for an event
* Generate booking confirmation
* View all bookings
* Search bookings
* Responsive user interface
* Automated application testing
* Docker-based deployment
* Jenkins CI/CD automation

## Technology Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### Database

* SQLite

### Testing

* Pytest

### Version Control

* Git
* GitHub

### CI/CD

* Jenkins

### Containerization

* Docker
* Docker Compose

## Project Structure

```text
online-booking-devops/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── Jenkinsfile
├── README.md
│
├── templates/
│   ├── index.html
│   ├── event.html
│   ├── booking.html
│   ├── confirmation.html
│   └── bookings.html
│
├── static/
│   └── style.css
│
└── tests/
    └── test_app.py
```

## Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Mohammad-Zain-Azmi/online-booking-devops.git
cd online-booking-devops
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

```powershell
venv\Scripts\activate
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

### 5. Run the application

```powershell
python app.py
```

Open:

```text
http://localhost:5000
```

## Run Automated Tests

Run:

```powershell
python -m pytest
```

The project currently contains 9 automated tests covering the main application functionality.

## Build Docker Image

Build the Docker image:

```powershell
docker build -t online-booking-app .
```

## Run Docker Container

Run:

```powershell
docker run -d --name online-booking-app -p 5000:5000 online-booking-app
```

Open:

```text
http://localhost:5000
```

View container logs:

```powershell
docker logs online-booking-app
```

Stop the container:

```powershell
docker stop online-booking-app
```

## Run Using Docker Compose

Start the application:

```powershell
docker compose up --build
```

The application will be available at:

```text
http://localhost:5000
```

To run in the background:

```powershell
docker compose up -d
```

To stop the application:

```powershell
docker compose down
```

## DevOps Pipeline

The project follows this DevOps workflow:

```text
Developer
    ↓
GitHub
    ↓
Jenkins
    ↓
Checkout Source Code
    ↓
Install Dependencies
    ↓
Run Automated Tests
    ↓
Build Docker Image
    ↓
Deploy Docker Container
    ↓
Online Booking System
```

### Jenkins Pipeline Stages

1. Check Docker
2. Install Python dependencies
3. Run automated Pytest tests
4. Build Docker image
5. Deploy Docker container

## Automated Testing

The project uses Pytest for automated testing.

The current test suite contains 9 tests covering:

* Home page
* Event details
* Booking page
* Booking creation
* Bookings page
* Application functionality

The Jenkins pipeline successfully executes all 9 tests.

## Docker Deployment

Docker is used to package the application and its dependencies into a portable container.

The application exposes port:

```text
5000
```

The application is accessible through:

```text
http://localhost:5000
```

Docker Compose provides an easier way to build and start the application:

```powershell
docker compose up
```

## Team Contributions

### Member 1

* Backend/application development
* Flask application logic
* SQLite database integration

### Member 2

* Application functionality
* Project integration
* Development and testing support

##
