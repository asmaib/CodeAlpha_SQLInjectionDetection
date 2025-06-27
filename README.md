# SQL Injection Detection

A FastAPI-based web application that detects potential SQL injection attempts in user input and stores data securely using encrypted passwords.  
Built as part of the **CodeAlpha Internship Task 2**.

## 📌 Live Demo
🔗 [Visit the live site here](https://sql-injection-detector-zyq1.onrender.com)  

---

## 🚀 Features

- Detect basic SQL injection patterns in usernames and passwords.
- Prevent injection-based data leaks.
- Secure password storage using Fernet encryption.
- Add users with validated input.
- SQLite backend (lightweight, no external DB required).
- Clean and responsive frontend (HTML/CSS/JS).
- Deployed on Render with auto-deploy on push.

---

## 🛠️ Technologies Used

- **Python** 3.11+
- **FastAPI** (Backend)
- **SQLAlchemy + SQLite** (Database)
- **Fernet / Cryptography** (Encryption)
- **HTML, CSS, JavaScript** (Frontend)
- **Render** (Deployment platform)

---

## 📁 Project Structure

```
CodeAlpha_SQLInjectionDetection/
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
├── main.py # FastAPI app entry point
├── database.py # DB config and SQLite connection
├── models.py # Pydantic input models
├── security.py # Password encryption/decryption
├── requirements.txt # Project dependencies
├── render.yaml # Render deployment config
└── README.md # Documentation
```

---

## ✅ How It Works

1. User fills the login/signup form in the frontend.
2. The input is checked for common SQL injection patterns.
3. If input is safe, the password is encrypted and stored.
4. All responses are shown with real-time alerts in the UI.

---

## 🧑‍💻 Author
- Asma Alshilash
