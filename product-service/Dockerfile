FROM python:3.9-slim

# Create a non-root user and group
RUN groupadd -r appgroup && useradd --no-log-init -r -g appgroup appuser

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY --chown=appuser:appgroup requirements.txt .

# Upgrade pip and then install any needed packages specified in requirements.txt
# Increased default timeout for pip
RUN pip install --upgrade pip --timeout 120 && \
    pip install --no-cache-dir -r requirements.txt --timeout 120

# Copy the rest of the application's code into the container at /app
COPY --chown=appuser:appgroup ./src ./src

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Switch to non-root user
USER appuser

# Run the application with Gunicorn
# Changed from "src.main:app" to "src.main:app" with the pythonpath set
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "--pythonpath", "/app", "src.main:app"]