    # Use a slim Python base image
    FROM python:3.9-slim-buster

    # Set the working directory inside the container
    WORKDIR /app

    # Copy the requirements file and install dependencies
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy the entire application code
    COPY . .

    # Expose the port your Flask app listens on
    EXPOSE 5000

    # Command to run the Flask application
    CMD ["python", "app.py"]