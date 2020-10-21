# Library - recruitment app
This is a recruitment task with the aim to create a webapp used for managing a collection of books and importing data from Google Books API

The project is available at https://mjanusz-library.herokuapp.com/

## Technologies
* Python 3.8.6
* Django 3.1.2
* Bootstrap 4
* jQuery 3.5.1

## Setup
To run this project you have to have Python 3.8.6 installed locally, create aa virtual environment and run command

```pip install -r requirements.txt```

After the required packages are installed use commands

```
python manage.py migrate
python manage.py runserver
``` 

The development server should start and the app should be accessible at [localhost:8000]

## URLs

Main page - list of books: '/'

Book adding form: 'book/add/'

Book editing form: 'book/edit/<book_id>/'

Book deletion page: 'book/delete/<book_id>/'

REST API view of all books: 'book/api/'

Google Books API import page: 'import/'