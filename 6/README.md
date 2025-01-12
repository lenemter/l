# Задание 1: Защита данных пользователя

Задание: Создать класс UserAccount с атрибутами:

- username (имя пользователя).
- email (электронная почта).
- Приватный атрибут __password (пароль).

Реализовать методы:

- set_password(new_password) для изменения пароля.
- check_password(password) для проверки введённого пароля.

Пароль хранится в приватном атрибуте __password.
Метод set_password обновляет значение пароля.
Метод check_password сравнивает введённый пароль с текущим.

Код:

```python
class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password  # Приватный атрибут

    def set_password(self, new_password):
        self.__password = new_password  # Изменение пароля

    def check_password(self, password):
        return self.__password == password  # Проверка пароля


if __name__ == "__main__":
    user = UserAccount("User1", "user1@example.com", "initial_pass")
    
    # Изменение пароля
    user.set_password("new_password")
    
    # Проверка нового пароля
    print(user.check_password("wrong_password"))  # Результат: False
    print(user.check_password("new_password"))    # Результат: True
```

# Задание 2: Полиморфизм и наследование

Задание: Создать базовый класс Vehicle с атрибутами:

- make (марка).
- model (модель).
- Метод get_info() для возврата информации о транспортном средстве.

Создать класс Car, наследующий от Vehicle, с дополнительным атрибутом:

- fuel_type (тип топлива).

Переопределить метод get_info() в классе Car для отображения информации о типе топлива.

Класс Car наследует атрибуты и методы от Vehicle.
Метод get_info переопределён, чтобы включать информацию о топливе.

Код:

```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)  # Вызов конструктора базового класса
        self.fuel_type = fuel_type

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}, Топливо: {self.fuel_type}"


if __name__ == "__main__":
    car = Car("Toyota", "Camry", "Бензин")
    print(car.get_info())  # Результат: Марка: Toyota, Модель: Camry, Топливо: Бензин
```
