# coder:MELIKE SULTAN BOZOGLAN
# date: 16.02.2024
# Global AI Hub-Python Bootcamp

# import part
import sys

# create class
class Library:

    def __init__(self):

        try:
            self.file = open("books.txt", "a+")

        except FileNotFoundError:
            print("File not found")
            sys.exit()

    def __del__(self):

        self.file.close()

    def list_book(self):

        self.file.seek(0)
        books = self.file.readlines()

        for book in books:
            b = book.strip().split(", ") 
            if len(b) >= 2:  
                print(f"Book: {b[0]}, Author: {b[1]}")
            else:
                print("Invalid book information:", book.strip())
         
    def add_book(self):
        title = input("please enter title of book: ")
        author = input("please enter author of book: ")
        release_year = input("please enter release year of book: ")
        number_of_pages = input("please enter number of pages of book: ")
        
        self.file.write(f"{title}, {author}, {release_year}, {number_of_pages}\n")
        print("book added successfully")

    def remove_book(self):
        title_to_remove = input("Please enter the title of the book you want to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = []
        removed = False

        for book in books:
            book_info = book.strip().split(", ")
            if book_info[0] == title_to_remove:
                removed = True
            else:
                updated_books.append(book)

        if removed:
            self.file.seek(0)
            self.file.truncate() 
            self.file.writelines(updated_books)
            print(f"{title_to_remove} has been removed from the library.")
        else:
            print(f"{title_to_remove} is not found in the library.")
        
# create object
lib = Library()
        
# menu
print("""
    MENU
1) List Books
2) Add Books
3) Remove Book
!please enter between 1-3!
--> press q for exit
""")


while(True):
    select = input("please enter your select: ")

    if(select == "1" or select == 1):
        lib.list_book()

    elif(select == "2" or select == 2):
        lib.add_book()

    elif(select == "3" or select == 3):
        lib.remove_book()

    elif(select.lower() == "q"):
        sys.exit()

    else:
        print("Invalid! Please enter a number between 1 and 3 or 'q' to exit.")


