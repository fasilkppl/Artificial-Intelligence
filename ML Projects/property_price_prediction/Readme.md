# Docker and EC2 Setup 

# 1. Install Docker Desktop
# Download from: https://www.docker.com/products/docker-desktop

# 2. Verify installation
docker --version
docker-compose --version
Setup Steps
Step 1: Add your ML model files


# Place these files in backend/artifacts/
backend/
  └── artifacts/
      ├── columns.json          # Your feature columns
      └── home_prices_model.pickle  # Your trained model
Step 2: Build and run


# From project root directory
docker-compose up --build
Step 3: Access the app

Open browser → http://localhost
Part 2: Deploy to Amazon EC2
Step 1: Create EC2 Instance
Login to AWS Console → EC2 → Launch Instance
Name: bangalore-predictor
AMI: Amazon Linux 2023
Instance type: t2.small (or t2.micro for free tier)
Key pair: Create new → Download .pem file
Security Group: Allow ports 22, 80, 443
Click Launch Instance
Step 2: Connect to EC2

# Make key readable
chmod 400 your-key.pem

# SSH into instance
ssh -i your-key.pem ec2-user@<your-ec2-public-ip>
Step 3: Install Docker on EC2

sudo yum update -y
sudo yum install -y docker git
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Re-login to apply group changes
exit
ssh -i your-key.pem ec2-user@<your-ec2-public-ip>
Step 4: Upload Project to EC2

# From your LOCAL machine
scp -i your-key.pem -r ./* ec2-user@<your-ec2-public-ip>:~/app/
Step 5: Deploy

# On EC2
cd ~/app
docker-compose up -d --build
Step 6: Access Your App
http://<your-ec2-public-ip>