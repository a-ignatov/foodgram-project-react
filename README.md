# Для ревью

- сайт доступен по ссылке http://158.160.14.237/recipes
- Админка
```bash
http://158.160.14.237/admin/login/?next=/admin/
```
- Можно залогиниться под qwerty/qwerty
- Ссылка на гит
```bash
https://github.com/a-ignatov/foodgram-project-react
```

# Технологии проекта
![Foodgram workflow](https://github.com/a-ignatov/foodgram-project-react/actions/workflows/main.yml/badge.svg)

[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646??style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![GitHub](https://img.shields.io/badge/-GitHub-464646??style=flat-square&logo=GitHub)](https://github.com/)
[![docker](https://img.shields.io/badge/-Docker-464646??style=flat-square&logo=docker)](https://www.docker.com/)
[![NGINX](https://img.shields.io/badge/-NGINX-464646??style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![Python](https://img.shields.io/badge/-Python-464646??style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646??style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646??style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)

# Foodgram - сервис для публикации рецептов
# Доступен по адресу: http://158.160.14.237/

Сервис позволяет пользователям просматривать рецепты любимых блюд, а также публиковать собственные.
При регистрации пользователь указывает свой email, который будет использоваться при авторизации.

Зарегистрированные пользователи могут подписываться на авторов рецептов или добавлять рецепты в корзину, в избранное.
Есть возможность фильтрации рецептов по тегам, поиск по началу названия ингредиента при добавлении или редактировании рецепта.
![recipe](https://github.com/a-ignatov/foodgram-project-react/blob/868dff2bd8ed2ef3ccdd3a9bdb994d44ab3c5e0d/backend/media/data/Screenshot%202022-11-22%20at%2018.41.58.png)

## Запуск сайта локально
- Склонировать проект и перейти в папку проекта

```bash
git clone git@github.com:a-ignatov/foodgram-project-react.git
cd foodgram-project-react
```
- Установить и активировать виртуальное окружение

```bash
python3 -m venv venv
source venv/bin/activate 
```

- Установить зависимости из файла **requirements.txt**
 
```bash
cd backend
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполнить команды:

```bash
python manage.py makemigrations
python manage.py migrate
```
- Создать пользователя с неограниченными правами:

```bash
python manage.py createsuperuser
```
- Запустить web-сервер на локальной машине:

```bash
python3 manage.py runserver
```

## Docker инструкции
- Установить Docker и получить образ

```bash
docker pull aignatov2/foodgram_backend:latest
docker pull aignatov2/foodgram_frontend:latest
```

Проект можно развернуть используя контейнеризацию Docker  
Параметры запуска описаны в `docker-compose.yml`.

При запуске создаются 3 контейнера:

 - контейнер базы данных **db**
 - контейнер приложения **backend**
 - контейнер web-сервера **nginx**

Для развертывания контейнеров необходимо:

- Создать и сохранить переменные окружения в **.env** файл, образец ниже
```bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

- Запустить docker-compose

```bash
docker-compose up
```
- Выполнить миграции и подключить статику

```bash
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py collectstatic --noinput
```
- Создать superuser

```bash
docker-compose exec backend python manage.py createsuperuser
```

- Зайти в админ-панель Django под суперюзером и создать несколько объектов класса Tag. 

## Ресурсы API Foodgram

- Ресурс auth: аутентификация.
- Ресурс users: пользователи.
- Ресурс tags: получение данных тега или списка тегов рецепта.
- Ресурс recipes: создание/редактирование/удаление рецептов, а также получение списка рецептов или данных о рецепте.
- Ресурс shopping_cart: добавление/удаление рецептов в список покупок.
- Ресурс download_shopping_cart: cкачать файл со списком покупок.
- Ресурс favorite: добавление/удаление рецептов в избранное пользователя.
- Ресурс subscribe: добавление/удаление пользователя в подписки.
- Ресурс subscriptions: возвращает пользователей, на которых подписан текущий пользователь. В выдачу добавляются рецепты.
- Ресурс ingredients: получение данных ингредиента или списка ингредиентов.

Примеры запросов по API:

- [GET] /api/users/ - Получить список всех пользователей.
- [POST] /api/users/ - Регистрация пользователя.
- [GET] /api/tags/ - Получить список всех тегов.
- [POST] /api/recipes/ - Создание рецепта.
- [GET] /api/recipes/download_shopping_cart/ - Скачать файл со списком покупок.
- [POST] /api/recipes/{id}/favorite/ - Добавить рецепт в избранное.
- [DEL] /api/users/{id}/subscribe/ - Отписаться от пользователя.
- [GET] /api/ingredients/ - Список ингредиентов с возможностью поиска по имени.