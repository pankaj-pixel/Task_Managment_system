# Task Management API

This is a Task Management API built using Django and Django Rest Framework (DRF). It allows users to create tasks, assign tasks to one or more users, and retrieve tasks assigned to a specific user.

## API Handling PDF To handle Request/Response Attached
JoshTalk_TaskManagment_API_Docs.pdf(IN ZIP)

## Requirements

- Python 3.x
- Django 3.x or higher
- Django Rest Framework
- A database SQLite(by Default)

## Installation

1. **Clone the repository**:
 
   git clone https://github.com/pankaj-pixel/Task_Managment_system.git
   cd Task_Managment_system

Step 2: Set up a virtual environment
It's recommended to set up a virtual environment to avoid conflicts with other projects. Run the following command to create and activate a virtual environment:

For Windows:
python -m venv venv
venv\Scripts\activate
Step 3: Install dependencies
Install all required dependencies by running the following command:


pip install -r requirements.txt
Step 4: Apply database migrations
Migrations to set up the database:

python manage.py migrate

Step 5: Create a superuser (optional)
To access the Django admin panel or create new users, create a superuser:

python manage.py createsuperuser
You will be prompted to enter a username, email, and password for the superuser.

Step 6: Run the development server
Start the Django development server by running the following command:

python manage.py runserver
The API will be available at: http://127.0.0.1:8000/.
