# Test automation coverage dashboard

### Как запустить локально

1. apt install python3 -venv
2. python3 -m venv env
3. source env/bin/activate
4. pip install -U pip
5. pip install -r requirements.txt
6. python manage.py migrate
7. python manage.py runserver

### Q & A
* Проверка установленной версии
  
  >django-admin --version   

* Старт Django-проекта

    >django-admin startproject coverage
* Корень проекта = директория с файлом manage.py

* Справка по приложению 

  >python manage.py --help

* Добавление нового приложения  
  > django-admin startapp [name app]
  > 
* Создание миграций
  >python manage.py makemigrations 
* Выполнение миграций
  >python manage.py migrate


### База данных
Изменить параметры подключения к базе данных можно в файле coverage_app/setting.py в переменной DATABASES.

По умолчанию используется PostgreSQL


### Как запустить через docker-compose
Скачайте репозиторий. В директории скаченного проекта выполните команду
> docker-compose up

По умолчанию создается superuser admin
###### Веб-сервер - uWSGI

###### Сервер приложений - Gunicorn

###### Обратный прокси-сервер - Nginx

###### Инструкция по деплою - https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04-ru
