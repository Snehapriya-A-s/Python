class Publisher:
    def __init__(self, publisher):
        self.publisher = publisher
    def display(self):
        print("Publisher name : ", self.publisher)
class Book(Publisher):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display(self):
        super().display()
        print("Title of the book : ", self.title)
        print("Author of the book : ", self.author)
class Python(Book):
    def __init__(self, publication, author, title, price, numb):
        self.price = price
        self.noofpages = numb
        Book.__init__(self, title, author)
        Publisher.__init__(self, publication)
    def display(self):
        super().display()
        print("Price of the book : ", self.price)
        print("Number of pages in the book", self.noofpages)
b1 = Python("MARK LUTZ", "guido vann rossum ", "python language reference manual", 1858, 1350)
b1.display()