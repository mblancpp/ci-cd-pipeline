pipeline {
    agent any
    environment {
        // This securely pulls your secret token from Jenkins Credentials manager
        WEBEX_BOT_TOKEN = credentials('webex-bot-token')
        // Set your Webex Room ID directly here or bind it as a credential too
        WEBEX_ROOM_ID   = 'YOUR_ROOM_ID_HERE'
    }
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
            sh '''
            curl -X POST "https://webexapis.com/v1/messages" \
                 -H "Authorization: Bearer ${WEBEX_BOT_TOKEN}" \
                 -H "Content-Type: application/json" \
                 -d "{\\"roomId\\": \\"${WEBEX_ROOM_ID}\\", \\"text\\": \\"✅ Jenkins Build SUCCESS: Python unit tests passed successfully!\\"}"
            '''
        }
        failure {
            sh '''
            curl -X POST "https://webexapis.com/v1/messages" \
                 -H "Authorization: Bearer ${WEBEX_BOT_TOKEN}" \
                 -H "Content-Type: application/json" \
                 -d "{\\"roomId\\": \\"${WEBEX_ROOM_ID}\\", \\"text\\": \\"❌ Jenkins Build FAILED: Check console logs.\\"}"
            '''
        }
    }
}
