# Bootstrap Inspired User Authentication System

This repository features a Python-based web application leveraging the Bootstrap framework for user interface design and provides functionalities such as login, registration, password reset, and admin user management.

## Features
- **Login Page:** Allows users to authenticate using their username and password.
- **Welcome Page:** Displays a personalized welcome message following successful login.
- **Password Reset Page:** Allows users to reset their password by providing their username and email address. A verification email is sent before resetting the password.
- **Registration Page:** Permits new users to create an account with a username, email, and password. Email verification is required before the account becomes active.
- **Admin Page:** Enables an admin user to manage all registered users. The admin can deactivate users, reset passwords, and update user information. Admin's login details are pre-configured: username `admin` and password `superadmin`.

## Design Principles
- **Language & Architecture:** The backend is developed in Python and maintains a lightweight architecture.
- **UI Framework:** The application uses [Bootstrap](https://getbootstrap.com/) to ensure responsive and aesthetic design. The primary theme color of the app is blue.

## Development
1. Clone the repository:
   ```
   git clone https://github.com/tangdung139-cell/gstest-open-swe.git
   cd gstest-open-swe
   ```
2. Set up the Python environment:
   ```
   python -m venv env
   source env/bin/activate   # For Unix
   env\Scripts\activate    # For Windows
   pip install -r requirements.txt
   ```
3. Run the development server:
   ```
   python app.py
   ```
4. Access the application at `http://localhost:5000`.

## Contribution Guide
Please ensure all changes adhere to the repository's contribution guidelines and align with the design principles outlined above.