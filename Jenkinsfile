pipeline {
    agent {
        docker {
            image 'python:3.7-alpine'
        }
    }
    stages {
        stage('Code linting') {
            steps {
                sh 'pip install -r requirements.txt'
                echo 'Code is being linting now'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build') {
         steps {
            sh(script: """
               docker build -t calender_app .
            """)
         }
      }

        stage('Push')  {
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