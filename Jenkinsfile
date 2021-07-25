pipeline {
    agent any
<<<<<<< HEAD
    tools {
        terraform 'terraform'
    }
    stages {
        stage ('git checkout'){
            git changelog: false, credentialsId: '4e103e68-1057-4f9a-af49-04400d98fc71', poll: false, url: 'https://github.com/kondalonline/Learn'
=======
    stages {
        stage('build') {
            steps {
                echo 'building ..'
                sh 'echo "this is step 2" '
                sh ''' 
                    echo " step 3"
                    pwd
                    hostname
                    uname -a
                    ls -ltr
                    echo " build completed "
                '''
            }
>>>>>>> c849e0711957395e1d78d334117c5a95fa3900aa
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
