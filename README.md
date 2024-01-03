# DEVELOPMENT OF A SYSTEM TO EXTRACT VEHICLE PARAMETERS
_Author: **Nicolas Gonzalez Vallejo**_ <br />
Contact: ngonzaa27@gmail.com <br />

## Index
* [Project structure](https://github.com/ngonza27/BookAPI/#project-structure)
* [How to run](https://github.com/ngonza27/BookAPI/#how-to-run)


## Project structure
<br />
+---Backend<br />
▒   +---app.py<br />
+---Frontend<br />
    +---BookApp<br />
        +---e2e<br />
        +---src<br />
            +---app<br />
            ▒   +---book<br />
            ▒   +---others<br />
            +---assets<br />
            +---environments<br />


## Prerequisites
Install the following libraries:

For the Backend application:
```sh
$ cd Backend
# Install pipenv
$ pip install pipenv
# Enable the virtual environment
$ pipenv shell
# Install the application dependencies
$ pipenv install
```

For the Frontend application:
```sh
$ cd Frontend/BookApp
# If node is not installed, download it from the following link (https://nodejs.org/en/download)
# Install angular
$ npm install @angular/cli
# Install the application dependencies
$ npm install
```

## How to run

Note: Run the following commands in separate terminals for each application.
-  Start the Backend Application.
```sh
$ cd Backend
$ pipenv shell
# Create the db
$ python
$ >>> from app import db
$ >>> db.create_all()
$ >>> exit()
$ python app.py
```

-  Start the Frontend Application.
```sh
$ cd Frontend/BookApp
# Start the application
$ npm start
```
## Documentation

### Postman: 
https://documenter.getpostman.com/view/16129790/2s9YsFFEUu

### Swagger:
Note: once the backend is running the following link can be accessed by the browser.
http://localhost:5000/apidocs/
