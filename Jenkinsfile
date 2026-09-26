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
                bat 'docker --version'
                bat 'where docker'
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

    }
}