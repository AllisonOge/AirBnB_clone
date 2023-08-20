# AirBnB_clone
AirBnB clone built using the Python language and Flask framework as part of the ALX projects

## Project design stages
1. The console project (completed-7 days sprint)
2. Web static (active-2 days sprint)

### 1. The Console Project
Deals with serialization/deserialization of Python Object to JSON. The requirements of this module are:
- Data model
- CRUD operation
- Persist to JSON file

#### Quick Start
Run the `console.py` file to use the console terminal and try some CRUD operations, observe the impact on the `file.json` file in the root directory.
> Examples
```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help all
Prints all string representation of all instances based or not on the class name

Usage: all <class name> or all

data models are: BaseModel, User, State, City, Amenity, Place, Review
(hbnb) all
[]
(hbnb) help create
Create a new instance of data models, save it (to the JSON file) and print the id

Usage: create <class name>

data models are: BaseModel, User, State, City, Amenity, Place, Review
(hbnb) create User
60b0bba8-e9af-4da0-83e3-ab0e479a5285
(hbnb) all
["[User] (60b0bba8-e9af-4da0-83e3-ab0e479a5285) {'id': '60b0bba8-e9af-4da0-83e3-ab0e479a5285', 'created_at': datetime.datetime(2023, 8, 20, 9, 12, 59, 700603), 'updated_at': datetime.datetime(2023, 8, 20, 9, 12, 59, 700623)}"]
(hbnb) help update
Updates data model based on the class name and id by adding or updating attribute

Usage: update <class name> <id> <attribute name> 

data models are: BaseModel, User, State, City, Amenity, Place, Review
(hbnb) update User 60b0bba8-e9af-4da0-83e3-ab0e479a5285 name Betty
(hbnb) all User
["[User] (60b0bba8-e9af-4da0-83e3-ab0e479a5285) {'id': '60b0bba8-e9af-4da0-83e3-ab0e479a5285', 'created_at': datetime.datetime(2023, 8, 20, 9, 12, 59, 700603), 'updated_at': datetime.datetime(2023, 8, 20, 9, 12, 59, 700623), 'name': 'Betty'}"]
(hbnb) quit
```
#### Data model
![Alt text](datamodel.jpg)

The figure shows the different models needed for the project which are:
- User: the logged-in user of the application
- Review: User's review of the place
- Place: Location to be leased
- City: City where the Place is located
- State: State where the Place is located
- PlaceAmenity: junction or intermediary table to resolve many2many relationships between Place and Amenity
- Amenity: Amenity of a Place (there are many amenities in a place and one amenity to several places)

#### Design Architecture
Uses an OOP class with a class attribute for a couple of reasons:
- easy class identification
- provision of default values
- same behaviour for file storage and database storage


## File structure
- `models` - holds all data models
- `models/engine` - holds all storage classes using the same prototype
- `console.py` - entry file for the console project
- `models/base_model.py` - base model class for all data models
- `tests` - holds all test cases
