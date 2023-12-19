# Use an official Python runtime as a parent image
FROM python:3.11-slim

RUN apt-get update && apt-get -y install cron

# Set the working directory to /app
WORKDIR /app

# Copy all files from the current directory into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Add cronjob file in the cron directory
COPY cronjob /etc/cron.d/hello-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/hello-cron

# Apply cron job
RUN crontab /etc/cron.d/hello-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD ["cron", "-f"]