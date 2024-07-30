# Django Advanced Blog



# What is this project?
<span><img src="https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=green" /></span>
<span><img src="https://img.shields.io/badge/Docker-2CA5E0?style=flat&logo=docker&logoColor=white" /></span>
<span></span>

This is a boilerplate to start a django project with sqllite as database running on docker.

# How to use?

<strong>If you want to get notified about the future changes Follow my github account.</strong>

First clone the project.

```bash
git clone https://github.com/mammadsafar/Django-Advanced-Blog.git
```

Then make sure Docker is running.
* If you are on windows click on the Docker Desktop icon and wait for about a minute.

Then in the project directory run this command:

```bash
docker-compose up --build
```

It will create two containers:
One for Django and one for PostgreSql as the database for the project.
All the required packages will be installed.

### Migrate DB.

```bash
docker-compose exec backend sh -c "python manage.py makemigrations"
docker-compose exec backend sh -c "python manage.py migrate"
``` 

for create superuser or admin user this

```bash
docker-compose exec backend sh -c "python manage.py createsuperuser"
``` 
and use email and pass word to login as admin

 go to 127.0.0.1:8000/admin/ for access to admin panel


### API Documention

 go to 127.0.0.1:8000/swagger/ or 127.0.0.1:8000/redoc/

### API Documention for postman
 to use json file to import document to post man go to 127.0.0.1:8000/swagger/output.json


for install package use
```bash
docker-compose exec backend sh -c "pip install <pakagename>"
```

# Run with Docker
just run this command
```bash
docker-compose up -t --build
```



