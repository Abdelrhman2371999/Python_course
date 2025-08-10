import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Book:
    def __init__(self, title, author, year, book_id, status="available"):
        self.title = title
        self.author = author
        self.year = year
        self.book_id = book_id
        self.status = status

    def display(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Status: {self.status}")
        print("--" * 10)

def create_book():
    clear_screen()
    print("Add a New Book")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = int(input("Enter year of publication: "))
    book_id = input("Enter book ID: ")
    status = input("Enter status (available/borrowed) or press Enter for default (available): ")
    if not status:
        status = "available"
    return Book(title, author, year, book_id, status)

def search_book(books):
    clear_screen()
    print("Search for a Book")
    print("1. Search by ID")
    print("2. Search by Title")
    print("3. Search by Status")
    choice = input("Enter your choice: ")
    found_books = []
    if choice == '1':
        book_id = input("Enter book ID to search: ")
        for b in books:
            if b.book_id == book_id:
                found_books.append(b)
                break
    elif choice == '2':
        title = input("Enter title to search: ")
        for b in books:
            if b.title.lower() == title.lower():
                found_books.append(b)
    elif choice == '3':
        status = input("Enter status to search: ")
        for b in books:
            if b.status.lower() == status.lower():
                found_books.append(b)
    else:
        print("Invalid choice!")
    if found_books:
        print("Found Books:")
        for book in found_books:
            book.display()
    else:
        print("No books found.")

# Main program loop    
Books = []

while True:
    clear_screen()
    print("=== Library Management System ===")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Exit")
    print("4. Search Book")
    choice = input("Enter your choice: ")

    if choice == '1':
        book = create_book()
        Books.append(book)
        print("Book added successfully!")
        time.sleep(2)
    elif choice == '2':
        clear_screen()
        if not Books:
            print("No books in the library yet.")
        else:
            for b in Books:
                b.display()
        input("Press Enter to continue...")
    elif choice == '3':
        print("Exiting the program...")
        break
    elif choice == '4':
        search_book(Books)
        input("Press Enter to continue...")
    else:
        print("Invalid choice! Please try again.")
        time.sleep(2)
