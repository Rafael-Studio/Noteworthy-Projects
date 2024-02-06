# Virtual Library DOCUMENTATION
# This program is a simple library database using SQLite with the following features:
# 1 - List registered books;
# 2 - Add new books to the library;
# 3 - Search the library;
# 4 - Borrow and return books;
# 5 - Exclude items from the database.
# This program features an interactive menu for ease of use.

# Usage Instructions:
# Run the program and select your choices to manage, search, and modify the database.

# Features:
# - **List Registered Books:** View a list of all books currently registered in the library.
# - **Add New Books:** Register new books by providing title, author, and genre information.
# - **Search the Library:** Search for books by title, author, or genre, narrowing down your search criteria.
# - **Borrow and Return Books:** Manage the borrowing and returning process. The status of each book is updated in real-time.
# - **Exclude Items:** Remove items from the database when necessary.
#
# Database:
# The program utilizes SQLite for database management.
#
#  Note:
# - Follow the on-screen prompts for a seamless and user-friendly experience.

from time import sleep
import sqlite3


# Separator for better visual experience
def formatting():
    print("-=" * 50)


# Function to list every single book registered in the database
def list_books():
    print("List of Registered Books:")
    formatting()

    # Initialize database connection
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Fetch all books from the database in alphabetical order by title
    cursor.execute('SELECT * FROM books ORDER BY title')
    books = cursor.fetchall()

    if not books:
        print("No books registered in the library.")
    else:
        # Display information for each book
        for book in books:
            status = "Status: Available" if book[4] else "Status: Borrowed"
            print(f"Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, {status}")
            formatting()

    # Close the connection
    conn.close()


# Function to add new books to the database
def add_book():
    print("Add a New Book to the Library.")
    formatting()

    title = str(input("Enter the title of the book: ")).strip()
    author = str(input("Enter the author of the book: ")).strip()
    genre = str(input("Enter the genre of the book: ")).strip()
    available = True

    print("\nPlease review the entered information:")
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Genre: {genre}")

    confirm = input("\nIs the information correct? [Y/N]: ").strip().upper()[0]
    if confirm == "Y":

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        # Creating a table for storing books
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                genre TEXT,
                available INTEGER
            )
        ''')

        # Inserting the new book into the database
        cursor.execute('''
               INSERT INTO books (title, author, genre, available)
               VALUES (?, ?, ?, ?)
           ''', (title, author, genre, available))

        # Committing the changes and close the connection
        conn.commit()
        conn.close()

        print(f"\nBook '{title}' by {author} has been added to the library.")
    else:
        print("\nBook addition canceled. Please re-enter the information.")


# Function to search books in the library by Title, Author or Genre
def search_book():
    while True:
        print("Search the Library:")
        formatting()

        print("Choose a search criteria:\n"
              "[1] Search by Title.\n"
              "[2] Search by Author.\n"
              "[3] Search by Genre.\n"
              "[9] Return to Main Menu.")

        try:
            search_option = int(input("Enter the number corresponding to your choice: "))
        except (ValueError, TypeError):
            print("\033[31mInvalid input. Please enter a valid number.\033[m")
            continue

        if search_option not in [1, 2, 3, 9]:
            print("\033[31mInvalid choice. Please select a valid option.\033[m")
        elif search_option == 9:
            break
        else:
            search_term = input("Enter the search term: ").strip().lower()

            conn = sqlite3.connect('library.db')
            cursor = conn.cursor()

            if search_option == 1:
                print(f"Executing query for title: {search_term}")
                cursor.execute('SELECT * FROM books WHERE title LIKE ? COLLATE NOCASE ORDER BY title', (search_term,))
            elif search_option == 2:
                print(f"Executing query for author: {search_term}")
                cursor.execute('SELECT * FROM books WHERE author LIKE ? COLLATE NOCASE ORDER BY author', (search_term,))
            elif search_option == 3:
                print(f"Executing query for genre: {search_term}")
                cursor.execute('SELECT * FROM books WHERE genre LIKE ? COLLATE NOCASE ORDER BY genre', (search_term,))

            books = cursor.fetchall()

            if not books:
                print(f"\033[31mNo books found matching the search term: {search_term}\033[m")
            else:
                print("Search Results:")
                formatting()
                for book in books:
                    status = "Available" if book[4] else "Borrowed"
                    print(f"Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Status: {status}")
                    formatting()

            conn.close()


# function to borrow a book from the library
def borrow_book():
    title = input("Enter the EXACT title of the book you want to borrow: ").strip()

    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Check if the book is available
    cursor.execute('SELECT * FROM books WHERE title = ? COLLATE NOCASE AND available = 1', (title,))
    book_data = cursor.fetchone()

    if not book_data:
        print(f"Book with title '{title}' not found or not available for borrowing in the library.")
        formatting()
    else:
        # Update the database with the new availability status
        cursor.execute('UPDATE books SET available = 0 WHERE title = ? COLLATE NOCASE', (title,))
        conn.commit()
        print(f"{title} has been borrowed.")
        formatting()

    conn.close()


# function to return a previously borrowed book to the library
def return_book():
    title = input("Enter the EXACT title of the book you want to return: ").strip()

    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Check if the book is already available
    cursor.execute('SELECT * FROM books WHERE title = ? COLLATE NOCASE AND available = 0', (title,))
    book_data = cursor.fetchone()

    if not book_data:
        print(f"Book with title '{title}' is either not found or already available in the library.")
        formatting()
    else:
        # Update the database with the new availability status
        cursor.execute('UPDATE books SET available = 1 WHERE title = ? COLLATE NOCASE', (title,))
        conn.commit()
        print(f"Thank you for returning {title}.")
        formatting()

    conn.close()


def remove_book():
    title = input("Enter the EXACT title of the book you want to remove: ").strip()

    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Check if the book exists in the library
    cursor.execute('SELECT * FROM books WHERE title = ?', (title,))
    book_data = cursor.fetchone()

    if not book_data:
        print(f"\033[31mBook with title '{title}' not found in the library.\033[m")
        formatting()
    else:
        confirm = input("\nIs the information correct? [Y/N]: ").strip().upper()
        if confirm == "Y":
            # Remove the book from the database
            cursor.execute('DELETE FROM books WHERE title = ? COLLATE NOCASE', (title,))
            conn.commit()
            print(f"Book '{title}' has been removed from the library.")
            formatting()
        else:
            print("\nBook removal canceled.")

    conn.close()


# Interactive menu
def menu():
    while True:
        formatting()
        print("Main Menu")
        formatting()
        sleep(1)
        print("Options:")
        print("[1] List Registered Books.\n"
              "[2] Register a New Book.\n"
              "[3] Search the Library.\n"
              "[4] Borrow a Book.\n"
              "[5] Return a Book.\n"
              "[6] Remove a Book from the Library.\n"
              "[0] Exit the Program.")
        formatting()
        try:
            choice = int(input("Please type your choice: "))
        except KeyboardInterrupt:
            print("\033[31mInterruption detected. Please restart the program.\033[m")
            break
        except (ValueError, TypeError):
            print("\033[31mInvalid input. Please choose a valid option.\033[m")
        if choice not in range(0, 7):
            print("\033[31mInvalid input. Please choose a valid option.\033[m\n")
        if choice == 0:
            formatting()
            print("Program exited successfully.")
            break
        elif choice == 1:
            list_books()
        elif choice == 2:
            add_book()
        elif choice == 3:
            search_book()
        elif choice == 4:
            borrow_book()
        elif choice == 5:
            return_book()
        elif choice == 6:
            remove_book()


if __name__ == "__main__":
    formatting()
    greeting = "Welcome to the Library!"
    print(f"{greeting:^100}")
    menu()
