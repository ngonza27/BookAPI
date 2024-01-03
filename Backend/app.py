import os
import uuid
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')

db = SQLAlchemy(app)
ma = Marshmallow(app)
app.app_context().push()


class BookModel(db.Model):
  id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4().hex))
  title = db.Column(db.String(100))
  author = db.Column(db.String(255))
  read = db.Column(db.Boolean)

  def __init__(self, title, author, read):
    self.title = title
    self.author = author
    self.read  = read
    

class Schema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = BookModel

book_schema = Schema()
books_schema = Schema(many=True)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

@app.route('/')
def hello_world():
  """
    Home endpoint
    ---
    responses:
      200:
        description: Returns a welcome message
  """
  return 'API running'

@app.route('/book/')
def book_list():
  """
    Retrieve the list of books
    ---
    responses:
      200:
        description: Returns the list of books
        schema:
          type: array
          items:
            $ref: '#/definitions/BookModel'
  """
  all_books = BookModel.query.all()
  return jsonify(books_schema.dump(all_books))


@app.route('/book', methods=['POST'])
def create_book():
  """
    Create a new book
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/BookModel'
    responses:
      200:
        description: Returns the created book
        schema:
          $ref: '#/definitions/BookModel'
  """
  title = request.json.get('title', '')
  author = request.json.get('author', '')
  read = request.json.get('read', False)

  book = BookModel(title=title, author=author, read=read)
  
  db.session.add(book)
  db.session.commit()
  
  return book_schema.jsonify(book)


@app.route('/book/<book_id>', methods=["GET"])
def book_detail(book_id):
  """
    Retrieve details of a specific book
    ---
    parameters:
      - name: book_id
        in: path
        type: string
        required: true
        description: ID of the book to retrieve
    responses:
      200:
        description: Returns details of the specified book
        schema:
          $ref: '#/definitions/BookModel'
  """
  book = BookModel.query.get(book_id)
  return book_schema.jsonify(book)


@app.route('/book/<book_id>', methods=['PUT'])
def update_book(book_id):
  """
    Update details of a specific book
    ---
    parameters:
      - name: book_id
        in: path
        type: string
        required: true
        description: ID of the book to update
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/BookModel'
    responses:
      200:
        description: Returns the updated book
        schema:
          $ref: '#/definitions/BookModel'
  """
  title = request.json.get('title', '')
  author = request.json.get('author', '')
  read = request.json.get('read', False)

  book = BookModel.query.get(book_id)
  
  book.title = title
  book.author = author
  book.read = read

  db.session.add(book)
  db.session.commit()

  return book_schema.jsonify(book)


@app.route('/book/<book_id>', methods=["DELETE"])
def delete_book(book_id):
  """
    Delete a specific book
    ---
    parameters:
      - name: book_id
        in: path
        type: string
        required: true
        description: ID of the book to delete
    responses:
      200:
        description: Returns details of the deleted book
        schema:
          $ref: '#/definitions/BookModel'
  """

  book = BookModel.query.get(book_id)
  
  db.session.delete(book)
  db.session.commit()

  return book_schema.jsonify(book)


# Swagger definitions
app.config['SWAGGER'] = {
    'title': 'Flask CRUD API',
    'uiversion': 3,
}

if __name__ == '__main__':
  app.run(debug=True)
