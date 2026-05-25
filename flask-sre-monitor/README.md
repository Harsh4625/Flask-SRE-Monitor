# Flask SRE Monitor

A containerized system monitoring web service built with **Flask**, **Docker**, **Nginx**, and **Gunicorn** — deployed on a Linux environment.

Demonstrates core SRE/DevOps concepts: containerization, reverse proxying, health checks, and infrastructure-as-code.

---

## Architecture

```
Client (Browser / curl)
        │
        ▼
  ┌───────────┐
  │   Nginx   │  ← Reverse proxy (port 80)
  │  :80      │     Rate limiting, request forwarding
  └─────┬─────┘
        │ proxy_pass
        ▼
  ┌───────────┐
  │   Flask   │  ← App server via Gunicorn (port 5000, internal)
  │  :5000    │     /health  /status  /metrics
  └───────────┘

Both containers on shared Docker bridge network.
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| App framework | Flask 3.x |
| WSGI server | Gunicorn |
| Reverse proxy | Nginx (Alpine) |
| Containerization | Docker + Docker Compose |
| OS | Linux (Ubuntu / any) |
| Version control | Git + GitHub |

---

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | Service info |
| `GET /health` | Liveness probe — is app alive? |
| `GET /status` | Readiness probe — uptime, host, env |
| `GET /metrics` | CPU %, RAM usage, Disk usage |
| `GET /nginx-health` | Nginx-level health check (bypasses Flask) |

---

## Running Locally

### Prerequisites
- Docker
- Docker Compose

### Steps

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/flask-sre-monitor.git
cd flask-sre-monitor

# 2. Build and start all containers
docker-compose up --build

# 3. Test endpoints
curl http://localhost/health
curl http://localhost/status
curl http://localhost/metrics
```

### Stop containers
```bash
docker-compose down
```

---

## Useful Docker Commands

```bash
# View running containers
docker ps

# View logs (Flask app)
docker logs flask_app

# View logs (Nginx)
docker logs nginx_proxy

# Exec into Flask container (Linux CLI practice)
docker exec -it flask_app bash

# Rebuild after code change
docker-compose up --build --force-recreate
```

---

## Key Concepts Demonstrated

- **Containerization** — App runs identically on any Linux machine via Docker
- **Reverse Proxy** — Nginx forwards traffic to Flask; hides internal port
- **Health Checks** — Docker restarts container if `/health` fails
- **Service Dependency** — Nginx waits for Flask to be healthy before starting
- **Rate Limiting** — Nginx limits 10 req/sec per IP (basic DDoS protection)
- **Gunicorn** — Production-grade WSGI server (not Flask dev server)
- **Docker Networking** — Containers communicate via internal bridge network

---

## Project Structure

```
flask-sre-monitor/
├── app/
│   ├── app.py              # Flask application
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # Container build instructions
├── nginx/
│   └── nginx.conf          # Reverse proxy configuration
├── docker-compose.yml      # Multi-container orchestration
├── .gitignore
└── README.md
```

---

## What I Learned

- Writing Dockerfiles and building images
- Configuring Nginx as a reverse proxy
- Using docker-compose for multi-service deployment
- Linux-based deployment and container management via CLI
- Health check patterns used in real SRE environments
