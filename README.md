

---

🚀 FastAPI Tasks Collection

This repository contains multiple FastAPI mini-projects (Tasks 1–5) that demonstrate building REST APIs with different features such as file handling, query/path parameters, and JSON storage.


---

📦 Installation

1. Clone the repo:

git clone https://github.com/adannalyn/tasks.git
cd tasks


2. Create a virtual environment (recommended):

python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


3. Install dependencies:

pip3 install -r requirements.txt




---

📝 Tasks

Task 1: File Handler Module

Utility functions for saving and loading JSON data.

Used in later tasks for persistence.



---

Task 2: Student Management API

Manage students (name, age, grade).

Endpoints:

POST /students/

GET /students/


Data saved in students.json using file_handler.py.



---

Task 3: Job Application Tracker API

Track job applications with:

name, company, position, status


Endpoints:

POST /applications/

GET /applications/

GET /applications/search?status=pending


Data saved in applications.json.



---

Task 4: Notes App API (File System Support)

Add, read, update, and delete notes saved as .txt files.

Endpoints:

POST /notes/

GET /notes/{title}

PUT /notes/{title}

DELETE /notes/{title}




---

Task 5: Simple Contact API (Path & Query Parameters)

Manage contacts (name, phone, email) in memory.

Endpoints:

POST /contacts → Create contact

GET /contacts?name=John → Fetch by name

POST /contacts/{name} → Update

DELETE /contacts/{name} → Delete


Uses pydantic.EmailStr for validation.



---

▶️ Running the Apps

Each task has its own main.py. Run with:

uvicorn main:app --reload

Then open your browser at:

👉 http://127.0.0.1:8000/docs for interactive API docs.


---

📋 Requirements

Dependencies are managed in requirements.txt.
To save current environment into requirements:

pip3 freeze > requirements.txt

To install later:

pip3 install -r requirements.txt


---

🛠️ Tools Used

FastAPI

Uvicorn

Pydantic



---
