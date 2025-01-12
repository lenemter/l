# Задание 1: Базовый класс и методы

Задание: Создать класс Book, который имеет:

- Атрибуты:
- - title (название книги).
- - author (автор книги).
- - year (год издания).
- Метод get_info(), возвращающий информацию о книге в формате: "Название книги: [title], Автор: [author], Год издания: [year]".

Определён класс Book с методом __init__ для инициализации атрибутов.
Метод get_info() возвращает строку с информацией о книге.
Код:

```python
class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year
    
    def get_info(self) -> str:
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"

# Пример использования
book = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)
print(book.get_info())
# Результат: Название книги: Мастер и Маргарита, Автор: Михаил Булгаков, Год издания: 1967
```

# Задание 2: Работа с конструктором

Задание: Определить класс Circle для представления круга. Использовать конструктор __init__ для инициализации радиуса (radius). Добавить методы:

- get_radius(), возвращающий текущий радиус.
- set_radius(new_radius), изменяющий радиус.
- Создать объект класса Circle, изменить его радиус и вывести обновлённый радиус.

В классе Circle реализованы методы для получения и изменения радиуса.
Создан объект, радиус которого был сначала выведен, затем изменён, и снова выведен.

Код:

```python
class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius
    
    def get_radius(self) -> float:
        return self.radius
    
    def set_radius(self, new_radius: float) -> None:
        self.radius = new_radius

# Пример использования
def main():
    circle = Circle(5)  # Создание круга с радиусом 5
    print(f"Радиус круга: {circle.get_radius()}")  # Результат: Радиус круга: 5

    circle.set_radius(10)  # Изменение радиуса
    print(f"Новый радиус круга: {circle.get_radius()}")  # Результат: Новый радиус круга: 10

if __name__ == "__main__":
    main()
```
