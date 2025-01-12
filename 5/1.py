class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year
    
    def get_info(self) -> str:
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"
