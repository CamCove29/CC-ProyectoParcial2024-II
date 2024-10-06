from flask import Flask, request, jsonify, render_template
import json
import sqlite3

app = Flask(__name__)


# Conexión a la base de datos
def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('books.sqlite')  # Cambiado a 'books.sqlite'
    except sqlite3.error as e:
        print(e)
    return conn

@app.route("/books", methods=["GET", "POST"])
def books():
    # Acceder a la conexión de la base de datos
    conn = db_connection()
    cursor = conn.cursor()

    # Creando nuestra solicitud GET para todos los libros
    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM books")  # Cambiado a 'books'
        books = [
            dict(id=row[0], title=row[1], author=row[2], genre=row[3], year=row[4])  # Cambiado a campos de libros
            for row in cursor.fetchall()
        ]

        if books is not None:
            return jsonify(books)

    # Creando nuestra solicitud POST para un libro
    if request.method == "POST":
        title = request.form["title"]  # Cambiado a 'title'
        author = request.form["author"]  # Cambiado a 'author'
        genre = request.form["genre"]  # Cambiado a 'genre'
        year = request.form["year"]  # Cambiado a 'year'

        # Consulta SQL para INSERTAR un libro en nuestra base de datos
        sql = """INSERT INTO books (title, author, genre, year)
                 VALUES (?, ?, ?, ?)"""

        cursor = cursor.execute(sql, (title, author, genre, year))
        conn.commit()
        return f"Book with id: {cursor.lastrowid} created successfully"


# Ruta con todos los métodos de solicitud necesarios para un solo libro
@app.route('/book/<int:id>', methods=["GET", "PUT", "DELETE"])
def book(id):
    conn = db_connection()
    cursor = conn.cursor()
    book = None

    # Creando nuestra solicitud GET para un libro
    if request.method == "GET":
        cursor.execute("SELECT * FROM books WHERE id=?", (id,))
        rows = cursor.fetchall()
        for row in rows:
            book = row
        if book is not None:
            return jsonify(book), 200
        else:
            return "Something went wrong", 404

    # Creando nuestra solicitud PUT para un libro
    if request.method == "PUT":
        sql = """UPDATE books SET title=?, author=?, genre=?, year=?
                 WHERE id=?"""

        title = request.form["title"]
        author = request.form["author"]
        genre = request.form["genre"]
        year = request.form["year"]

        updated_book = {
            "id": id,
            "title": title,
            "author": author,
            "genre": genre,
            "year": year
        }

        conn.execute(sql, (title, author, genre, year, id))
        conn.commit()
        return jsonify(updated_book)

    # Creando nuestra solicitud DELETE para un libro
    if request.method == "DELETE":
        sql = """DELETE FROM books WHERE id=?"""
        conn.execute(sql, (id,))
        conn.commit()

        return "The book with id: {} has been deleted.".format(id), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)

