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

import sqlite3
from time import sleep

COLOR_MSG = {
    "info": "{msg}",
    "debug": "{msg}",
    "warning": "{msg}",
    "error": "\033[31m{msg}\033[m",  # red
    "critical": "\033[31m{msg}\033[m",  # red
}


def log(level, msg):
    print(COLOR_MSG[level].format(msg=msg))


# Separator for better visual experience
def formatting():
    print("-=" * 50)


# Function to list every single book registered in the database
def list_books():
    print("List of Registered Books:")
    formatting()

    # Initialize database connection
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Fetch all books from the database in alphabetical order by title
    cursor.execute("SELECT * FROM books ORDER BY title")
    books = cursor.fetchall()

    if not books:
        log("info", "No books registered in the library.")
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

    title = input("Enter the title of the book: ").strip()
    author = input("Enter the author of the book: ").strip()
    genre = input("Enter the genre of the book: ").strip()
    available = True

    print("\nPlease review the entered information:")
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Genre: {genre}")

    confirm = input("\nIs the information correct? [Y/n]: ").strip().upper()
    while confirm not in "YN":
        confirm = input("Invalid input. Please confirm if the entered information is correct [Y/n]: ").strip().upper()
    if confirm == "Y":

        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()

        # Creating a table for storing books
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                genre TEXT,
                available INTEGER
            )
        """
        )

        # Inserting the new book into the database
        cursor.execute(
            """
            INSERT INTO books (title, author, genre, available)
            VALUES (?, ?, ?, ?)
        """,
            (title, author, genre, available),
        )

        # Committing the changes and close the connection
        conn.commit()
        conn.close()

        log("info", f"\nBook '{title}' by {author} has been added to the library.")

    if confirm == "N":
        log("info", "\nBook addition canceled. Please re-enter the information.")


# Function to search books in the library by Title, Author or Genre
def search_book():
    while True:
        print("Search the Library:")
        formatting()

        print(
            "Choose a search criteria:\n"
            "[1] Search by Title.\n"
            "[2] Search by Author.\n"
            "[3] Search by Genre.\n"
            "[9] Return to Main Menu."
        )

        try:
            search_option = int(
                input("Enter the number corresponding to your choice: ")
            )
        except (ValueError, TypeError):
            log("error", "Invalid input. Please enter a valid number.")
            continue

        if search_option not in [1, 2, 3, 9]:
            log("error", "Invalid choice. Please select a valid option.")
        elif search_option == 9:
            break
        else:
            search_term = input("Enter the search term: ").strip().lower()

            conn = sqlite3.connect("library.db")
            cursor = conn.cursor()

            if search_option == 1:
                log("debug", f"Executing query for title: {search_term}")
                cursor.execute(
                    "SELECT * FROM books WHERE title LIKE ? COLLATE NOCASE ORDER BY title",
                    (search_term,),
                )
            elif search_option == 2:
                log("debug", f"Executing query for author: {search_term}")
                cursor.execute(
                    "SELECT * FROM books WHERE author LIKE ? COLLATE NOCASE ORDER BY author",
                    (search_term,),
                )
            elif search_option == 3:
                log("debug", f"Executing query for genre: {search_term}")
                cursor.execute(
                    "SELECT * FROM books WHERE genre LIKE ? COLLATE NOCASE ORDER BY genre",
                    (search_term,),
                )

            books = cursor.fetchall()

            if not books:
                log("error", f"No books found matching the search term: {search_term}")
                sleep(1)
            else:
                print("Search Results:")
                formatting()
                for book in books:
                    status = "Available" if book[4] else "Borrowed"
                    print(
                        f"Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Status: {status}"
                    )
                    formatting()
                sleep(1)

            conn.close()


# function to borrow a book from the library
def borrow_book():
    title = input("Enter the EXACT title of the book you want to borrow: ").strip()

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Check if the book is available
    cursor.execute(
        "SELECT * FROM books WHERE title = ? COLLATE NOCASE AND available = 1", (title,)
    )
    book_data = cursor.fetchone()

    if not book_data:
        print(
            f"Book with title '{title}' not found or not available for borrowing in the library."
        )
        formatting()
    else:
        # Update the database with the new availability status
        cursor.execute(
            "UPDATE books SET available = 0 WHERE title = ? COLLATE NOCASE", (title,)
        )
        conn.commit()
        log("info", f"{title} has been borrowed.")
        formatting()

    conn.close()


# function to return a previously borrowed book to the library
def return_book():
    title = input("Enter the EXACT title of the book you want to return: ").strip()

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Check if the book is already available
    cursor.execute(
        "SELECT * FROM books WHERE title = ? COLLATE NOCASE AND available = 0", (title,)
    )
    book_data = cursor.fetchone()

    if not book_data:
        log(
            "info",
            f"Book with title '{title}' is either not found or already available in the library.",
        )
        formatting()
    else:
        # Update the database with the new availability status
        cursor.execute(
            "UPDATE books SET available = 1 WHERE title = ? COLLATE NOCASE", (title,)
        )
        conn.commit()
        print(f"Thank you for returning {title}.")
        formatting()

    conn.close()


def remove_book():
    title = input("Enter the EXACT title of the book you want to remove: ").strip()

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Check if the book exists in the library
    cursor.execute("SELECT * FROM books WHERE title = ?", (title,))
    book_data = cursor.fetchone()

    if not book_data:
        log("error", f"Book with title '{title}' not found in the library.")
        formatting()
    else:
        confirm = input("\nIs the information correct? [Y/N]: ").strip().upper()
        while confirm not in "YN":
            confirm = input(
                "Invalid input. Please confirm if the entered information is correct [Y/n]: ").strip().upper()
        if confirm == "Y":
            # Remove the book from the database
            cursor.execute("DELETE FROM books WHERE title = ? COLLATE NOCASE", (title,))
            conn.commit()
            log("info", f"\nBook '{title}' has been removed from the library.")
            formatting()
        if confirm == "N":
            print("\nBook removal canceled.")

    conn.close()


def has_books_table():
    with sqlite3.connect("library.db") as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM books")
            return True
        except sqlite3.OperationalError:
            print("No books detected.")
            return False


# Interactive menu
def menu():
    while True:
        formatting()
        print("Main Menu")
        formatting()
        sleep(1)

        if not has_books_table():
            # If table doesn't exist there is no other option other than add books
            choice = 2
        else:
            print("Options:")
            print(
                "[1] List Registered Books.\n"
                "[2] Register a New Book.\n"
                "[3] Search the Library.\n"
                "[4] Borrow a Book.\n"
                "[5] Return a Book.\n"
                "[6] Remove a Book from the Library.\n"
                "[0] Exit the Program."
            )
            formatting()
            invalid_choice = True
            choice = 0

            while invalid_choice:
                try:
                    choice = int(input("Please type your choice: "))
                    if choice in range(0, 7):
                        invalid_choice = False
                    else:
                        log("error", "Invalid input. Please choose a valid option.\n")
                except KeyboardInterrupt:
                    log("info", "\nInterruption detected. Please restart the program.")
                    exit(0)
                except (ValueError, TypeError):
                    log("error", "Invalid input. Please choose a valid option.")

        try:
            match choice:
                case 0:
                    formatting()
                    print("Program exited successfully.")
                    exit(0)
                case 1:
                    list_books()
                case 2:
                    add_book()
                case 3:
                    search_book()
                case 4:
                    borrow_book()
                case 5:
                    return_book()
                case 6:
                    remove_book()
                case _:
                    log("error", "Unexpected error")
        except sqlite3.DatabaseError as err:
            log("critical", f"Database error: {err}")


if __name__ == "__main__":
    formatting()
    greeting = "Welcome to the Library!"
    print(f"{greeting:^100}")
    menu()
