pipeline {
    agent {
        docker {
            image 'python:3.13.2-alpine3.21'
        }
    }
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings --tb=short'
            }
        }
    }
    post {
        always {
            sh 'echo "Pipeline execution finished."'
        }
    }
}
