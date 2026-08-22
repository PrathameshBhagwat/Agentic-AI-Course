# 11. Library Management — Aggregation + Encapsulation
# Create:
# Book
# Library
# • Book should contain title, author, and price.
# • Make price private.
# • Create getter/setter for price.
# • Library should contain multiple Book objects.
# • Add books to the library.
# • Display all books.
# • Search for a book by title. 

class Book:
    def __init__(self,id,title, author):
        self.id = id 
        self.title = title
        self.author = author
        self.__price = 0
    
    def get_price(self):
        return self.__price
    
    def set_price(self,amount):
        self.__price = amount
    

class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self,book):
        self.books.append(book)
        
    def display_books(self):
        if len(self.books) == 0:
            print("Library is empty.")
            return 
        
        for i in self.books:
            print("Book ID : ",i.id)
            print("Book Title is : ",i.title)
            print("Author name : ",i.author)
            print("Price : ",i.get_price())
        
    def search_book(self,title):
        for i in self.books:
            if i.title.lower() == title.lower():
                print("Book ID : ",i.id)
                print("Book Title is : ",i.title)
                print("Author name : ",i.author)
                print("Price : ",i.get_price())
                
                return
            
        print("Book not found")
                

    
library = Library()
  
def add_book():
    book_id = int(input("Enter Book ID : "))
    title = input("Enter Book Title : ")
    author = input("Enter Author Name : ")
    price = int(input("Enter Book Price : "))
    
    book = Book(book_id,title,author)
    
    book.set_price(price)
    
    library.add_book(book)
    print("Book added.")

while True:
    print("\n========== Library ==========")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Search Book")
    print("4. Exit")
    
    choice = int(input("Enter the choice : "))
    
    match choice:
        case 1:
            add_book()
        
        case 2:
            library.display_books()
            
        case 3:
            title = input("Enter the title for search : ")
            library.search_book(title)
            
        case 4:
            print("Thank You")
            break