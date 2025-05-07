# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Create a non-root user and group
RUN groupadd -r appgroup && useradd --no-log-init -r -g appgroup appuser

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY --chown=appuser:appgroup requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container at /app
COPY --chown=appuser:appgroup ./src ./src

# Make port 5002 available
EXPOSE 5002

# Switch to non-root user
USER appuser

# Run the Uvicorn server
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "5002"]