## Prerequisites

1. `Docker` installed on your system.

2. `Docker Compose` installed on your system.

3. A terminal or command prompt for running commands.

## Installation and Setup
1. Clone the Project Repository

Clone the project repository to your local machine using the 

Following command:


```bash
git clone <repository_url>
```
Replace <repository_url> with the actual URL of the project repository.

2. Build Docker Images

Navigate to the project directory and build the Docker images using Docker Compose:


```bash
docker-compose -f docker-compose.local.yml build
```

3. Run Docker Containers

Start the Docker containers to run the application services:

```bash
docker-compose -f docker-compose.local.yml up
```
This command will start all the services defined in the docker-compose.local.yml file.

4. Create a Superuser

Open another terminal and create a Django superuser to access the admin panel:

```bash
docker-compose -f docker-compose.local.yml exec django python manage.py createsuperuser
```

Follow the prompts to set up the superuser account.
5. Access the Application

Open your web browser and navigate to http://localhost:8000/ to access the application.
Using the Application
Accessing the Django Admin Panel

Go to http://localhost:8000/admin/ in your web browser.

Log in using the superuser credentials you created.

Navigate to the Products section.

Click on the Upload CSV button to upload your product data.