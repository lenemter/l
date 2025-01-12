# Задание 1: Открытие и чтение файла

Задание: Создать текстовый файл example.txt с несколькими строками текста. Реализовать функцию, которая читает содержимое файла, используя:

- Чтение всего файла сразу.
- Построчное чтение.

Реализация: Функция принимает аргумент, определяющий способ чтения файла (read_line_by_line). Если аргумент установлен в True, содержимое читается построчно. В противном случае файл читается полностью.

Код:

``` python
def read_file(read_line_by_line: bool) -> None:
    with open("example.txt", "r", encoding="UTF-8") as file:
        if read_line_by_line:
            for line in file:
                print(line.rstrip())
        else:
            print(file.read())
```

Пример вызова:

```python
print("--- Сначала обычное чтение ---")
read_file(False)

print("--- Теперь чтение по одной строчке ---")
read_file(True)
```

# Задание 2: Запись в файл

Задание: Написать программу, которая:

- Запрашивает текст у пользователя и записывает его в файл user_input.txt.
- Реализует возможность:
- - Полной перезаписи файла.
- - Добавления текста в конец существующего файла.

Реализация: Пользователь вводит текст и выбирает режим записи:

- Полная перезапись (w).
- Добавление текста в конец файла (a).

Код:

```python
new_content = input("Что вы хотите написать в файл user_input.txt: ")
override_previous_content = input("Перезаписать файл полностью или добавить в конец? Введите «П» если хотите перезаписать: ")

if override_previous_content.lower() == "п":
    mode = "w"
else:
    mode = "a"

with open("user_input.txt", mode, encoding="UTF-8") as file:
    file.write(new_content)

if override_previous_content.lower() == "п":
    print("Файл был перезаписан")
else:
    print("Ваш кусок текста был добавлен в конец файла")
```

# Задание 3: Обработка исключений при чтении файла

Задание: Модифицировать программу из Задания 1 так, чтобы она корректно обрабатывала исключение FileNotFoundError, возникающее при попытке открыть несуществующий файл. Вместо ошибки выводить понятное сообщение.

Реализация: Добавлен блок try-except для обработки исключения. Если файл не найден, выводится сообщение: "Файл «example2.txt» не найден."

Код:

```python
def read_file(read_line_by_line: bool) -> None:
    try:
        with open("example2.txt", "r", encoding="UTF-8") as file:
            if read_line_by_line:
                for line in file:
                    print(line.rstrip())
            else:
                print(file.read())
    except FileNotFoundError:
        print("Файл «example2.txt» не найден.")
```

Пример вызова:

```python
print("--- Сначала обычное чтение ---")
read_file(False)

print("--- Теперь чтение по одной строчке ---")
read_file(True)
```
