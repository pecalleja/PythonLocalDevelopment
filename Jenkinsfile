pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                script {
                    docker.image('python:3.13.2-alpine3.21').inside {
                        sh 'python --version'
                        sh 'pip --version'
                        sh 'pip freeze'
                    }
                }
            }
        }
    }
    post {
        always {
            echo "Pipeline execution finished."
        }
    }
}
