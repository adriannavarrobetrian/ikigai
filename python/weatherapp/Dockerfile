FROM python:3.11

WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app files to the working directory
COPY . .

# Expose the necessary port
EXPOSE 8000

# Set the startup command to run the Flask app
CMD ["python", "server.py"]