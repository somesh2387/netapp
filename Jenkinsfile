#!groovy
pipeline {
  agent none
  stages {
    stage('Docker Build') {
      agent any
      steps {
        sh 'docker build -t somesh7292/netapp:latest .'
      }
    }
    stage('Docker Push') {
      agent any
      steps {
        withCredentials([usernamePassword(credentialsId: '9394fcb5-14dc-4963-8848-06563c1c7bec', passwordVariable: '9394fcb5-14dc-4963-8848-06563c1c7becPassword', usernameVariable: '9394fcb5-14dc-4963-8848-06563c1c7becUser')]) {
          sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
          sh 'docker push somesh7292/netapp:latest'
        }
      }
    }
  }
}
