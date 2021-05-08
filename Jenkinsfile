pipeline {
environment{
imageName=0
}
  agent any
  stages
    {
    stage('Docker build to Image'){
    steps{
    script{
    imageName=docker.build "bhashkaryadav1998/chess_project:latest"
    }
    }
    }
    stage('Push Docker Image'){
        steps{
        script{
        docker.withRegistry('','docker-jenkins'){
        imageName.push()
        }
        }
        }
        }

  }
}