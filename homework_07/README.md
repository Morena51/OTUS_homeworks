# Test Coverage Dashboard

### Где развернуто

http://172.23.12.112/

### Как запустить локально

1. apt install python3 -venv
2. python3 -m venv env
3. source env/bin/activate
4. pip install -U pip
5. cd mysite
6. pip install -r requirements.txt
7. export ALLURE_USERNAME=''
8. export ALLURE_PASSWORD=''
9. python3 manage.py runserver

### Как развернуто

###### БД - PostgreSQL

###### Веб-сервер - uWSGI

###### Сервер приложений - Gunicorn

###### Обратный прокси-сервер - Nginx

###### Инструкция по деплою - https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04-ru
