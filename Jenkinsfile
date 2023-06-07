pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('Task2') {
      steps {
        bat 'python Task2.py'
        bat 'result.txt'
      }
    }
  }
}
