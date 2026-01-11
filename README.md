# Laravel Internship Assignment

This repository contains the completed internship assignment as provided by Hunt Digital Media.  
The assignment demonstrates Laravel setup, database integration, Selenium automation using Python, and HTML template integration.

---

## 📌 Project Overview

The assignment consists of three main tasks:

1. Running a Laravel project locally with database integration.
2. Automating the Laravel login page using Python Selenium.
3. Integrating an external HTML calendar template into the Laravel project.

All tasks have been implemented and verified successfully.

---

## ✅ Task 1: Laravel Project Setup

- The Laravel project was extracted and set up on a local development environment.
- Required dependencies were installed using Composer.
- Database was imported using the provided `db.sql` file.
- The application was successfully run on a local server.
- Login page was accessed and verified.

🔗 Login Page URL:
http://127.0.0.1:8000/login

yaml
Copy code

📸 Screenshot:
- `task1-login-page.png`

---

## ✅ Task 2: Selenium Automation (Python)

- A Python Selenium script was created to automate the Laravel login page.
- The script performs the following actions:
  - Opens the Laravel login page.
  - Automatically fills the email and password fields with random values.
  - Closes the browser after execution.
- Selenium 4 (Selenium Manager) was used for automatic browser driver handling.

📄 Script File:
- `login_test.py`

📸 Screenshot:
- `task2-selenium-automation.png`

---

## ✅ Task 3: HTML Calendar Integration

- An external HTML calendar template was integrated into the Laravel project.
- The HTML file was converted into a Blade view.
- A custom route was created to display the calendar page inside Laravel.

🔗 Calendar Page URL:
http://127.0.0.1:8000/html-page

yaml
Copy code

📸 Screenshot:
- `task3-calendar-page.png`

---

## ▶️ How to Run the Project

### Run Laravel Application
```bash
php artisan serve
Open the browser and visit:

arduino
Copy code
http://127.0.0.1:8000/login
Run Selenium Automation Script
bash
Copy code
python login_test.py
🧰 Technologies Used
Laravel (PHP Framework)

MySQL

Python 3

Selenium 4

HTML / CSS / JavaScript

Git & GitHub

👤 Submitted By
Saloni Saini

