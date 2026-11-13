pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh 'python3 -m unittest test_app.py'
            }
        }
    }
    post {
        success {
            script {
                sh 'python3 notify_webex.py "✅ Build Success! Jenkins successfully built and tested commit on GitHub."'
            }
        }
        failure {
            script {
                sh 'python3 notify_webex.py "❌ Build Failed! Check Jenkins console output."'
            }
        }
    }
}
