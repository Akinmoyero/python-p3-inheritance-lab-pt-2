class Book:
    all_books = []
    
    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise Exception("Title must be a non-empty string.")
        self._title = value

class Author:
    all_authors = []
    
    def __init__(self, name):
        self.name = name
        Author.all_authors.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise Exception("Name must be a non-empty string.")
        self._name = value
    
    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]
    
    def books(self):
        return list(set(contract.book for contract in self.contracts()))
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Contract:
    all_contracts = []
    
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class.")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class.")
        if not isinstance(date, str) or not date.strip():
            raise Exception("Date must be a non-empty string.")
        if not isinstance(royalties, (int, float)) or royalties < 0:
            raise Exception("Royalties must be a non-negative number.")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        
        Contract.all_contracts.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]

# Example Usage (for testing purposes)
if __name__ == "__main__":
    author1 = Author("J.K. Rowling")
    book1 = Book("Harry Potter")
    contract1 = author1.sign_contract(book1, "2025-02-21", 15)
    
    print(author1.contracts())  # List of contracts
    print(author1.books())  # List of books
    print(author1.total_royalties())  # Total royalties earned
