# Project Setup Guide

## Backend (Django)

1. **Set up the backend**:
   - Navigate to the backend directory in your terminal.

2. **Make Migrations**:
   - Run the following command to create migration files:
     ```bash
     python manage.py makemigrations
     ```

3. **Apply Migrations**:
   - Run the following command to apply the migrations:
     ```bash
     python manage.py migrate
     ```

4. **Run the Development Server**:
   - Finally, run the Django development server with:
     ```bash
     python manage.py runserver
     ```

   Your backend should now be up and running at `http://127.0.0.1:8000/` by default.

---

## Frontend (React)

1. **Install Dependencies**:
   - Navigate to the frontend directory in your terminal.
   - Install the necessary dependencies using npm:
     ```bash
     npm install
     ```

2. **Start the Development Server**:
   - After the dependencies are installed, start the frontend development server:
     ```bash
     npm start
     ```

   Your frontend should now be accessible at `http://localhost:3000/` by default.

---

### Notes

- Ensure you have the required dependencies installed for both the backend (Django) and frontend (React) before running the commands.
- If you encounter any issues, please refer to the respective documentation for [Django](https://docs.djangoproject.com/en/stable/) and [React](https://reactjs.org/docs/getting-started.html).

### View
<img width="736" alt="image" src="https://github.com/user-attachments/assets/b8552171-23da-4517-9d98-a1d0af197f3c" />
