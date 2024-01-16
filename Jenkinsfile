pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'jenkins/jenkins:latest'
        DOCKER_HUB_CREDENTIALS = 'docker-hub' // Credential ID for Docker Hub
    }

    stages {
        stage('Checkout and Clone') {
            steps {
                script {
                    git branch: 'main', url: 'https://github.com/nhdang002/UIT-src.git'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.withRegistry('https://hub.docker.com/', DOCKER_HUB_CREDENTIALS) {
                        def customImage = docker.build("${DOCKER_IMAGE}:${env.BUILD_NUMBER}")
                        customImage.push()
                    }
                }
            }
        }
"""
        stage('Run Trained Model') {
            steps {
                script {
                    // Add steps to run trained model if needed
                    sh "python run_trained_model.py ${MODEL_FILE}"
                }
            }
        }

        stage('Check for Code Duplication') {
            steps {
                script {
                    sh "python check_code_duplication.py"
                }
            }
        }"""

        stage('Deploy to Production') {
            steps {
                script {
                    // Add steps to deploy to production if needed
                    sh "kubectl apply -f ./production.yaml"
                }
            }
        }
    }

    post {
        success {
            echo "SUCCESSFUL"
        }
        failure {
            echo "FAILED"
        }
    }
}
