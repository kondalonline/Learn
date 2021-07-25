pipeline {
    agent any
    tools {
        terraform 'terraform'
    }
    stages {
        stage ('git checkout'){
            steps {
                git credentialsId: '974adeae-bb15-45f2-900a-da1f0d34d03c', url: 'https://github.com/kondalonline/Learn'
            }
        }
        stage('terraform init') {
            steps {
                sh 'terraform init'
            }
        }
        stage('terraform apply') {
            steps{
                sh 'terraform apply'
            }
        }

    }
}
