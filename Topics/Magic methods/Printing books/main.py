class Book:
    def __init__(self, author, title, price, book_id):
        self.author = author
        self.title = title
        self.price = price
        self.book_id = book_id

    def __repr__(self):
        return f'{self.title} by {self.author}. ${self.price}. [{self.book_id}]'


# test = Book("George Orwell", "1984", 13.59, 1956789)
