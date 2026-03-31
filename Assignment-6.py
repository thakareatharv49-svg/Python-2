class Library:
    def __init__(self,book_name,author,available=True):
        self.book_name=book_name
        self.author=author
        self.available=available
    def checkout_book(self):
        if self.available:
            self.available=False
            print(f"{self.book_name} by {self.author} has been checked out ")
        else:
            print(f"{self.book_name} by {self.author} is not available")
    def return_book(self):
        if not self.available:
            self.available=True
            print(f"{self.book_name} by {self.author} has been returned")
        else:
            print(f"{self.book_name} by {self.author} has not been checked out")
    def display_book(self):
        status="available"if self.available else "Not available"
        print(f"{self.book_name} by {self.author} is {status}") 

book1=Library(1879,"Paul Hawking")
book2=Library("Harry Pottor","J.K Rolling")
book3=Library("Bird","Lily Jones")

book1.checkout_book()
book2.return_book()
book3.display_book()