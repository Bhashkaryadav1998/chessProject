pipeline {
environment{
imageName=0
}
  agent any
  stages
    {
    stage('Test'){
    steps{
    sh """
          PATH=/home/bhashkar/anaconda3/condabin/conda
          conda activate
          python test.py
       """
    }
    }
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
    stage("Rundeck Deploy"){
     steps{
     script {
               step([
                 $class: "RundeckNotifier",
                 includeRundeckLogs: true,
                 rundeckInstance: "Rundeck Server",
                 jobId: "b749e5e7-361b-4d1e-bb67-6d1a3e1a0068",
                 shouldWaitForRundeckJob: true,
                 shouldFailTheBuild: true,
                 tailLog: true
               ])
             }
     }
     }
  }
}