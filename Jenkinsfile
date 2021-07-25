pipeline {
    agent any
    tools {
        terraform 'terraform'
    }
    stages {
        stage ('git checkout'){
            git changelog: false, credentialsId: '4e103e68-1057-4f9a-af49-04400d98fc71', poll: false, url: 'https://github.com/kondalonline/Learn'
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
