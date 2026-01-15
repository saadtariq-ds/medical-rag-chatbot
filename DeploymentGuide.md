# Medical RAG Chatbot Deployment Guide

## 🐳 Step 1: Build Docker Image, Scan with Trivy, and Push to AWS ECR
### 1. Install Trivy in Jenkins Container
```bash
docker exec -u root -it jenkins-dind bash
apt install -y
curl -LO https://github.com/aquasecurity/trivy/releases/download/v0.62.1/trivy_0.62.1_Linux-64bit.deb
dpkg -i trivy_0.62.1_Linux-64bit.deb
trivy --version
exit
```
Then restart the container
```bash
docker restart jenkins-dind
```

### 2. Install AWS Plugins in Jenkins
- Go to Jenkins Dashboard → Manage Jenkins → Plugins
- Install:
  - AWS SDK
  - AWS Credentials
Restart the container:
```bash
docker restart jenkins-dind
```

### 3. Create IAM User in AWS
- Go to AWS Console → IAM → Users → Add User
- Assign programmatic access
- Attach policy: AmazonEC2ContainerRegistryFullAccess
- After creation, generate Access Key + Secret

### 4. Add AWS Credentials to Jenkins
- Go to Jenkins Dashboard → Manage Jenkins → Credentials
- Click on (Global) → Add Credentials
- Select AWS Credentials
- Add:
  - Access Key ID
  - Secret Access Key
- Give an ID (e.g., `aws-ecr-creds`) and Save

### 5. Install AWS CLI Inside Jenkins Container
```bash
docker exec -u root -it jenkins-dind bash
apt update
apt install -y unzip curl
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
./aws/install
aws --version
exit
```

### 6. Create an ECR Repository
- Go to AWS Console → ECR → Create Repository
- Note the repository URI

### 7. Add Build, Scan, and Push Stage in Jenkinsfile ( Already done if cloned )


### 8. Fix Docker Daemon Issues (If Any)
If you encounter Docker socket permission issues, fix with:
```bash
docker exec -u root -it jenkins-dind bash
chown root:docker /var/run/docker.sock
chmod 660 /var/run/docker.sock
getent group docker
# If group 'docker' exists, skip next line
usermod -aG docker jenkins
exit
```
Restart the container:
```bash
docker restart jenkins-dind
```
Then open Jenkins Dashboard again to continue.

---

## 🚀 Step 2:  Deployment to AWS App Runner

### ✅ Prerequisites
- Jenkinsfile Deployment Stage ( Already done if cloned )

### 🔐 IAM User Permissions
- Go to AWS Console → IAM → Select your Jenkins user
- Attach the policy: `AWSAppRunnerFullAccess`

### 🌐 Setup AWS App Runner (Manual Step)
1. Go to AWS Console → App Runner
2. Click Create service
3. Choose:
  - Source: Container registry (ECR)
  - Select your image from ECR
4. Configure runtime, CPU/memory, and environment variables
5. Set auto-deploy from ECR if desired
6. Deploy the service

### 🧪 Run Jenkins Pipeline
- Go to Jenkins Dashboard → Select your pipeline job
- Click Build Now

### If all stages succeed (Checkout → Build → Trivy Scan → Push to ECR → Deploy to App Runner):
- 🎉 CI/CD Deployment to AWS App Runner is complete!
- ✅ Your app is now live and running on AWS 🚀