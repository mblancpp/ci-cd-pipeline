pipeline {
    agent any
    environment {
        WEBEX_BOT_TOKEN = credentials('webex-bot-token')
        WEBEX_ROOM_ID   = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNTZiNWZlZTAtZGU2Zi0xMWYxLWFkOGYtODVkNmNiYTYxZmVi'
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
            sh '''
                curl -s -X POST https://webexapis.com/v1/messages \
                -H "Authorization: Bearer ${WEBEX_BOT_TOKEN}" \
                -H "Content-Type: application/json" \
                -d "{\\"roomId\\": \\"${WEBEX_ROOM_ID}\\", \\"text\\": \\"✅ Jenkins Build SUCCESS!\\"}"
            '''
        }
        failure {
            sh '''
                curl -s -X POST https://webexapis.com/v1/messages \
                -H "Authorization: Bearer ${WEBEX_BOT_TOKEN}" \
                -H "Content-Type: application/json" \
                -d "{\\"roomId\\": \\"${WEBEX_ROOM_ID}\\", \\"text\\": \\"❌ Jenkins Build FAILED!\\"}"
            '''
        }
    }
}
