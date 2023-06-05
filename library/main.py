# Requirements:
#   - allow for checkout of books
#   - allow return of books
#   - user management
#   - invoicing
# 
# Components:
# Library:
#   - will contain one or more copies of multiple books
#   - will have multiple racks (1 rack can contain at most one copy of a book)
# Book:
#   - book id, title, authors, publishers
# User:
#   - user id, name
#   - borrowed books (maximum of 5)
# UsersDB:
#   - all users in library system
#   - has data on all users (such as their borrowed books)
# BooksDB:
#   - would be a hashmap key: set(book_id, title, authors, publishers): Book()
# LibraryManagement:
#   - add book (to first available rack), remove book copy, allow user to borrow book copy, allow user to return book,
#   - allow user to print all books borrowed by them
#   - allow user to search for books gien properties
# 
# flow:
# create library managment system -> create library -> add book (with copies) to racks -> borrow book, search, remove, etc
class Book:
  def __init__(self, book_id, title, authors, publishers):
    self._book_id = book_id
    self._title = title
    self._authors = authors
    self._publishers = publishers

  def get_id(self):
    return self._book_id
  
  def get_title(self):
    return self._title

  def get_authors(self):
    return self._authors
  
  def get_publishers(self):
    return self._publishers

class BookCopy(Book):
  def __init__(self, book_id, title, authors, publishers, book_copy_id):
    super().__init__(book_id, title, authors, publishers)
    self._book_copy_id = book_copy_id
    self._borrower = None
    self._due_date = None
    self._rack = -1

  def get_book_copy_id(self):
    return self._book_copy_id

  def get_borrower(self):
    return self._borrower

  def add_borrower(self, user_id):
    self._borrower = user_id
    self._rack = -1

  def remove_borrower(self):
    self._borrower = None

  def get_due_date(self):
    return self._due_date

  def set_due_date(self, due_date):
    self._due_date = due_date

  def set_rack_book_is_on(self, rack):
    self._rack = rack
  
class User:
  def __init__(self, user_id, name):
    self._user_id = user_id
    self._name = name
    self._books_borrowed = set()

  def get_id(self):
    return self._user_id

  def get_name(self):
    return self._name

  def get_books_borrowed(self):
    return self._books_borrowed
  
  # before we borrow, make sure book_id exists
  def borrow_book(self, book_id, max_number_of_books):
    if len(self._books_borrowed) == max_number_of_books: 
      return False
    self._books_borrowed.add(book_id)
    return True

  def remove_book(self, book_id):
    self._books_borrowed.remove(book_id)

class UserDB:
  def __init__(self):
    self._users = {}
  
  def add_user(self, user):
    self._users[user.get_id()] = user

  def get_user(self, user_id):
    if user_id not in self._users:
      raise KeyError('Invalid user id')
    return self._users[user_id]

  def remove_user(self, user_id):
    del self._users[user_id]

  def get_db(self):
    return self._users

class BookDB:
  def __init__(self):
    self._books = {}

  def add_book(self, book):
    book_key = self._generate_book_key(book)
    if book_key not in self._books:
      self._books[book_key] = set()

  def add_copy_to_book(self, book, book_copy):
    book_key = self._generate_book_key(book)
    if book_key not in self._books:
      raise KeyError('Invalid book key')

    self._books[book_key].add(book_copy)

  def find_book(self, attribute_value):
    for book in self._books:
      if attribute_value in book:
        return self._books[book]

  def get_db(self):
    return self._books

  def _generate_book_key(self, book):
    title = book.get_title()
    authors = book.get_authors()
    book_id = book.get_id()
    publishers = book.get_publishers()
    return tuple(set(title, authors, book_id, publishers))

class Rack:
  def __init__(self, rack_number):
    self._rack = set()
    self._rack_number = rack_number

  def add_book_to_rack(self, book_id):
    self._rack.add(book_id)

  def remove_book_from_rack(self, book_id):
    self._rack.remove(book_id)

  def get_books_on_rack(self):
    return self._rack
  
  def get_rack_number(self):
    return self._rack_number

class Library:
  def __init__(self, racks):
    self._racks = racks

  def add_book_to_library(self, book_id):
    for rack in self._racks:
      if len(rack.get_books_on_rack()) == 0:
        rack.add_book_to_rack(book_id)
        return True
    return False

  def remove_book_from_library(self, book_id):
    for rack in self._racks:
      if book_id in rack.get_books_on_rack():
        rack.remove_book_from_rack(book_id)
        return True
    return False

class LibraryManager:
  def __init__(self, users_db, books_db):
    self._library = None
    self._users_db = users_db
    self._books_db = books_db

  def create_library(self, number_of_racks):
    racks = [Rack() for _ in range(number_of_racks)]
    self._library = Library(racks)
  
  def add_book_to_library(self):
    pass

  def create_book(self, book_id, title, authors, publishers):
    return Book(book_id, title, authors, publishers)

  def create_book_copies(self, book_id, title, authors, publishers, book_copy_id):
    return BookCopy(book_id, title, authors, publishers, book_copy_id)
  
  def search_book(self, attribute_value):
    return self._books_db.find_book(attribute_value)

  def get_user_borrowed_books(self, user_id):
    user = self._users_db.get_db()[user_id]
    return user.get_books_borrowed()

  
# usersDB = {user_id1: User(), user_id2: User(), user_id3: User(), ...}
# booksDb = {bookd_id1: [BookCopy1(), BookCopy2, BookCopy3], book_id2: [BookCopy4()]}
# Library() -> [Racks(), ...] 
# BookCopy() -> borrower, due date, rack #
"Testing"
user_db = UserDB()
book_db = BookDB()
library_manager = LibraryManager(user_db, book_db)
