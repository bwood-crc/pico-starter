import flask
# Coding an API

import mysql.connector
# CRUD interactions with the database.0

from flask import request, jsonify
# Request = details of the request received.

app = flask.Flask(__name__)
# app = The rest server itself.

@app.route('/api/v1/books', methods=['GET'])
def get_all_books():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
    password = "Canada123",
    database = "bookstore",
    )
    # MyDB = Connection to the DB

    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM book")
    my_result = my_cursor.fetchall()

    return my_result

    #for x in my_result:
    #    print(x)

@app.route('/api/v0/books/<isbn>', methods=['GET'])
def get_book(isbn):
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
    password = "Canada123",
    database = "bookstore",
    )
    # MyDB = Connection to the DB

    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT * FROM book where isbn = " + isbn)
    my_result = my_cursor.fetchall()

    return my_result

    #for x in my_result:
    #    print(x)


@app.route('/api/v1/books', methods=['POST'])
def create_book():

    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
    password = "Canada123",
    database = "bookstore",
    )

    # handle the POST request

    isbn = request.form.get("isbn")
    title = request.form.get("title")
    author = request.form.get("author")

    # insert record into the DB

    my_cursor = mydb.cursor()

    new_book_sql = ("INSERT INTO book (isbn,title, author) values (%s, %s, %s)")

    new_book_data = (isbn, title, author)

    my_cursor.execute(new_book_sql, new_book_data)

    # id_num = cursor.lastrowid
    # Get the last inserted ID (if applicable)
    mydb.commit()  # Must be called to commit changes
    return "Success"

    # response = make_response("<h1>Success</h1>")
    # response.status_code = 200
    # return response

app.run()
