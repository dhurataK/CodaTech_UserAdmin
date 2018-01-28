# CodaTech_UserAdmin
A web application for CRUD operations using Django Framework

## Installation guide
### Clone repository
```
git clone https://github.com/dhurataK/CodaTech_UserAdmin.git
```
### Change directory (cd) to reposotiry CodaTech_UserAdmin
```
cd CodaTech_UserAdmin
```
### Create a virtual environment in your virtual environment folder.
**If you're using Mac:**
```
> virtualenv djangoEnv
```
**If you're using a PC:**
```
> python -m virtualenv djangoEnv
```
### Activate your virtual environment

**If you're using Mac:**
```
> source djangoEnv/bin/activate
```
**If you're using a PC:**
```
> call djangoEnv/scripts/activate
```
### Install required packages  
```
(djangoEnv)>pip install -r requirements.txt
```
## Running the tests

### Change directory (cd) to UserAdmin folder
```
cd UserAdmin
```
### Make migration
```
python manage.py migrate
```
### Run the server
```
python manage.py runserver  
```
### Open up the browser http://localhost:8000/
## Built With
* [Django](https://www.djangoproject.com/) - The web framework used
* [PostgreSQL](https://www.postgresql.org/) - Database
* [Python](https://www.python.org/) - Version 3.6.2
