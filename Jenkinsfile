pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'building ..'
                step {
                    echo "inside step 1"
                
                }
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
