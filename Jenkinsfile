pipeline {
    agent {
        docker {
            image 'python:3-slim'
        }
    }
    stages {

        stage('Code linting') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pylint calendars/'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest tests'
            }
        }

        stage('Build') {
         steps {
            sh 'docker build -t calender_app . '
         }
      }

      stage('Push') {
         steps {
            dir("$WORKSPACE") {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub') {
                      def image = docker.build('seifeleslam/calender_app:latest')
                      image.push()
                  }
                }
            }
         }
      }


    }
}