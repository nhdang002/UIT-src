pipeline {
    agent none

    environment {
        DOCKER_IMAGE = 'nhdang002/UIT-src'
    }

    stages {
         stage("Test") {
        agent {
          docker {
            image 'python:3.8-slim-buster'
            args '-u 0:0 -v /tmp:/root/.cache'
          }
        }
        steps {
                sh "pip install poetry"
                sh "poetry install"
                sh "poetry run pytest"
                }
    }
        stage('Checkout and Clone') {
            agent any
            steps {
                script {
                    // Bước lấy mã nguồn từ repository Git
                    git branch: 'main', url: 'https://github.com/nhdang002/UIT-src.git'
                }
            }     
        }

        stage("build") {
      agent { node {label 'main'}}
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

        //clean to save disk
        sh "docker image rm ${DOCKER_IMAGE}:${DOCKER_TAG}"
        sh "docker image rm ${DOCKER_IMAGE}:latest"
        }
        }

        stage('Run Trained Model') {
            agent any
            steps {
                script {
                    // Bước chạy mô hình đã được huấn luyện
                    sh "python run_trained_model.py ${MODEL_FILE}"
                }
            }
        }

        stage('Check for Code Duplication') {
            agent any
            steps {
                script {
                    sh "python check_code_duplication.py"
                }
            }
        }

        stage('Deploy to Production') {
            agent any
            steps {
                script {
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