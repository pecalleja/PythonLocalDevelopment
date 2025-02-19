pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                script {
                    docker.image('python:3.13.2-alpine3.21').inside {
                        sh 'pip install --upgrade pip'
                        sh 'pip install -r requirements.txt'
                        sh 'pytest --maxfail=1 --disable-warnings --tb=short'
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
