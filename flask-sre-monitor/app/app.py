from flask import Flask, jsonify, render_template
import psutil
import platform
import datetime
import os

app = Flask(__name__)

START_TIME = datetime.datetime.utcnow()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    """Basic liveness probe — is the app alive?"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    }), 200

@app.route("/status")
def status():
    """Readiness probe — is the app ready to serve traffic?"""
    uptime_seconds = (datetime.datetime.utcnow() - START_TIME).total_seconds()
    return jsonify({
        "status": "ok",
        "uptime_seconds": round(uptime_seconds, 2),
        "host": platform.node(),
        "python_version": platform.python_version(),
        "environment": os.getenv("APP_ENV", "development")
    }), 200

@app.route("/metrics")
def metrics():
    """System resource metrics — CPU, RAM, Disk."""
    return jsonify({
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": {
            "total_mb": round(psutil.virtual_memory().total / 1024 / 1024, 2),
            "used_mb": round(psutil.virtual_memory().used / 1024 / 1024, 2),
            "percent": psutil.virtual_memory().percent
        },
        "disk": {
            "total_gb": round(psutil.disk_usage("/").total / 1024 / 1024 / 1024, 2),
            "used_gb": round(psutil.disk_usage("/").used / 1024 / 1024 / 1024, 2),
            "percent": psutil.disk_usage("/").percent
        },
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
