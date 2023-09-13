pipeline{
    agent any
    stages {
    
        stage('Setup Python Virtual ENV for dependencies'){
       
      steps  {
            sh '''
            chmod +x envsetup.sh
            ./jenkins/envsetup.sh
            '''}
        }
        // stage('Setup Gunicorn Setup'){
        //     steps {
        //         sh '''
        //         chmod +x gunicorn.sh
        //         ./jenkins/gunicorn.sh
        //         '''
        //     }
        // }
        // stage('setup NGINX'){
        //     steps {
        //         sh '''
        //         chmod +x nginx.sh
        //         ./jenkins/nginx.sh
        //         '''
        //     }
        // }
    }
}