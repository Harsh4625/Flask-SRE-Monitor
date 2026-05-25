# --- Stage 1: Base image ---
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy only requirements first (layer caching — faster rebuilds)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of app code
COPY . .

# Expose Flask port
EXPOSE 5000

# Set environment variable
ENV APP_ENV=production

# Run with Gunicorn (production WSGI server, not Flask dev server)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
