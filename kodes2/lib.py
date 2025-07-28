class Library:
    available_books = ["Pyhton", "C", "C++", "DBMS", "math", "DS"]
    def __init__(self, student_name):
        self.name = student_name

    def display_books(self):
        for book in Library.available_books:
            print(book)

    def borrow_book(self, book_name):
        if book_name in Library.available_books:
            Library.available_books.remove(book_name)
            print("hello",self.name, "you borrowed", book_name)
        else:
            print( self.student_name,"sorry", book_name, "in not available here !")

    def return_book(self, book_name):
            Library.available_books.append(book_name)
            print("hello", self.name, "you returned book",book_name, "successfully, Thank you!")
        #else:
           # print( self.name,"sorry", book_name, "in not available here !")   

c1 = Library("yash")
c1.display_books()
c1.borrow_book("DBMS")
c1.display_books()
c1.return_book("DBMS")
