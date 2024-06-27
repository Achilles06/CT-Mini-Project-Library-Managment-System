from book import Book
from user import User
from author import Author
from genre import Genre
from data_handler import DataHandler

class Menu:
    def __init__(self):
        self.books = DataHandler.load_data('books.txt')
        self.users = DataHandler.load_data('users.txt')
        self.authors = DataHandler.load_data('authors.txt')
        self.genres = DataHandler.load_data('genres.txt')

    def main_menu(self):
        while True:
            print("\nWelcome to the Library Management System!")
            print("Main Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Genre Operations")
            print("5. Quit")
            choice = input("Select an option: ")

            if choice == '1':
                self.book_operations()
            elif choice == '2':
                self.user_operations()
            elif choice == '3':
                self.author_operations()
            elif choice == '4':
                self.genre_operations()
            elif choice == '5':
                self.quit_system()
            else:
                print("Invalid option. Please try again.")

    def book_operations(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")
            choice = input("Select an option: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.borrow_book()
            elif choice == '3':
                self.return_book()
            elif choice == '4':
                self.search_book()
            elif choice == '5':
                self.display_all_books()
            elif choice == '6':
                break
            else:
                print("Invalid option. Please try again.")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        isbn = input("Enter ISBN: ")
        publication_date = input("Enter publication date (YYYY-MM-DD): ")
        genre_name = input("Enter genre name: ")
        genre = self.genres.get(genre_name)
        if not genre:
            description = input("Enter genre description: ")
            category = input("Enter genre category: ")
            genre = Genre(genre_name, description, category)
            self.genres[genre_name] = genre
        book = Book(title, author, isbn, publication_date, genre)
        self.books[isbn] = book
        print(f"Book '{title}' added successfully.")

    def borrow_book(self):
        user_id = input("Enter user library ID: ")
        isbn = input("Enter ISBN of the book to borrow: ")
        user = self.users.get(user_id)
        book = self.books.get(isbn)
        if user and book:
            message = user.borrow_book(book)
            print(message)
        else:
            print("Invalid user ID or ISBN.")

    def return_book(self):
        user_id = input("Enter user library ID: ")
        isbn = input("Enter ISBN of the book to return: ")
        user = self.users.get(user_id)
        book = self.books.get(isbn)
        if user and book:
            message = user.return_book(book)
            print(message)
        else:
            print("Invalid user ID or ISBN.")

    def search_book(self):
        isbn = input("Enter ISBN of the book to search: ")
        book = self.books.get(isbn)
        if book:
            print(book.display_details())
        else:
            print("Book not found.")

    def display_all_books(self):
        if self.books:
            for book in self.books.values():
                print(book.display_details())
        else:
            print("No books available.")

    def user_operations(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")
            choice = input("Select an option: ")

            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.view_user_details()
            elif choice == '3':
                self.display_all_users()
            elif choice == '4':
                break
            else:
                print("Invalid option. Please try again.")

    def add_user(self):
        name = input("Enter user name: ")
        library_id = input("Enter library ID: ")
        user = User(name, library_id)
        self.users[library_id] = user
        print(f"User '{name}' added successfully.")

    def view_user_details(self):
        library_id = input("Enter user library ID: ")
        user = self.users.get(library_id)
        if user:
            print(user.display_details())
        else:
            print("User not found.")

    def display_all_users(self):
        if self.users:
            for user in self.users.values():
                print(user.display_details())
        else:
            print("No users available.")

    def author_operations(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to Main Menu")
            choice = input("Select an option: ")

            if choice == '1':
                self.add_author()
            elif choice == '2':
                self.view_author_details()
            elif choice == '3':
                self.display_all_authors()
            elif choice == '4':
                break
            else:
                print("Invalid option. Please try again.")

    def add_author(self):
        name = input("Enter author name: ")
        biography = input("Enter biography: ")
        author = Author(name, biography)
        self.authors[name] = author
        print(f"Author '{name}' added successfully.")

    def view_author_details(self):
        name = input("Enter author name: ")
        author = self.authors.get(name)
        if author:
            print(author.display_details())
        else:
            print("Author not found.")

    def display_all_authors(self):
        if self.authors:
            for author in self.authors.values():
                print(author.display_details())
        else:
            print("No authors available.")

    def genre_operations(self):
        while True:
            print("\nGenre Operations:")
            print("1. Add a new genre")
            print("2. View genre details")
            print("3. Display all genres")
            print("4. Back to Main Menu")
            choice = input("Select an option: ")

            if choice == '1':
                self.add_genre()
            elif choice == '2':
                self.view_genre_details()
            elif choice == '3':
                self.display_all_genres()
            elif choice == '4':
                break
            else:
                print("Invalid option. Please try again.")

    def add_genre(self):
        name = input("Enter genre name: ")
        description = input("Enter description: ")
        category = input("Enter category: ")
        genre = Genre(name, description, category)
        self.genres[name] = genre
        print(f"Genre '{name}' added successfully.")

    def view_genre_details(self):
        name = input("Enter genre name: ")
        genre = self.genres.get(name)
        if genre:
            print(genre.get_category_details())
        else:
            print("Genre not found.")

    def display_all_genres(self):
        if self.genres:
            for genre in self.genres.values():
                print(genre.get_category_details())
        else:
            print("No genres available.")

    def quit_system(self):
        # Save data before quitting
        DataHandler.save_data('books.txt', self.books)
        DataHandler.save_data('users.txt', self.users)
        DataHandler.save_data('authors.txt', self.authors)
        DataHandler.save_data('genres.txt', self.genres)
        print("Library data saved. Exiting the system.")
        exit()

