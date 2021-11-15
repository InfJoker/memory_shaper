# Memory Shaper

Web-cервис для работы с [flash-карточками](https://en.wikipedia.org/wiki/Flashcard).

[Презентация](https://www.canva.com/design/DAEvtLso758/XvV7IUnFqkkS-UJnjgFQ3Q/view?utm_content=DAEvtLso758&utm_campaign=designshare&utm_medium=link&utm_source=sharebutton)

## Как поднять локально

У вас уже должен быть установлен 'docker' и 'docker-compose'.

### Поднимаем все приложение
В этом случае автоматически поднимается база, если она еще не поднята, и накатываются миграции.
```
docker-compose up memory_shaper
```

### Поднимаем базу и накатываем накатываем миграции.

Замечу: чтобы просто повторно накатить миграции достаточно еще раз запустить эту команду.
```
docker-compose up db-migrate
```

## Запуск в PyCharm

Открываете проект как Flask application.

Устанавливаем venv и ставим в него зависимости из [requirements.txt](https://github.com/InfJoker/memory_shaper/blob/master/requirements.txt)

Далее конфигурируем запуск:

В Target пишем `{путь до run_app.py}/run_app.py`

В `FLASK_ENV` пишем `development`

В `Environment variables` прописываем `APP_ENVIRONMENT=Dev;DATABASE_URL=postgresql+psycopg2://postgres:passw0rd@localhost:5432/shaper;SECRET_KEY=secret`

## Из консоли

Сидим в корневой директории проекта.

Делаем себе venv и ставим все из [requirements.txt](https://github.com/InfJoker/memory_shaper/blob/master/requirements.txt)

Устанавливаем переменные окружения
```
APP_ENVIRONMENT=Dev;DATABASE_URL=postgresql+psycopg2://postgres:passw0rd@localhost:5432/shaper;SECRET_KEY=secret;FLASK_APP=memory_shaper/run_app.py
export APP_ENVIRONMENT DATABASE_URL SECRET_KEY FLASK_APP
```
Запускаем нашу красоту
```
python -m flask run
```
