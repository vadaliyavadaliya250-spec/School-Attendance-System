# 🏫 School Attendance Management System

A web-based **School Attendance Management System** designed to simplify and manage student attendance digitally.

The system allows administrators and teachers to manage students, classes, attendance records, and generate attendance information through an easy-to-use interface.

## 🚀 Features

* 👨‍🎓 Student Management
* 👩‍🏫 Teacher Management
* 🏫 Class Management
* 📋 Daily Attendance Management
* ✅ Mark Students Present/Absent
* 📅 View Attendance by Date
* 📊 Attendance Reports
* 🔍 Search and Filter Students
* 🔐 Admin Login
* 📱 Responsive User Interface
* 💾 Database-based Attendance Records

## 🛠️ Technologies Used

* Python
* Flask
* HTML5
* CSS3
* JavaScript
* Bootstrap
* SQLite

## 📁 Project Structure

```text
school-management-system/
│
├── app.py
├── database.db
├── requirements.txt
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── students.html
│   ├── attendance.html
│   └── reports.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── images/
│
└── README.md
```

> The actual folder structure may vary depending on the project implementation.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Or download the project as a ZIP file and extract it.

### 2. Open the Project Folder

Open the project in **Visual Studio Code** or another code editor.

```bash
cd school-management-system
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Required Packages

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install flask
```

### 5. Run the Application

```bash
python app.py
```

The application will normally be available at:

```text
http://127.0.0.1:5000/
```

## 📚 Main Modules

### 🔐 Admin Module

The administrator can:

* Login securely
* Manage students
* Manage teachers
* Manage classes
* View attendance records
* Generate attendance reports

### 👨‍🎓 Student Module

Student information can include:

* Student name
* Student ID
* Class
* Roll number
* Contact information
* Attendance history

### 📋 Attendance Module

Teachers/admins can:

* Select a class
* Select attendance date
* View students
* Mark students as Present or Absent
* Save attendance records
* View previous attendance

### 📊 Attendance Reports

The system can provide:

* Daily attendance
* Student attendance history
* Class attendance
* Present/Absent records
* Attendance percentage

## 🔄 System Workflow

```text
Admin / Teacher Login
        ↓
    Dashboard
        ↓
 Select Class
        ↓
 View Students
        ↓
 Mark Attendance
        ↓
 Save Attendance
        ↓
 Database
        ↓
 View Attendance Reports
```

## 💾 Database

The system uses **SQLite** to store application data.

Example database information:

```text
Students
├── id
├── name
├── roll_number
├── class
└── contact

Attendance
├── id
├── student_id
├── date
└── status
```

## 📱 Responsive Design

The system can be accessed from:

* 💻 Desktop
* 📱 Mobile
* 📲 Tablet

## 🔒 Security

The system includes basic security practices such as:

* Admin authentication
* Session management
* Form validation
* Database protection
* Controlled access to attendance records

## 🔮 Future Improvements

Possible future features include:

* 📱 QR Code Attendance
* 🤳 Face Recognition Attendance
* 📧 Email Notifications
* 📲 SMS Notifications
* 📊 Advanced Analytics Dashboard
* 📄 PDF Attendance Reports
* 📥 Excel Export
* 👨‍👩‍👧 Parent Login
* 🧑‍🏫 Teacher-specific Login
* ☁️ Cloud Database
* 📱 Mobile Application
