class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
        self.issued_to = ""

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", "Available" if self.available else "Issued")
        if not self.available:
            print("Issued to:", self.issued_to)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = input("Enter Book ID: ")

        for book in self.books:
            if book.book_id == book_id:
                print("Book ID already exists!")
                return

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        if not title.strip() or not author.strip():
            print("Title and author cannot be empty!")
            return

        book = Book(book_id, title, author)
        self.books.append(book)
        print("Book added successfully!")

    def view_books(self):
        if len(self.books) == 0:
            print("No books available!")
            return

        for book in self.books:
            book.display()
            print("----------------------")

    def search_book(self):
        keyword = input("Enter Book ID or Title: ").lower()
        found = False

        for book in self.books:
            if book.book_id.lower() == keyword or keyword in book.title.lower():
                book.display()
                found = True

        if not found:
            print("Book not found!")

    def issue_book(self):
        book_id = input("Enter Book ID to issue: ")

        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    student = input("Enter Student Name: ")

                    if not student.strip():
                        print("Student name cannot be empty!")
                        return

                    book.available = False
                    book.issued_to = student
                    print("Book issued successfully!")
                else:
                    print("Book is already issued!")
                return

        print("Book not found!")

    def return_book(self):
        book_id = input("Enter Book ID to return: ")

        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    book.issued_to = ""
                    print("Book returned successfully!")
                else:
                    print("This book is already available!")
                return

        print("Book not found!")

    def view_issued_books(self):
        found = False

        for book in self.books:
            if not book.available:
                book.display()
                print("----------------------")
                found = True

        if not found:
            print("No books are currently issued!")

    def remove_book(self):
        book_id = input("Enter Book ID to remove: ")

        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    self.books.remove(book)
                    print("Book removed successfully!")
                else:
                    print("Return the book before removing it!")
                return

        print("Book not found!")


library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. View Issued Books")
    print("7. Remove Book")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.view_books()
    elif choice == "3":
        library.search_book()
    elif choice == "4":
        library.issue_book()
    elif choice == "5":
        library.return_book()
    elif choice == "6":
        library.view_issued_books()
    elif choice == "7":
        library.remove_book()
    elif choice == "8":
        print("Thank you for visiting the library!")
        break
    else:
        print("Invalid choice! Please try again.")