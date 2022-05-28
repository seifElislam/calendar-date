pipeline {
    agent {
        docker {
            label 'docker'
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


    }
}