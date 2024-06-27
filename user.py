class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    @property
    def name(self):
        return self.__name

    @property
    def library_id(self):
        return self.__library_id

    @property
    def borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book):
        if book.availability:
            book.availability = False
            self.__borrowed_books.append(book)
            return f"{book.title} borrowed successfully."
        return f"{book.title} is currently unavailable."

    def return_book(self, book):
        if book in self.__borrowed_books:
            book.availability = True
            self.__borrowed_books.remove(book)
            return f"{book.title} returned successfully."
        return f"{book.title} not found in borrowed books."

    def display_details(self):
        borrowed_titles = [book.title for book in self.__borrowed_books]
        return f"Name: {self.__name}, Library ID: {self.__library_id}, " \
               f"Borrowed Books: {', '.join(borrowed_titles) if borrowed_titles else 'None'}"

    def __repr__(self):
        return f"User('{self.__name}', '{self.__library_id}', {self.__borrowed_books})"
