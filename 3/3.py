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


def main():
    print("--- Сначала обычное чтение ---")
    read_file(False)

    print("--- Теперь чтение по одной строчке ---")
    read_file(True)


if __name__ == "__main__":
    main()
