pipeline {
    agent any
    environment {
        WEBEX_BOT_TOKEN = credentials('webex-bot-token')
        WEBEX_ROOM_ID   = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNTZiNWZlZTAtZGU2Zi0xMWYxLWFkOGYtODVkNmNiYTYxZmVi' // Replace with your actual Room ID
    }
    stages {
        stage('Run Unit Tests') {
            steps {
                sh 'python3 -m unittest test_app.py'
            }
        }
    }
    post {
        success {
            script {
                sh 'pip install requests'
                sh 'python3 notify_webex.py "✅ Build Success! Jenkins successfully built and tested commit on GitHub."'
            }
        }
        failure {
            script {
                sh 'pip install requests'
                sh 'python3 notify_webex.py "❌ Build Failed! Check Jenkins console output."'
            }
        }
    }
}
