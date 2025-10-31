pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: '1', usernameVariable: 'USER', passwordVariable: 'PASS')]){
                    bat '''
                        echo %PASS% | docker login -u %USER% --password-stdin
                        docker build -t %USER%/auto_data:latest .
                    '''
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: '1', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    bat '''
                        echo %PASS% | docker login -u %USER% --password-stdin
                        docker push %USER%/auto_data:latest
                    ''' 
                }
            }
        }
        stage('Deploy') {
            steps {
                bat '''
                    docker-compose up -d
                ''' 
            }
        }
    }
}
