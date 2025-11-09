CodeCollab Platform
A collaborative coding platform built with Django, featuring problem sharing, solution submission, and community interaction.

Features
User authentication and profiles
Create and browse coding problems
Submit and view solutions
Upvote functionality for problems and solutions
Comment system
Progress tracking
Admin dashboard for content moderation
Responsive design with Tailwind CSS
Interactive components with Alpine.js
Tech Stack
Backend: Django
API: Django REST Framework
Database: SQLite (development), PostgreSQL (production)
Frontend: HTML5, Tailwind CSS, Alpine.js
Authentication: Django's built-in authentication
Prerequisites
Python 3.8 or higher
pip (Python package installer)

Installation
Clone - git@github.com:CodeOfCreation/CodeCollab.git

or create the project structure

Create a virtual environment (recommended):
python -m venv venv

Activate the virtual environment:
On Windows
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

Install required packages
pip install django djangorestframework pillow

Database Setup
Run database migrations
python manage.py makemigrations
python manage.py migrate

Create a superuser account (optional but recommended):
python manage.py createsuperuser

Collect static files:
python manage.py collectstatic

Running the Application
Start the development server
python manage.py runserver

Access the application:
Main site: http://127.0.0.1:8000/
Admin panel: http://127.0.0.1:8000/admin/

Project Structure:

codecollab_project/
├── manage.py
├── codecollab_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── core/
│           ├── base.html
│           ├── index.html
│           └── dashboard.html
├── users/
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   └── templates/
│       └── users/
│           ├── login.html
│           ├── signup.html
│           └── profile.html
├── problems/
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   └── templates/
│       └── problems/
│           ├── problems.html
│           ├── problem_detail.html
│           └── create_problem.html
├── api/
│   ├── __init__.py
│   ├── apps.py
│   ├── serializers.py
│   ├── viewsets.py
│   ├── urls.py
│   └── admin.py
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── alpine.js
└── templates/
    └── registration/
        └── logged_out.html

Usage
Sign Up/Login: Create an account or log in to access features
Create Problems: Share coding challenges with the community
Browse Problems: Explore problems by difficulty, language, or tags
Submit Solutions: Share your solutions to problems
Upvote/Comment: Engage with the community by upvoting and commenting
Track Progress: View your activity and achievements on your profile
Admin Features
Manage users and their profiles
Moderate problems, solutions, and comments
View platform analytics
Manage tags and categories
Database Management
View Database Content
Option 1 - SQLite Browser:

Download DB Browser for SQLite
Open db.sqlite3 file from your project directory
Option 2 - Django Shell:
python manage.py shell

from users.models import CustomUser
from problems.models import Problem, Solution, Comment, Upvote

# View data
print(f"Users: {CustomUser.objects.count()}")
print(f"Problems: {Problem.objects.count()}")
print(f"Solutions: {Solution.objects.count()}")

Troubleshooting
Make sure the virtual environment is activated
Ensure all required packages are installed
Check that database migrations were applied successfully
Verify that static files were collected
Security Notes
For production use, change the SECRET_KEY in settings.py
Set DEBUG = False in settings.py for production
Configure proper allowed hosts in settings.py

License
This project is open source and available under the MAHADEV SHETE & NIKHIL ASHTURE License.