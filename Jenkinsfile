pipeline {
    agent any
    
    environment {
        DOCKER_HUB_CREDENTIALS = 'docker-hub' // Credential ID for Docker Hub
    }

    stages {
        stage('Clone') {
            steps {
                
                git branch: 'main', url: 'https://github.com/nhdang002/UIT-src.git'
            
            }
        }

        stage('Build Docker Image') {
            steps {
                    // Build Docker image
                    withDockerRegistry(credentialsId: 'docker-hub', url: 'https://index.docker.io/v1/') {
                        sh 'docker build -t haidang1412/mlops:test1 .'
                        sh 'docker push haidang1412/mlops'
                    
                }
            }
        }
        
    }
}
