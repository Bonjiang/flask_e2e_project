### About my webservice 

My web service is a healthcare oriented service that displays data with tables of general patient information and their medical records information. This is a great starter tool for medical offices and it can be further developed to host more information and data. Currently, I leveraged Faker to generate fake random data to fill the tables, but this can altered to store real information. I find this web service to be important because it leverages many technologies to provide a great and easy experience:

-Github (Version Control)
-Frontend framework: Tailwind
-Backend framework: Flask
-Database via GCP: MYSQL with SQLAlchemy (ORM), simplifying database interactions (in the docs folder is a screenshot of the EER Diagram)
-Authorization: Google OAuth, allowing users to login using their Google credentials 
-Logging: Python's built-in logging module
-Containerization: Docker, to ensure appliaton runs consistenly in various environments
-This product is deployed to the cloud via GCP
-This product uses environment variables 
-This product uses Github for version control

### To run my web service

#### Run locally without Docker

1) Obtain the relevant database connection information and details to then update the environment variables in your own ".env" file, I have provided a template of the needed information in my file.
2) Set up a MySQL database and connect using the appropriate information
3) Install all the required Python packages. This can be found in my "requirements.txt" file
4) Look through my files and folders and incorporate any relevant information. Feel free to modify the endpoints/pages/data, ect.
5) From here, run the Flask application with the "python app.py" command
6) This service can be accessed at the "http://localhost:8080" (I have used the 8080 port, but feel free to modify)

#### Run Locally with Docker

1) To build the Docker image based on my Docker file, run the "docker build -t bonnie ." command, which builds the image and specifying and tagging the image to be named "bonnie". Note: Add the period at the end of the command because it represents the context of the build and tells Docker to use the current directory.
2) Then, run the command "docker run -d -p 8005:8080 bonnie" to run in detached mode/background and map the port 8005 on the host to port 8080 on the container. Feel free to use another port.
3) This should then generate a link to view the application.

#### Deploy to the Cloud

1) Choose a cloud provider. (GCP, Azure-I went with GCP)
2) Set up the infrastructure and provide any relevant information. This would include setting up a MYSQL Instance, creating a database, OAuth credentials for authorization, ect.) Do this on the cloud platform you had chosen.
3) Update the .env file with your information and Dockerfile if that is needed. (This is to accomadate to your configurations that at specfic to your cloud)
4) Build the Docker image locally
5) Push it to a container that is compatible with your cloud provider.
6) Then, just deploy this application on the cloud service. Make sure all the .env information and configuration settings are all appropriate.
7) Finally, this service can be accessed through the link/url of the cloud provider.



Please note: I ran into an error when running the python app.py command (attached picture in docs folder) and it would say my base.html template was not found, when I had this file under my templates. When I stopeed the service to try again, it gave me the same error repeatedly. I also made sure my app.py was under the same directory.







