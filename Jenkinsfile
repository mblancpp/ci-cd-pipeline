pipeline {
    agent any
    environment {
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
        stage('Notify WebEx') {
            steps {
                sh """
                curl -X POST "https://api.ciscospark.com/v1/messages" \
                     -H "Authorization: Bearer ${env.WEBEX_TOKEN}" \
                     -H "Content-Type: application/json" \
                     -d '{"roomId": "${env.WEBEX_ROOM_ID}", "text": "CI/CD Pipeline Build SUCCESSFUL! Unit tests passed."}'
                """
            }
        }
    }
    post {
<<<<<<< HEAD
        success {
            sh '''
            curl -X POST "https://webexapis.com/v1/messages" \
                 -H "Authorization: Bearer ${WEBEX_BOT_TOKEN}" \
                 -H "Content-Type: application/json" \
                 -d "{\\"roomId\\": \\"${WEBEX_ROOM_ID}\\", \\"text\\": \\"✅ Jenkins Build SUCCESS: Python unit tests passed successfully!\\"}"
            '''
        }
=======
>>>>>>> Initial commit with app and unit tests
        failure {
            sh """
            curl -X POST "https://api.ciscospark.com/v1/messages" \
                 -H "Authorization: Bearer ${env.WEBEX_TOKEN}" \
                 -H "Content-Type: application/json" \
<<<<<<< HEAD
                 -d "{\\"roomId\\": \\"${WEBEX_ROOM_ID}\\", \\"text\\": \\"❌ Jenkins Build FAILED: Check console logs.\\"}"
            '''
=======
                 -d '{"roomId": "${env.WEBEX_ROOM_ID}", "text": "CI/CD Pipeline Build FAILED!"}'
            """
>>>>>>> Initial commit with app and unit tests
        }
    }
}
