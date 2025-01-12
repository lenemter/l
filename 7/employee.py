class Employee:
    def __init__(self, name: str, id: int) -> None:
        self.name = name
        self.id = id

    def get_info(self) -> str:
        return f"Employee: name='{self.name}' id={self.id}"
