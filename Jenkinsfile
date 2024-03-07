pipeline {
     agent {
        label 'wsl'
     }
     tools {
        git  "wsl_git"
        nodejs "wsl_node"
     }
     environment {
         NODE_VERSION = '14.17.5'
         AWS_ACCOUNT_ID="637423238337"
         AWS_DEFAULT_REGION="ap-south-1"
         IMAGE_REPO_NAME="products-container"
         IMAGE_TAG="latest"
         REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
         CLUSTER = "mcart-cluster"
         SERVICE = "mcart-products-service"
    }

 stages {

     stage('Docker Build') {
         steps{
             script {
                sh("eval \$(aws ecr get-login --no-include-email | sed 's|https://||')")
                 dir('products_service') {
                    sh 'pwd'
                    sh "docker build -t ${IMAGE_REPO_NAME} ."
                }
             }
         }
     }

     stage('Docker Push to ECR') {
         steps{
             script {
                 sh "docker tag ${IMAGE_REPO_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}:${IMAGE_TAG}"
                 sh "docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:${IMAGE_TAG}"
                 }
             }
         }
     stage('Deploy to serverless') {
         steps{
             script {
                     dir('order_service_api') {
                        sh 'pwd'
                        sh 'node -v'
                        sh 'serverless plugin install -n serverless-wsgi'
                        sh 'serverless plugin install -n serverless-python-requirements'
                        sh "serverless deploy --force"
                     }
                 }
             }
         }

     stage('Deploy to ECS') {
         steps{
                withAWS(region: AWS_DEFAULT_REGION, credentials: 'MCART_CREDS') {
                    sh "aws ecs update-service --cluster ${CLUSTER} --service ${SERVICE} --force-new-deployment"
                }
             }
         }
     }
}