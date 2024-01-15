pipeline {
    agent none
    
    environment {
        DOCKER_IMAGE = 'nhdang002/UIT-src'  
    }
    stgae
    stages {
        stage('Checkout and Clone') {
            steps {
                script {
                    // Bước lấy mã nguồn từ repository Git
                   git branch: 'main', url: 'https://github.com/nhdang002/UIT-src.git'
                }
            }
        }

        stage('Build and Push Docker Image') {
            agent { node {label 'master'}}
            environment {
            DOCKER_TAG="${GIT_BRANCH.tokenize('/').pop()}-${GIT_COMMIT.substring(0,7)}"
        }
            steps {
                sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} . "
                sh "docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest"
                sh "docker image ls | grep ${DOCKER_IMAGE}"
                withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login --username $DOCKER_USERNAME --password-stdin'
                    sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                    sh "docker push ${DOCKER_IMAGE}:latest"
            }
        }
      }
        }

        stage('Run Model Tests') {
            steps {
                script {
                    // Bước chạy các bài kiểm thử cho mô hình
                    sh "pytest ./test_model.py"
                }
            }
        }

        stage('Deploy to Production') {
            steps {
                script {
                    // Bước triển khai mô hình vào môi trường sản xuất  
                    sh "kubectl apply -f ./production.yaml"
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished!"
        }
    }
}
