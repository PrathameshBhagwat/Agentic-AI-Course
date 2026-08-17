class Books:
    def __init__(self,Book_ID,Book_Name,Author_Name):
        self.Book_ID = Book_ID
        self.Book_Name = Book_Name
        self.Author_Name=Author_Name
        self.Availability_Status = True

    def display_book(self):
        print("Book ID : ",self.Book_ID)
        print("Book Name : ",self.Book_Name)
        print("Author of the book : ",self.Author_Name)
        
    def issue_book(self):
        if self.Availability_Status == True:
            self.Availability_Status = False
            print(self.Book_Name," is issued successfully.")
        else:
            print(self.Book_Name," is already issued.")
    
    def return_book(self):
        input_id = int(input("Enter the book id for the issue : "))
        if self.Availability_Status == False:
            self.Availability_Status = True
            print(self.Book_Name,"is returned successfully.")
        else:
            print("The Book is not issued what are you returning...!")
            
        
    def availability(self):
        if self.Availability_Status == True:
            print("The Book is available")
        else:
            print("The Book is not available try after some time.")

        

books = {}

def add_book():
    book_id=int(input("Enter the Book id : "))
    if book_id in books:
        print("The book is already in the library")
        return
    
    book_name  =input("Enter the book name : ")
    author_name = input("Enter the Author name : ")
    
    book = Books(book_id,book_name,author_name)
    
    books[book_id]= book
    
    print("Book added successfully.")
    
def display_book():
    input_id = int(input("Enter the Book ID : "))
    
    if input_id in books:
        book = books[input_id]
        
        book.display_book()
    
    else:
        print("Book not found.")
        

def check_availability():
    input_id = int(input("Enter the Book ID : "))
        
    if input_id in books:
        book = books[input_id]
        book.availability()
        
    else:
        print("Book not found.")
        
def issue_book():
    input_id = int(input("Enter the Book ID : "))
        
    if input_id in books:
        book = books[input_id]
        book.issue_book()
        
    else:
        print("Book not found.")  

def return_book():
    input_id = int(input("Enter the Book ID : "))
        
    if input_id in books:
        book = books[input_id]
        book.return_book()
        
    else:
        print("Book not found.")
        

#Menu 
while True:
    print("1. Add Book")
    print("2. Display Book Details")
    print("3. Check the availability book")
    print("4. Issue book")
    print("5. Return book")
    print("6. Exit")
        
    choice = int(input("Enter your choice : "))
        
    match choice:
        case 1:
            add_book()
            
        case 2:
            display_book()
                
        case 3:
            check_availability()
                
        case 4:
            issue_book()

        case 5:
            return_book()

        case 6:
            print("Thank You for using the system.")
            break
        
        case _:
            print("Invalid Choice.")

            
        