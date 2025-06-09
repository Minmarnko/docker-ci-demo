FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files (including test_pipeline.py)
COPY . .

# Run the pipeline script by default
CMD ["python", "pipeline.py"]
