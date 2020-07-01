# AirBnB clone - The console 
This  is the first step of the AirBnB project. A command interpreter is created in this step to manage objects for the website.

### Commands:
* Create: creates an object. `Usage: create <class name>`
* Destroy: delete an object. `Usage: destroy <class name> <id>`
* All: shows all objects, of one type or all types.`Usage: all`
* Update: Updates an instance based on the class name and id by adding or updating attribute. `Usage: update <class name> <id> <attribute name> "<attribute value>"`
* Show: shows an object (based on id). `Usage: show <class name> <id>`
* Quit/EOF: quits the console.`Usage: quit` or `EOF`
* Help: sees descriptions of commands.`Usage: help` or `help <command>`

### How to start the console
You need to clone this repo `git clone https://github.com/AndresCallejasG/AirBnB_clone.git` once the repository has been cloned, execute the console `./console.py`

### Example
How to execute:
```
$ ./console.py

(hbnb)help

Documented commands (type help <topic>):
=========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```
```
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb)
```

```
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
```
