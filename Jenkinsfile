pipeline {
    agent any
    environment {
        WEBEX_BOT_TOKEN = credentials('webex-bot-token')
        WEBEX_ROOM_ID   = 'YOUR_WEBEX_ROOM_ID_HERE'
    }
    stages {
        stage('Test') {
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
                 -d "{\\"roomId\\": \\"${WEBEX_ROOM_ID}\\", \\"text\\": \\"✅ Jenkins Build SUCCESS!\\"}"
            '''
        }
        failure {
            sh '''
            curl -X POST "https://webexapis.com/v1/messages" \
                 -H "Authorization: Bearer ${WEBEX_BOT_TOKEN}" \
                 -H "Content-Type: application/json" \
                 -d "{\\"roomId\\": \\"${WEBEX_ROOM_ID}\\", \\"text\\": \\"❌ Jenkins Build FAILED!\\"}"
            '''
        }
    }
}
