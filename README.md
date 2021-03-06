# ![Pooling](project-logo.png)

## Общая информация

Задание - https://github.com/avito-tech/mi-trainee-task-2021

Вторая реализация с использованием Flask и Swagger (об этом написано в `Дополнительные ответы/Readme.txt`) - https://github.com/YegorYurchenko/Polling_JSON

При работе использовался [Python](https://www.python.org/) версии [3.9.5](https://www.python.org/downloads/release/python-395/) и [Django](https://www.djangoproject.com/) версии [3.2.4](https://docs.djangoproject.com/en/3.2/releases/3.2.4/).

Frontend написан с помощью HTML, CSS и JavaScript.

## Установка

1. Клонируйте репозиторий: `git clone https://github.com/YegorYurchenko/Polling.git`
1. Перейдите в папку Polling и создайте виртуальное окружение (в консоли): `py -m venv env`
1.  `Необязательно`: если вы используете VS Code, то установите расширение `Python`, зажмите `Ctrl+Shift+P`, напишите `Python: Select Interpreter` и выберите `Enter interpreter path...` -> `Find...` -> `env/Scripts/python.exe`
1. Запустите виртуальное окружение: `env/Scripts/activate`
1. Установите зависимости: `pip install -r requirements.txt`
1. Перейдите в папку `src`: `cd src`
1. Сделайте миграцию: `py manage.py migrate`
1. `Необязательно`: создайте суперюзера - `py manage.py createsuperuser`

## Запуск

1. `py manage.py runserver` - запуск проекта. После запуска сборки заработает локальный сервер по адресу `http://127.0.0.1:8000/`
1. `py manage.py test`- запуск тестов.

## Структура проекта

* `env` - виртуальное окружение
* `src` - исходники
    * `all_polls` - приложение для всех голосований
        * `templates` - html
        * `urls.py`
        * `views.py`
    * `create_poll` - приложение для создания нового голосования
        * `static` - js
        * `templates` - html
        * `forms.py`
        * `urls.py`
        * `views.py`
    * `poll` - приложение для выбранного голосования
        * `migrations` - файлы миграции
        * `static` - css, js, img
        * `templates` - html
        * `models.py`
        * `urls.py`
        * `views.py`
    * `polling` - основные файлы проекта
        * `settings.py` - настройки проекта
        * `urls.py` - основные url
    * `tests`
        * `test_forms.py`
        * `test_models.py`
        * `test_utils.py`
        * `test_views.py`
    * `db.sqlite3`
    * `manage.py`
* `.gitignore`
* `README.md`
* `requirements.txt` - необходимые зависимости
