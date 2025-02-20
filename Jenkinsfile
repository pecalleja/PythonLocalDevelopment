pipeline {
    agent {
        docker {
            image 'python:3.11-alpine'
        }
    }
    stages {
        stage('Test') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                pytest --maxfail=1 --disable-warnings --tb=short
                '''
            }
        }
    }
    post {
        always {
            sh 'echo "Pipeline execution finished."'
        }
    }
}
