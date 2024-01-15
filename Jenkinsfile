pipeline {
    agent any
    stages {
        stages('Clone') {
            step{
                git branch: 'main', url: 'https://github.com/nhdang002/UIT-src.git'
            }
        }
    }
}