A test assignment for the position of a backend developer in the studio of Artemy Lebedev.

_______________________________________________________________________________________________________________________________________________

Requirements specification:

Необходимо представить себя на месте разработчика сервиса, предоставляющего другим компаниям доступ к открытым данным, и написать API, который позволяет получить эти данные по HTTP. 

Нужно:

1. Взять любую таблицу длиной более 100 строк из реестра открытых данных Минкульта России https://opendata.mkrf.ru/opendata.
 
3. Написать парсер на Python, который сохранит данные из таблицы в базу данных.
  
3. Реализовать на Django API для доступа к базе данных.
  
4. Реализовать поиск по данным через API.

5. Создать Docker-образ, который парсит встроенную в него таблицу и поднимает сервер с базой данных и API.

6. Написать документацию к API.


Результат выполнения тестового задания: ссылка на репозиторий в «Гитхабе» и ссылка на образ в «Докер-хабе». Ответы принимаются до 30 апреля 23:59:59.
Это письмо отправлено роботом. Студия не имеет возможности вступать в переговоры о сроках и условиях выполнения тестовых заданий.

_______________________________________________________________________________________________________________________________________________

Process of implementation:

1. A table was taken at https://opendata.mkrf.ru/opendata/7705851331-cinema.

2. A parser was written for it that interacts with the database.

3. An API for accessing the database has been implemented.

4. The API for searching data by name and city has been implemented.

5. A Docker image has been created that parses the table embedded in it and raises the server with the database and API.

6. Documentation has been written using drf-yasg.

_______________________________________________________________________________________________________________________________________________

The result of the work:

Github - https://github.com/zubkovoleg01/test-task

DockerHub - https://hub.docker.com/repository/docker/zoleg01/cinemas/general

_______________________________________________________________________________________________________________________________________________
