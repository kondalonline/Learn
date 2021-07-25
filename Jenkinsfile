pipeline {
    agent none
    stages {
        stage('build') {
            steps {
                echo 'building ..'
                sh 'echo "this is step 2" '
                sh ''' 
                    echo " step 3"
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
