# Robust Teacher Portal

A modern, secure, and scalable Django web application for managing student records, designed for teachers. The portal features a beautiful UI, advanced UX, and robust backend logic for adding, editing, and deleting student records.

---

## ✨ Features

- **User Authentication:** Secure login/logout for teachers.
- **Student Dashboard:** View all students in a responsive, searchable table.
- **Add Student (Modal):** Add new students via a Bootstrap modal. If a student with the same name and subject exists, their marks are incremented.
- **Edit Student:** Update student details with validation and unique constraints.
- **Delete Student:** Confirm and delete student records with a confirmation dialog.
- **Advanced UI:** Uses Bootstrap 5, Bootstrap Icons, and Google Fonts for a modern look.
- **Security:** CSRF protection, input validation, and Django’s authentication system.
- **Scalable Architecture:** Modular Django app structure, ready for future enhancements.

---

## 🛠️ Tech Stack

- **Backend:** Django 4.x (Python 3.7+)
- **Frontend:** Bootstrap 5, Bootstrap Icons, Google Fonts
- **Database:** SQLite (default, easy to switch to PostgreSQL/MySQL)

---

## 🚀 Project Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/amol127/Robust_Teacher_Portal.git
cd Robust_Teacher_Portal
```

### 2. Create and Activate a Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django
```

*If you have a `requirements.txt` file, use:*
```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
cd Teacher_Portal
python manage.py migrate
```

### 5. Create a Superuser (for admin access)

```bash
python manage.py createsuperuser
```
- Follow the prompts to set username, email, and password.

### 6. Run the Development Server

```bash
python manage.py runserver
```

### 7. Access the Application

- **Teacher Portal:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### 8. (Optional) Load Initial Data

If you have fixtures or want to load sample data:
```bash
python manage.py loaddata <fixture_name>.json
```

### 9. Deactivating the Virtual Environment

When done, deactivate with:
```bash
deactivate
```

---

## 📦 Requirements

- Python 3.7+
- Django 4.x (or as specified in your requirements)
- (Optional) Other dependencies as needed

---

## 🖥️ Usage

### Login
- Teachers must log in to access the portal.
- The login page features a modern design, input icons, and a "Forgot Password?" link (placeholder).

### Dashboard
- View all students in a table.
- Use the "Add Student" button to open a modal for new entries.

### Add Student
- Enter name, subject, and marks.
- If a student with the same name and subject exists, their marks are incremented.
- Otherwise, a new student is created.

### Edit Student
- Click "Action" → "Edit" to update student details.
- Unique constraint: No two students can have the same name and subject.

### Delete Student
- Click "Action" → "Delete" to confirm and remove a student.

---

## 🗃️ Models

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    marks = models.PositiveIntegerField()

    class Meta:
        unique_together = ('name', 'subject')
```

---

## 🔒 Security Best Practices

- **Authentication:** All student management views require login.
- **CSRF Protection:** Enabled by default for all forms.
- **Input Validation:** All fields are validated server-side.
- **Unique Constraints:** Prevents duplicate student entries.
- **Session Security:** Uses Django’s secure session management.

---

## 🏗️ Scalability & Maintainability

- **Modular Django app structure** for easy extension.
- **Reusable templates** and Bootstrap-based UI.
- **Settings management** for different environments.
- **Admin registration** for easy data management.

---

## 🧪 Testing

- **Unit tests:** Add tests in `portal/tests.py` using Django’s `TestCase`.
- **Integration tests:** Use Django’s test client to simulate user actions.
- **Manual E2E testing:** Recommended for UI/UX flows.

_Example test:_
```python
from django.test import TestCase
from .models import Student

class StudentTestCase(TestCase):
    def test_add_student_marks_update(self):
        s = Student.objects.create(name="John", subject="Math", marks=10)
        response = self.client.post('/student/add/', {'name': 'John', 'subject': 'Math', 'marks': 5})
        s.refresh_from_db()
        self.assertEqual(s.marks, 15)
```

---

## 🚦 Extending the Portal

- **Password Reset:** Integrate Django’s password reset views for full functionality.
- **User Roles:** Add staff/admin roles for more granular permissions.
- **APIs:** Expose student data via Django REST Framework for integration.
- **Advanced Search/Filter:** Add search and filter capabilities to the student list.
- **Notifications:** Use Django messages or real-time notifications for user feedback.

---

## 📄 License

MIT License (or your chosen license)

---

## 🤝 Contact

For questions or contributions, please open an issue or pull request.

---

**Enjoy your robust, modern Teacher Portal!**