# flask-todo-web-client
A simple CLI todo app web client

### Usage

- Deploy "atlasrule/flask-todo-web-server" on a cloud service with a procfile includes: "web: gunicorn wsgi:app"
- Update "socket_adress" in client main.py with your server domain/ip.
- Run "atlasrule/flask-todo-web-client" wsgi.py
- Select operation

| Command | Operation                       |
| ------- | ------------------------------- |
| 1       | CREATE an item                  |
| 2       | READ an item status             |
| 3       | READ Todo list                  |
| 4       | UPDATE an item as "Not Started" |
| 5       | UPDATE an item as "In Progress" |
| 6       | UPDATE an item as "Completed"   |
| 0       | Exit client                     |
