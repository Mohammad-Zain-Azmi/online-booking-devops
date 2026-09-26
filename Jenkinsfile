pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Docker') {
            steps {
                bat '"C:\\Users\\Mohammad Zain\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\Mohammad Zain\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\Mohammad Zain\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '"C:\\Users\\Mohammad Zain\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t online-booking-app .'
            }
        }

        stage('Deploy Docker Container') {
            steps {
                bat '"C:\\Users\\Mohammad Zain\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" rm -f online-booking-app 2>NUL || exit /b 0'
                bat '"C:\\Users\\Mohammad Zain\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" run -d --name online-booking-app -p 5000:5000 online-booking-app'
            }
        }

    }
}