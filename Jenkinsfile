pipeline {
    agent { docker { image 'python:3.7' } }
    stages {
        stage('build') {
            steps {
                sh """
                    pip install -r requirements.txt
                """
                sh 'pytest'
            }
        }
    }
}

/************ brand portal API testing Jenkinsfile ************/
// pipeline {
//     agent {
//         label "master"
//     }
//     options { skipDefaultCheckout() }
//     stages {
//         stage('Init') {
//             steps {
//                 cleanWs()
//                 checkout scm
//                 stash name: 'repo', useDefaultExcludes: false
//             }
//         }

//         stage('Testing') {
//             agent {
//                 label "TL"
//             }

//             steps {
//                 cleanWs()
//                 unstash 'repo'
//                 script {
//                     if ("${HOST}".contains("staging" as java.lang.CharSequence)){
//                         mark = "staging"
//                     } else if ("${HOST}".contains("test" as java.lang.CharSequence)) {
//                         mark = "test"
//                     } else {
//                         mark = "live"
//                     }
//                     currentBuild.description = "Running ${mark} env"

//                     docker.image("python:3.7").inside("-v ${WORKSPACE}:/app -u root"){
//                         sh """
//                             rm -f /etc/localtime && ln -s /usr/share/zoneinfo/Asia/Singapore /etc/localtime
//                             cd /app && pip install -r requirements.txt
//                         """

//                         try {
//                             sh "pytest -m ${mark} -n 30 --durations=20 --reruns=1"
//                         } catch (err) {
//                             currentBuild.result = "FAILURE"
//                         } finally {
//                             sh """
//                                 python -c 'from libs.jira_issues import create_jira_api_issues; create_jira_api_issues("${HOST}")' || true
//                                 python -c 'from libs.jira_issues import create_jira_performance_issues; create_jira_performance_issues("${HOST}")' || true
//                                 python -c 'from libs.file import get_performance_html; get_performance_html("${HOST}")' || true
//                             """
//                             echo "stash performance.html"
//                             stash includes:'performance.html', name: 'performance', useDefaultExcludes: false, allowEmpty: true
//                         }
//                     }
//                 }
//             }
//         }
//     }
//     post {
//         always {
//             script {
//                 recipients = "sunh@seagroup.com, xin.zhang@shopee.com, cong.ma@shopee.com, jerry.leo@shopee.com, xushu.yuan@shopee.com"
//                 unstash 'performance'
//                 if ("${mark}" == "live") {
//                     echo "${mark}"
//                     emailext (
//                         subject: "[JENKINS] Build ${currentBuild.currentResult}: Job ${env.JOB_NAME} # ${env.BUILD_ID}",
//                         body:  '''${BUILD_LOG, maxLines=1000, escapeHtml=false}''',
//                         to: recipients,
//                         recipientProviders: [[$class: 'CulpritsRecipientProvider']],
//                         attachmentsPattern: 'performance.html',
//                     )
//                 } else {
//                     echo "${mark}"
//                     if (currentBuild.currentResult != 'SUCCESS') {
//                         emailext (
//                             subject: "[JENKINS] Build ${currentBuild.currentResult}: Job ${env.JOB_NAME} # ${env.BUILD_ID}",
//                             body:  '''${BUILD_LOG, maxLines=1000, escapeHtml=false}''',
//                             to: recipients,
//                             recipientProviders: [[$class: 'CulpritsRecipientProvider']],
//                             attachmentsPattern: 'performance.html',
//                         )
//                     } else {
//                         emailext (
//                             subject: "[JENKINS] Build ${currentBuild.currentResult}: Job ${env.JOB_NAME} # ${env.BUILD_ID}",
//                             body:  '''${BUILD_LOG, maxLines=1000, escapeHtml=false}''',
//                             to: recipients,
//                             recipientProviders: [[$class: 'CulpritsRecipientProvider']],
//                             attachmentsPattern: 'performance.html',
//                         )
//                     }
//                 }
//             }
//         }
//     }
// }