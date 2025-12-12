#!/bin/bash

# Bangalore Home Price Predictor - EC2 Deployment Script
# Run this script on your EC2 instance

set -e

echo "🏠 Deploying Bangalore Home Price Predictor..."

# Update system
echo "📦 Updating system packages..."
sudo yum update -y || sudo apt-get update -y

# Install Docker if not present
if ! command -v docker &> /dev/null; then
    echo "🐳 Installing Docker..."
    sudo yum install -y docker || sudo apt-get install -y docker.io
    sudo systemctl start docker
    sudo systemctl enable docker
    sudo usermod -aG docker $USER
fi

# Install Docker Compose if not present
if ! command -v docker-compose &> /dev/null; then
    echo "🐳 Installing Docker Compose..."
    sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
fi

# Build and run containers
echo "🔨 Building containers..."
docker-compose build --no-cache

echo "🚀 Starting services..."
docker-compose up -d

echo "✅ Deployment complete!"
echo "🌐 Access the application at http://$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4)"

# Show running containers
docker-compose ps
