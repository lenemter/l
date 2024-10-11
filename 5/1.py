# А как?

class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year
    
    def get_info(self) -> str:
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"


# class Book:
#     # title = ""
#     # author = ""
#     # year = 0

#     def get_info(self) -> str:
#         return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"


# b = Book()
# b.title = "A"
# b.author = "B"
# b.year = 1
# print(b.get_info())


# b2 = Book()
# b2.title = "C"
# b2.author = "D"
# b2.year = 2

# print(b2.get_info())
# print(b.get_info())
