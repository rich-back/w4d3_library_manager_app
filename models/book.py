class Book:

    def __init__(self, title, author, genre, isbn_number, id=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn_number = isbn_number
        self.id = id