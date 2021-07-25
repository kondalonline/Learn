pipeline {
    agent any
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
        }
        stage('test') {
            steps{
                echo 'running tests..'
            }
        }
        stage('deploy') {
            steps{
                echo 'deploying app..'
            }
        }
    }
}
