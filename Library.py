class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(f"'{self.title}' is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"You have borrowed '{self.title}' by {self.author}.")

    def return_book(self):
        if not self.is_borrowed:
            print(f"'{self.title}' was not borrowed.")
        else:
            self.is_borrowed = False
            print(f"You have returned '{self.title}'.")


# Test
book1 = Book("Atomic Habits", "James Clear")
book1.borrow()
book1.borrow()      
book1.return_book()
book1.return_book() 

