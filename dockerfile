# pulling the 3.10-alpine image from Docker hub, provides the foundational software stack for the app
FROM python:3.10-alpine
# setting the working directory where following commands will be executed
WORKDIR /app
# copies contents of the current directory
COPY . /app
# installs the python dependencies listed in the file, in this case- "flask"
RUN pip install -r requirements.txt
# lets Docker know what port(s) the container is expected to use
EXPOSE 8080
# default command to run when the container starts so we don't have to manually run the command
CMD ["python", "app.py"]

# Docker build command: docker build -t bonnie . 
# Docker run command: docker run -d -p 8005:8080 bonnie