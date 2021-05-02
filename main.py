# Server request lookup table:

# Root directory (homepage)
# curl -X GET http://127.0.0.1:5000/

# Create an item
# curl -X POST http://127.0.0.1:5000/item -d "{\"item\": \"Setting up Flask\"}" -H 'Content-Type: application/json'

# Read an item
# curl -X GET http://127.0.0.1:5000/item/status?name=Setting+up+Flask

# Read all items
# curl -X GET http://127.0.0.1:5000/items/all

# Update an item
# curl -X PUT http://127.0.0.1:5000/item/update -d '{"item": "Setting up Flask", "status": "Completed"}' -H 'Content-Type: application/json'

# Delete an item
# curl -X DELETE http://127.0.0.1:5000/item/remove -d '{"item": "Setting up Flask"}' -H 'Content-Type: application/json'


import requests, json, socket
from os import system

address = 'flask-todo-web-server.herokuapp.com'


socket_address = 'http://{}'.format('flask-todo-web-server.herokuapp.com')



def main():

    first_run = True

    # The main CLI loop
    while True:

        if first_run:
            show_greeting_message()
            first_run = False

        else:
            system('cls')

        print("""

                  (1) CREATE an item
                 (2) READ an item status
                (3) READ Todo list
               (4) UPDATE an item as "Not Started"
              (5) UPDATE an item as "In Progress"
             (6) UPDATE an item as "Completed"
            (0) Exit client

        """)

        select = int(input('    Selection: '))

        if select == 1:
            item_name = input('    Item name: ')
            create_todo_item(item_name)

        elif select == 2:
            item_name = input('    Item name: ') 
            get_todo_item(item_name)

        elif select == 3:
            get_all_todo_items()

        elif select == 4:
            item_name = input('    Item name: ')
            update_todo_item(item_name, "Not Started")

        elif select == 5:
            item_name = input('    Item name: ')
            update_todo_item(item_name, "In Progress")

        elif select == 6:
            item_name = input('    Item name: ')
            update_todo_item(item_name, "Completed")

        elif select == 0:
            exit(0)

        else:
            print('   -Invalid Input-')

        input('Press a button to continue...')


def show_greeting_message():
    url = socket_address

    headers = {'Content-Type': 'application/json'}

    response = requests.get(url, headers=headers)

    content = response.content.decode("utf-8") 

    print(content)


def  create_todo_item(item):

    url = socket_address + '/item/new'

    headers = {'Content-Type': 'application/json'}

    data = json.dumps( {'item': item} )

    response = requests.post(url, headers=headers, data=data)

    print(response.content)


def  get_todo_item(item):
    url = socket_address + '/item/status'

    headers = {'Content-Type': 'application/json'}

    params = {'name': item}

    response = requests.get(url, headers=headers, params=params)

    print(response.content)


def  get_all_todo_items():

    url = socket_address + '/items/all'

    headers = {'Content-Type': 'application/json'}

    response = requests.get(url, headers=headers)

    print(response.content)


def  update_todo_item(item, status):
    url = socket_address + '/item/update'

    headers = {'Content-Type': 'application/json'}

    data = json.dumps( {'item': item, 'status': status} )

    response = requests.put(url, headers=headers, data=data)

    print(response.content)


def  delete_todo_item(item):
    url = socket_address + '/item/delete'

    headers = {'Content-Type': 'application/json'}

    data = json.dumps( {'item': item} )

    response = requests.delete(url, headers=headers, data=data)

    print(response.content)



if __name__ == '__main__':
    main()