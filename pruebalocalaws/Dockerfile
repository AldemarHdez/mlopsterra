# Use an official Python runtime as a parent image
FROM public.ecr.aws/lambda/python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt -t .

# Copy the rest of the application code into the container
COPY scripts/app.py /app/
COPY scripts/train.py /app/
COPY scripts/evaluate.py /app/
COPY data /app/data

# Command to run the FastAPI app using the AWS Lambda runtime
CMD ["app.handler"]

