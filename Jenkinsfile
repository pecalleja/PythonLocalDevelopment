pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                pytest --maxfail=1 --disable-warnings --tb=short
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline execution finished."
        }
    }
}
