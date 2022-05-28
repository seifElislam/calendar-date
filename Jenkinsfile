pipeline {
    agent any
    stages {

        stage('Code linting') {
            steps {
                sh 'pip install -r requirements.txt'
                echo 'Code is being linting now'
            }
        }

        stage('Test') {
            steps {
                echo 'pytest'
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