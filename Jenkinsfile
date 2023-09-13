pipeline{
    agent any
    stages {
    
        stage('Setup Python Virtual ENV for dependencies'){
       
      steps  {
            sh '''
            chmod +x ./jenkins/envsetup.sh
            ./jenkins/envsetup.sh
            '''}
        }
        stage('Setup Gunicorn Setup'){
            steps {
                sh '''
                chmod +x ./jenkins/gunicorn.sh
                ./jenkins/gunicorn.sh
                '''
            }
        }
        stage('setup NGINX'){
            steps {
                sh '''
                chmod +x ./jenkins/nginx.sh
                ./jenkins/nginx.sh
                '''
            }
        }
    }
}