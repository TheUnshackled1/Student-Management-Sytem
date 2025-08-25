# LopuesJaena Student Management System
![image](https://github.com/user-attachments/assets/aca09ed4-737c-454d-90b6-f7a352df233c)
![image](https://github.com/user-attachments/assets/624707b6-b6f5-48f5-9749-9838197d79be)
![image](https://github.com/user-attachments/assets/d3de78dd-469b-4d2d-b500-2e060076de1e)
The LopuesJaena Student Management System is a Django-based web application designed to manage student records efficiently. It allows users to create, read, update, and delete student information (CRUD), including details such as student number, name, subject, grade year, and grade.
## Features

* **Add New Students**: Input student details through a user-friendly form.
* **View Students**: Display a list of all registered students.
* **Edit Student Information**: Update existing student records as needed.
* **Delete Students**: Remove student records from the system.
* **Responsive Design**: Accessible on various devices with an intuitive interface.

## Prerequisites

🚀 How to Run the Project
✅ Prerequisites

Python 3.x installed → Download Python

pip (Python package installer) → included with Python 3.x

Virtual Environment → recommended for isolating dependencies

🔧 Setup Instructions

Clone or download the project

git clone https://github.com/YourRepo/Student-Management-System.git
cd Student-Management-System

Create a virtual environment

python -m venv .venv


Activate the virtual environment

On Windows (PowerShell):

.venv\Scripts\activate


On Linux / Mac:

source .venv/bin/activate


Install dependencies
Use the requirements file you generated:

pip install -r requirements.txt


⚡ If you don’t have requirements.txt yet, create it with:

pip freeze > requirements.txt


Apply database migrations

python manage.py migrate


Run the development server

python manage.py runserver


Open the app in your browser

Local: http://127.0.0.1:8000/

Deployed (PythonAnywhere): https://tyroneljms.pythonanywhere.com/

🎉 Enjoy

You’re all set! Login and start using the LopuesJaena Student Management System 🚀
