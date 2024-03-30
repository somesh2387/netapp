#!groovy
pipeline {
  agent none
  stages {
    stage('Test') {
      agent any
      steps {
        withPythonEnv('python3') {
          sh 'pip3 install -r requirements.txt'
          sh 'pytest test.py'
        }
      }
    }
    stage('checkout') {
      agent any
      steps {
        git branch: 'main',
        credentialsId: 'somesh7292',
        url: 'https://github.com/somesh7292/netapp-k8s.git'
        sh "ls -lat"
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
    stage('Manifest push') {
      agent any
      steps {
        git branch: 'main',
        credentialsId: 'somesh7292',
        url: 'https://github.com/somesh7292/netapp-k8s.git'
        sh "yq -i '.spec.template.spec.containers[0].image='docker.io/somesh7292/netapp:$BUILD_NUMBER'' k8s/deployment.yaml"
        sh "git add ."
        sh "git commit -m 'Deploying image tag $BUILD_NUMBER'"
        sh "git push"
      }
    }
  }
}
