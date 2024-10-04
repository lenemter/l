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
