import pdb
# import models
from models.book import Book
from models.author import Author
# import repositories
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Brian", 'Limond')
author_repository.save(author1)
author2 = Author("J. R. R.", 'Tolkien')
author_repository.save(author2)

author_repository.select_all()

book1 = Book("Daft Wee Stories", author1, "Humour", 17808937)
book_repository.save(book1)
book2 = Book("That's Your Lot", author1, "Humour", 10081726)
book_repository.save(book2)

book3 = Book("The Silmarillion", author2, "Fantasy", 23983948)
book_repository.save(book3)
book4 = Book("The Hobbit", author2, "Fantasy", 98734982)
book_repository.save(book4)

























pdb.set_trace()
