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
