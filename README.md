## Table of Contents

  * [Abstract](#abstract)
  * [Getting Started](#getting-started)

## Getting Started

- This app is using Django DRF for backend and React for frontend.
- Both of the apps are run on different port.
- User is authenticated using JWT auth token.
- Django uses CORS package to allow React app communicate with Django

## Getting Started

### 1. Github

- Clone repository using below command

  ```
  https://github.com/gajanankathar/fsp-gftglobal.git
  ```
  
   
### 2. Virtual environment

- Create a virtual environment inside backend directory using python3.6 or above 
  ```
  cd backend
  python -m venv venv
  ```
- Activate it
- Windows
  ```
  .\venv\Scripts\activate.bat
  ```
- Linux
  ```
  source venv/bin/activate
  ```
- Use this virtual environment for subsequent tasks
   
### 3. `pip`

- You will find the requirements.txt file inside backend/gftglobal directory
- Install all the requirements from requirements.txt
  ```
  pip install -r requirements.txt
  ```
  
### 4. DB Migrations

- Do DB migrations
- You should be in backend/gftglobal directory to fire below commands
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```

### 4. Run Django Server.

- Ensure that, you in backend/gftglobal directory to run django development server
  ```
  python manage.py runserver
  ```
- Now, our django server is up and running without any issues

### 5. Git clone React submodule

- Make sure to also clone react app git submodules.
  ```
  git submodule update --init
  ```

### 6. Run React app 

- Run react app in separate terminal
- Go to the frontend/partner-portal directory 
  ```
  npm install
  npm start
  ```
- This will run react app on http://localhost:3000/


### 6. Sitemap 

- Create new customer
  ```
  http://localhost:3000/register/
  ```
- Once you fill all the details and click register button, new customer gets added
to DB and new user created with username as customer first name in lower case and 
with default password as "password".

- Login using new user
  ```
  http://localhost:3000/login/
  ```
- You are redirected to home page after login and on home page customer details will be displayed.

- If you wish to edit, choose edit button and edit the form and hit update button.
- Your changes will be saved in the DB and same reflected on the home page.
  
- Logout: Click on the "Logout" button at the right upper corner to logout from the system.
