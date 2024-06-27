class Book:
    def __init__(self, title, author, isbn, publication_date, genre):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__publication_date = publication_date
        self.__availability = True
        self.__genre = genre

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    @property
    def publication_date(self):
        return self.__publication_date

    @property
    def availability(self):
        return self.__availability

    @availability.setter
    def availability(self, status):
        self.__availability = status

    @property
    def genre(self):
        return self.__genre

    def display_details(self):
        status = "Available" if self.__availability else "Borrowed"
        return f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__isbn}, " \
               f"Publication Date: {self.__publication_date}, Status: {status}, Genre: {self.__genre.name}"

    def __repr__(self):
        return f"Book('{self.__title}', '{self.__author}', '{self.__isbn}', '{self.__publication_date}', '{self.__genre}', {self.__availability})"
