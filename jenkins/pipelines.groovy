pipeline {
  agent any  
  environment {
    //put your environment variables
    doError = '0'
    // DOCKER_REPO = ""
    // CHART_DIR = ""
    // HELM_RELEASE_NAME = ""
  }   
  stages {
    stage ('Build and Test') {
      steps {
        bat '''
        if exist superapp rmdir superapp /q /s
        git clone git@github.com:hmanzer/superapp.git
        cd superapp\\customers_api
        docker build -t %DOCKER_REPO%:%BUILD_NUMBER% .
        echo 'Starting test cases'
        '''    
      }
    }  
    stage ('Artifact') {
      steps {
        bat '''
        gcloud auth configure-docker
        docker push %DOCKER_REPO%:%BUILD_NUMBER%
        '''
        }
    }   
    stage ('Deploy') {
      steps {
        bat '''
        kubectl config set-context --current --namespace=%ENV%
        helm upgrade --install %HELM_RELEASE_NAME% %CHART_DIR%\\%HELM_RELEASE_NAME%  --set image.repository=%DOCKER_REPO% --set image.tag=%BUILD_NUMBER%  --set environment=-%ENV% -f %CHART_DIR%/%HELM_RELEASE_NAME%/values.yaml --namespace %ENV%
        '''
      }
    }
    stage('Cleanup') {
      steps{
        bat "docker rmi %DOCKER_REPO%:%BUILD_NUMBER%"
      }
  }
  stage('Error') {
    // when doError is equal to 1, return an error
    when {
        expression { doError == '1' }
    }
    steps {
        echo "Failure :("
        error "Test failed on purpose, doError == str(1)"
    }
}
  stage('Success') {
    // when doError is equal to 0, just print a simple message
    when {
        expression { doError == '0' }
    }
    steps {
        echo "Success :)"
    }
}
  }
    // Post-build actions
}