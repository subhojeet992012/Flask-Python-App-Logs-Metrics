Flask Python App with Logs & Docker Deployment

This project is a Flask-based web application that logs requests to a file and exposes metrics for monitoring. The application is containerized using Docker, and logs are stored on the host machine using a bind mount.

📌 Features

✅ Flask Web Server - Serves HTTP requests on port 5000✅ Logging - Stores logs in a persistent directory (logs/app.log)✅ Dockerized Application - Runs inside a lightweight python:3.12-alpine container✅ Host-Container Log Binding - Logs persist even after the container stops✅ Prometheus Metrics (Optional) - Can expose metrics for monitoring

📂 Project Structure

Flask-Python-App-Logs-Metrics/
│── static/             # Static files (HTML, CSS, JS)
│── logs/               # Log directory (mounted to host)
│── venv/               # Virtual environment (local use)
│── app.py              # Flask application
│── requirements.txt    # Python dependencies
│── Dockerfile          # Docker container setup
│── README.md           # Project documentation

🚀 Setup & Running the Application

1️⃣ Clone the Repository

git clone https://github.com/your-repo/Flask-Python-App-Logs-Metrics.git
cd Flask-Python-App-Logs-Metrics

2️⃣ Install Dependencies (For Local Use)

python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
pip install -r requirements.txt

3️⃣ Run Flask App Locally

python3 app.py

📌 Access the application: http://127.0.0.1:5000/

📌 Check logs: cat logs/app.log

🛠 Running with Docker

1️⃣ Build Docker Image

docker build -t flask-app .

2️⃣ Run the Container with Log Persistence

docker run -d -p 5000:5000 -v $(pwd)/logs:/flask-app/logs --name flask-app flask-app

📌 Now logs are stored in logs/ on the host machine.

3️⃣ Verify Logs Are Stored on Host

ls -l logs/
tail -f logs/app.log

4️⃣ Stop & Remove Container

docker stop flask-app
docker rm flask-app

📌 Docker Compose Setup (Optional)

For easy multi-container management, use Docker Compose.

1️⃣ Create docker-compose.yml:

version: "3.8"

services:
  flask-app:
    image: flask-app
    container_name: flask-app
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./logs:/flask-app/logs  # Persist logs on the host

2️⃣ Run the app using Compose:

docker-compose up -d

📌 Environment Variables (Optional)

You can configure the app using environment variables:

FLASK_ENV=production
FLASK_DEBUG=0

📌 Next Steps

🔹 Add Prometheus metrics for monitoring🔹 Integrate Logstash & Elasticsearch for log aggregation🔹 Deploy on Kubernetes (K8s)

📌 Need help setting up logging with Fluent Bit or ELK Stack? Let me know! 🚀
