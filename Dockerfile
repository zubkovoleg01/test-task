FROM python:3.9

WORKDIR /api

COPY . .

# Установка зависимостей из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Запуск парсера для БД - cinemas.db
RUN python parser.py

CMD ["python", "manage.py", "runserver", "0.0.0.0:8008"]
