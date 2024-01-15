pipeline {
    agent any
    stages {
        stage('Git clone and setup') {
            steps{
                git branch: 'main', url: 'https://github.com/nhdang002/UIT-src.git'
            }
        }
    }
}