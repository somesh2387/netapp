#!groovy
pipeline {
  agent none
  stages {
    stage('Test') {
      agent any
      steps {
        sh 'pytest test.py'
      }
    }
    stage('Docker Build') {
      agent any
      steps {
        sh 'docker build -t somesh7292/netapp:$BUILD_NUMBER .'
      }
    }
    stage('Docker Push') {
      agent any
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerhubPassword', usernameVariable: 'dockerhubUser')]) {
          sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
          sh 'docker push somesh7292/netapp:$BUILD_NUMBER'
        }
      }
    }
  }
}
