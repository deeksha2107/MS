# Use lightweight Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /ai_study_planner

# Copy package and files
COPY . .

ENV PYTHONPATH=/ai_study_planner

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the study planner
CMD ["python", "main.py"]
