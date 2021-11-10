<h1>Микро-БЛОГ [FastAPI]</h1>


<h4>Запуск БД в Docker</h4>

```bash
# с удалением контейнера
sudo docker run --name microblog -e POSTGRES_PASSWORD='qwerty' -e POSTGRES_DB=microblog -p 5436:5432 -d --rm postgres
# без удаления контейнера
sudo docker run --name microblog -e POSTGRES_PASSWORD='qwerty' -e POSTGRES_DB=microblog -p 5436:5432 -d postgres
```

<h4>Инициализация дирректории с миграциями</h4>

```bash
alembic init migrations
```

<h4>Создание миграций</h4>

```bash
# создание файла с миграции
alembic revision --autogenerate -m "Название миграции"
# выполнение миграции
alembic upgrade head
```

<h4>Зайти в базу данных</h4>

```bash
sudo docker exec -it container_id bin/bash
psql -U postgres
```

