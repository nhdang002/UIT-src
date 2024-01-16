pipeline {
    agent any
    
    environment {
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
                    withDockerRegistry(credentialsId: 'docker-hub', url: 'https://index.docker.io/v1/') {
                        sh 'docker build -t haidang1412/testmodel .'
                        sh 'docker push haidang1412/testmodel'
                    }
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
