# CodaTech_UserAdmin
A web application for CRUD operations using Django Framework

## Installation guide
### 1) Clone repository
```
git clone https://github.com/dhurataK/CodaTech_UserAdmin.git
```

### 2) Change directory (cd) to reposotiry CodaTech_UserAdmin
```
cd CodaTech_UserAdmin
```
### 3) Create a virtual environment in your virtual environment folder.
    + If you're using Mac:
    ```
    > virtualenv djangoEnv
    ```
    + If you're using a PC:
    ```
    > python -m virtualenv djangoEnv
    ```
### 4) Activate your virtual environment
    + If you're using Mac:
    ```
    > source djangoEnv/bin/activate
    ```
    + If you're using a PC:
    ```
    > call djangoEnv/scripts/activate
    ```
### 5) Install required packages  
```
(djangoEnv)>pip install -r requirements.txt
```
## Running the tests

### 1) Change directory (cd) to UserAdmin folder
```
cd UserAdmin
```

### 2) Make migration
```
python manage.py migrate
```

### 3) Run the server
```
python manage.py runserver  
```
### 4) Open up the browser http://localhost:8000/

## Built With
* [Django](https://www.djangoproject.com/) - The web framework used
* [PostgreSQL](https://www.postgresql.org/) - Database
* [Python](https://www.python.org/) - Version 3.6.2
