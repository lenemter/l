# Задание 1: Импорт стандартных модулей

Задание: Использовать функцию sqrt() из модуля math для вычисления квадратного корня. Отобразить текущую дату и время с помощью модуля datetime.

Модуль math используется для выполнения математических операций.
Модуль datetime позволяет работать с текущей датой и временем.

Код:

```python
import math
import datetime

print(math.sqrt(144))  # Результат: 12.0
print(datetime.datetime.now())  # Отображает текущую дату и время
```

# Задание 2: Создание и использование собственного модуля

Задание: Создать модуль my_module.py с функцией, которая принимает два числа и возвращает их сумму. Импортировать созданный модуль в другой файл и вызвать его функцию.

Создан файл my_module.py с функцией sum, которая возвращает сумму двух аргументов.
В другом Python-файле модуль импортирован, и функция вызвана.

Код модуля my_module.py:

```python
def sum(a, b):
    return a + b
```

Код основного файла:

```python
import my_module

print(my_module.sum(155, 100))  # Результат: 255
```

# Задание 3: Создание и использование пакетов

Задание: Создать пакет, состоящий из нескольких модулей, каждый из которых выполняет свою задачу. Продемонстрировать импорт модулей из пакета и их использование.

Создан пакет package, содержащий два модуля:
numerical.py для операций с числами.
strings.py для работы со строками.
Импортированы модули из пакета и вызваны их функции.

Структура пакета:

```python
package/
│
├── __init__.py       # Указывает, что директория является пакетом
├── numerical.py      # Модуль для работы с числами
└── strings.py        # Модуль для работы со строками
```

Код модуля numerical.py:

``` python
import math

def f(x: float) -> float:
    return x ** 4 + math.sqrt(3 * x + 255 - 0.5) + 2 + math.cos(math.pi / 2)
```

Код модуля strings.py:

``` python
import random
import string

def random_string(length: int) -> str:
    return "".join(random.choices(string.ascii_letters, k=length))
```

Код основного файла:

```python
import package.numerical
import package.strings

# Примеры вызова функций из модуля numerical
print(package.numerical.f(1))
print(package.numerical.f(2))

# Примеры вызова функций из модуля strings
print(package.strings.random_string(10))
print(package.strings.random_string(20))
```
