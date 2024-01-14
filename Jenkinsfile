pipeline {
    agent any
    stages {
        stages('Clone') {
            steps{
                git branch: 'main', url: 'https://github.com/nhdang002/UIT-src.git'
            }
        }
    }
}