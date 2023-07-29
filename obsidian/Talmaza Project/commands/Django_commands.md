### To start django project
```cmd
django-admin startproject [devsearch]
```
in this case we make django project named "devsearch"
### To start django app
```cmd
python manage.py startapp [projects]
```
in this case we make django app in side the project named "projects"
```cmd
python manage.py runserver
```
To run the server inside the project
```cmd
python manage.py migrate
```
to create our inertial database tables
```cmd
python manage.py makemigrations
```
to add table we write it in the models file
example: if we add project modle
Migrations for 'projects':
  projects\\migrations\\0001_initial.py
    - Create model Project
after that we run ```python manage.py migrate``` command it will take our makemigrations that we make and put it in our database
```cmd
python manage.py createsuperuser
```
to craete super user in the database
```cmd
python manage.py shell
```
open python shell
