class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return self.__password == password


if __name__ == "__main__":
    user = UserAccount("AAA", "AAA@gmail.com", "12345678")
    user.set_password("qwerty")
    print(user.check_password("qwerty"))
