pipeline {
    agent none
    stages {
        stage('build') {
            steps {
                echo 'building ..'
                step {
                     echo 'step 1'
                }
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
