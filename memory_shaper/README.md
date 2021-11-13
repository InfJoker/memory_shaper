Ручки в папке [handlers](https://github.com/InfJoker/memory_shaper/tree/master/memory_shaper/handlers)

Чтобы понять, как что работает почитайте [доку](https://flask-doc.readthedocs.io/en/latest/quickstart.html)

Вся схема и классы описаны в [models.py](https://github.com/InfJoker/memory_shaper/blob/master/memory_shaper/models.py)

В файле [app.py](https://github.com/InfJoker/memory_shaper/blob/master/memory_shaper/app.py) у нас есть объект `Session`

Если хотите делать запросы к базе то создаете эту сессию c помощью `new_sql_session`:
```python
from memory_shaper.app import new_sql_session
sql_session = new_sql_session()
```
и работаете с ней.

Гайд можно прочитать начиная отсюда https://docs.sqlalchemy.org/en/13/orm/session_basics.html#basics-of-using-a-session

Договоримся, что  если пишем `sql_session.add(something)` или `sql_session.delete(something)` то в конце пишем `sql_session.commit()`

Пример:
```python
sql_session.add(something)
sql_session.commit(something)
```
Нужно переделать, чтобы работало с `session.begin()` но сейчас не об этом
