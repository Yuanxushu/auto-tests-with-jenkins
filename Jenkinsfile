pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                script {
                    sh """
                        pip install -r requirements.txt > installations.log
                    """
                    try {
                        sh "pytest --html=report.html"
                    } catch (err) {
                        currentBuild.result = "FAILURE"
                    } finally {
                        echo "stash report.html"
                        stash includes: 'report.html', name: 'report', useDefaultExcludes: false, allowEmpty: true
                    
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                recipients = "chelseayuanxs@gmail.com"
                unstash 'report'
                emailext (
                    subject: "[JENKINS] Build ${currentBuild.currentResult}: Job ${env.JOB_NAME} # ${env.BUILD_ID}",
                    body:  '''${BUILD_LOG, maxLines=1000, escapeHtml=false}''',
                    to: recipients,
                    recipientProviders: [[$class: 'CulpritsRecipientProvider']],
                    attachmentsPattern: 'report.html',
                )
            
            }
        }
    }
}