#!groovy
pipeline {
  agent none
  def app
  stages {
    stage('Docker Build') {
      agent any
      steps {
          app = docker.build("somesh7292/netapp")
          app.push("latest")          
      }
    }
  }
}
