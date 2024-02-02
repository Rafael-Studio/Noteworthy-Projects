# Virtual Library DOCUMENTATION
# books are registered into the database by user input (title, author, genre)
# This program is a simple library database using sqlite with the following features:
# 1 - listing registered books;
# 2 - adding new books to the library;
# 3 - searching the library;
# 4 - borrowing and returning books;
# 5 - excluding items from the database
# This program has an interactive menu for easy of use
# Run this program and select your choices to manage, search and modify the database

from time import sleep
import sqlite3


# Initializing the book class
class Book:
    def __init__(self, title, author, genre, available=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True


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

    # Fetch all books from the database
    cursor.execute('SELECT * FROM books')
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


def borrow_book():
    title = input("Enter the EXACT title of the book you want to borrow: ").strip()

    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Check if the book is available
    cursor.execute('SELECT * FROM books WHERE title = ? AND available = 1', (title,))
    book_data = cursor.fetchone()

    if not book_data:
        print(f"Book with title '{title}' not found or not available for borrowing in the library.")
        formatting()
    else:
        # Update the database with the new availability status
        cursor.execute('UPDATE books SET available = 0 WHERE title = ?', (title,))
        conn.commit()
        print(f"{title} has been borrowed.")
        formatting()

    conn.close()

def return_book():
    title = input("Enter the EXACT title of the book you want to return: ").strip()

    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Check if the book is already available
    cursor.execute('SELECT * FROM books WHERE title = ? AND available = 0', (title,))
    book_data = cursor.fetchone()

    if not book_data:
        print(f"Book with title '{title}' is either not found or already available in the library.")
        formatting()
    else:
        # Update the database with the new availability status
        cursor.execute('UPDATE books SET available = 1 WHERE title = ?', (title,))
        conn.commit()
        print(f"Thank you for returning {title}.")
        formatting()

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
              "[6] Exclude a Book from the Library.\n"
              "[0] Close the Program.")
        formatting()
        try:
            choice = int(input("Please, type your choice: "))
        except KeyboardInterrupt:
            print("\033[31mInterruption detected. Please restart the program.\033[m")
            break
        except (ValueError, TypeError):
            print("\033[31mInvalid input. Please choose a valid option.\033[m")
        if choice not in range(0, 6):
            print("\033[31mInvalid input. Please choose a valid option.\033[m\n")
        if choice == 0:
            formatting()
            print("Program closed successfully.")
            break
        elif choice == 1:
            list_books()
        elif choice == 2:
            add_book()
        elif choice == 4:
            borrow_book()
        elif choice == 5:
            return_book()


if __name__ == "__main__":
    menu()
