# Bangalore Home Price Predictor - Deployment Guide

## Project Structure

```
├── backend/
│   ├── artifacts/           # ML model files (you need to add these)
│   │   ├── columns.json
│   │   └── home_prices_model.pickle
│   ├── server.py
│   ├── util.py
│   ├── requirements.txt
│   └── Dockerfile
├── nginx/
│   └── nginx.conf
├── src/                     # React frontend
├── docker-compose.yml
├── Dockerfile.frontend
├── deploy.sh
└── DEPLOYMENT.md
```

## Prerequisites

1. **ML Model Files**: Place your trained model files in `backend/artifacts/`:
   - `columns.json` - Feature columns
   - `home_prices_model.pickle` - Trained scikit-learn model

2. **AWS Account** with EC2 access

## Local Development

```bash
# Start backend only
cd backend
pip install -r requirements.txt
python server.py

# Start frontend (in another terminal)
npm run dev
```

## EC2 Deployment Steps

### 1. Launch EC2 Instance

- **AMI**: Amazon Linux 2023 or Ubuntu 22.04
- **Instance Type**: t2.micro (free tier) or t2.small
- **Security Group**: Open ports 22 (SSH), 80 (HTTP), 443 (HTTPS)

### 2. Connect to EC2

```bash
ssh -i your-key.pem ec2-user@your-ec2-ip
```

### 3. Clone/Upload Project

```bash
# Option 1: Git clone
git clone <your-repo-url>
cd bangalore-price-predictor

# Option 2: SCP upload
scp -i your-key.pem -r ./project ec2-user@your-ec2-ip:~/
```

### 4. Add Model Artifacts

Upload your ML model files:
```bash
scp -i your-key.pem backend/artifacts/* ec2-user@your-ec2-ip:~/project/backend/artifacts/
```

### 5. Deploy

```bash
chmod +x deploy.sh
./deploy.sh
```

## Manual Docker Commands

```bash
# Build containers
docker-compose build

# Start in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild and restart
docker-compose up -d --build
```

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                    EC2 Instance                      │
│  ┌───────────────────────────────────────────────┐  │
│  │              Docker Compose                    │  │
│  │  ┌─────────────────┐    ┌─────────────────┐  │  │
│  │  │    Frontend     │    │    Backend      │  │  │
│  │  │    (Nginx)      │───▶│    (Flask +     │  │  │
│  │  │   Port 80       │    │    Gunicorn)    │  │  │
│  │  │                 │    │   Port 5000     │  │  │
│  │  │  - Static files │    │                 │  │  │
│  │  │  - /api proxy   │    │  - ML Model     │  │  │
│  │  └─────────────────┘    └─────────────────┘  │  │
│  └───────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/get_location_names` | GET | Get all available locations |
| `/api/predict_home_price` | POST | Predict price (form data: total_sqft, bhk, bath, location) |
| `/api/health` | GET | Health check |

## Troubleshooting

### Check container status
```bash
docker-compose ps
```

### View logs
```bash
docker-compose logs frontend
docker-compose logs backend
```

### Restart services
```bash
docker-compose restart
```

### Check if model files exist
```bash
ls -la backend/artifacts/
```

## Environment Variables (Optional)

Create `.env` file for custom configuration:
```env
FLASK_ENV=production
WORKERS=4
```
