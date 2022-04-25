```
django-admin startproject factory - создание проекта
python manage.py startapp educational-program - создание приложение "пользователи"

python -m venv .venv – создание виртуального окружения Windows
source .venv/Scripts/activate – активация виртуального окружения Windows
pip install -r requirements.txt – установка зависимостей из requirements.txt
python manage.py runserver - запуск сервера
python manage.py collectstatic - сгенерировать статику

python manage.py makemigrations - создать миграции
python manage.py migrate - применить миграции

pip freeze – вывести установленные модули в консоль
pip freeze > requirements.txt – сохранить установленные модули в файл

Первый запуск
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Последующие запуски
source .venv/Scripts/activate
python manage.py runserver


TODO

```
