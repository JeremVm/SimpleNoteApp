FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory 
COPY . /app

# Install necessary packages
RUN pip install --upgrade pip \
    && pip install opentelemetry-distro opentelemetry-exporter-otlp \
    && pip install Flask 

# Automatically instrument the Flask app
RUN opentelemetry-bootstrap -a install

# Expose the port that Flask runs on
EXPOSE 5000

# Run the Flask app using OpenTelemetry's auto-instrumentation
CMD ["opentelemetry-instrument", "flask", "run", "--host=0.0.0.0"]

