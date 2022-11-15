# Технологии проекта
![Foodgram workflow](https://github.com/a-ignatov/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646??style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![GitHub](https://img.shields.io/badge/-GitHub-464646??style=flat-square&logo=GitHub)](https://github.com/)
[![docker](https://img.shields.io/badge/-Docker-464646??style=flat-square&logo=docker)](https://www.docker.com/)
[![NGINX](https://img.shields.io/badge/-NGINX-464646??style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![Python](https://img.shields.io/badge/-Python-464646??style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646??style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646??style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)


# Проект Foodgram
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен администратором (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха.
Произведению может быть присвоен жанр (Genre) из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

## Установка
Склонируйте репозиторий.
cd api_yamdb
Cоздать и активировать виртуальное окружение: python -m venv venv
source venv/scripts/activate
python -m pip install --upgrade pip
Установить зависимости из файла requirements.txt: pip install -r requirements.txt
Выполнить миграции: python manage.py migrate
Запустить проект: python manage.py runserver
Проект запущен и доступен по адресу [localhost:8000](http://localhost:8000/).

## Ресурсы API YaMDb
