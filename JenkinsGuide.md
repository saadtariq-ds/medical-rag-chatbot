# Medical RAG Chatbot Jenkins Guide

## ✅ Prerequisites Checklist
1. Docker Desktop is installed and running in the background
2. Code versioning is properly set up using GitHub (repository pushed and updated)
3. Dockerfile is created and configured for the project
4. Dockerfile is also created and configured for Jenkins

## 🚀 Step 1: Jenkins Setup for Deployment
### 1. Create Jenkins Setup Directory and Dockerfile
- Create a folder named `custom_jenkins`
- Inside `custom_jenkins`, create a `Dockerfile` and add the necessary Jenkins + Docker-in-Docker configuration code

### 2. Build Jenkins Docker Image
Open terminal and navigate to the folder:
```bash
cd custom_jenkins
```
Make sure Docker Desktop is running in the background, then build the image:
```bash
docker build -t jenkins-dind .
```

### 3. Run Jenkins Container
```bash
docker run -d ^
  --name jenkins-dind ^
  --privileged ^
  -p 8080:8080 ^
  -p 50000:50000 ^
  -v /var/run/docker.sock:/var/run/docker.sock ^
  -v jenkins_home:/var/jenkins_home ^
  jenkins-dind
```
✅ If successful, you’ll get a long alphanumeric container ID

### 4. Check Jenkins Logs and Get Initial Password
```bash
docker ps
docker logs jenkins-dind
```
If the password isn’t visible, run:
```bash
docker exec jenkins-dind cat /var/jenkins_home/secrets/initialAdminPassword
```

### 5. Access Jenkins Dashboard
Open your browser and go to: http://localhost:8080

### 6. Install Python Inside Jenkins Container
Back in the terminal:
```bash
docker exec -u root -it jenkins-dind bash
apt update -y
apt install -y python3
python3 --version
ln -s /usr/bin/python3 /usr/bin/python
python --version
apt install -y python3-pip
exit
```

### 7. Restart Jenkins Container
```bash
docker restart jenkins-dind
```

### 8. Go to Jenkins Dashboard and Sign In Again

---

## 🔗 Step 2: Jenkins Integration with GitHub

### 1. Generate a GitHub Personal Access Token
- Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
- Click Generate new token (classic)
- Provide:
  - A name (e.g., `Jenkins Integration`)
  - Select scopes:
    - `repo` (for full control of private repositories)
    - `admin:repo_hook` (for webhook integration)
- Generate the token and save it securely (you won’t see it again!).

### 2. Add GitHub Token to Jenkins Credentials
1. Go to Jenkins Dashboard → Manage Jenkins → Credentials → (Global) → Add Credentials
2. Fill in the following:
  - Username: Your GitHub username
  - Password: Paste the GitHub token you just generated
  - ID: `github-token`
  - Description: `GitHub Token for Jenkins`
3. Click Save.

### 3. Create a New Pipeline Job in Jenkins
1. Go back to Jenkins Dashboard
2. Click New Item → Select Pipeline
3. Enter a name (e.g., medical-rag-pipeline)
4. Click OK → Scroll down, configure minimal settings → Click Save
⚠️ You will have to configure pipeline details again in the next step

### 4. Generate Checkout Script from Jenkins UI
1. In the left sidebar of your pipeline project, click Pipeline Syntax
2. From the dropdown, select `checkout: General SCM`
3. Fill in:
  - SCM: Git
  - Repository URL: Your GitHub repo URL
  - Credentials: Select the `github-token` you just created
4. Click Generate Pipeline Script
5. Copy the generated Groovy script (e.g., `checkout([$class: 'GitSCM', ...])`)

### 5. Create a Jenkinsfile in Your Repo
1. Open your project in VS Code
2. Create a file named Jenkinsfile in the root directory

### 6. Push the Jenkinsfile to GitHub
```bash
git add Jenkinsfile
git commit -m "your commit name"
git push origin main
```

### 7. Trigger the Pipeline
1. Go to Jenkins Dashboard → Select your pipeline → Click Build Now

🎉 You’ll see a SUCCESS message if everything works!
✅ Your GitHub repository has been cloned inside Jenkins’ workspace!