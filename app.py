from flask import Flask, request
import logging
import os
import time
from prometheus_client import Counter, Gauge, Histogram, Summary, generate_latest, CONTENT_TYPE_LATEST

# Create a Flask app instance
app = Flask(__name__, static_folder="static", static_url_path="/static")

# Ensure logs directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logging
logging.basicConfig(filename="logs/app.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Prometheus Metrics
REQUEST_COUNT = Counter("flask_request_count", "Total number of requests", ["endpoint"])
ACTIVE_REQUESTS = Gauge("flask_active_requests", "Number of active requests")
REQUEST_LATENCY = Histogram("flask_request_latency_seconds", "Latency of requests", ["endpoint"])
REQUEST_SIZE = Summary("flask_request_size_bytes", "Size of HTTP requests", ["endpoint"])

# Middleware for tracking metrics
@app.before_request
def before_request():
    """Tracks active requests and request size"""
    ACTIVE_REQUESTS.inc()
    REQUEST_SIZE.labels(endpoint=request.path).observe(len(request.data))

@app.after_request
def after_request(response):
    """Tracks request count and latency"""
    REQUEST_COUNT.labels(endpoint=request.path).inc()
    ACTIVE_REQUESTS.dec()
    return response

# Route for homepage
@app.route("/")
def hello():
    start_time = time.time()
    response = "Hello, World!"
    REQUEST_LATENCY.labels(endpoint="/").observe(time.time() - start_time)
    app.logger.info("Root endpoint was accessed")
    return response

# Prometheus metrics endpoint
@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

# Run Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

